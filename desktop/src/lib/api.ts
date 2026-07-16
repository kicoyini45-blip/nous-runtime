export interface RuntimeConfig { url: string; token: string; }
type Envelope<T> = { ok: boolean; data?: T; error?: { code?: string; message?: string } };

let config: RuntimeConfig = { url: "http://localhost:8770", token: "" };

export function setConfig(value: RuntimeConfig) {
  config = value;
  sessionStorage.setItem("nous_server_url", value.url);
  sessionStorage.setItem("nous_server_token", value.token);
}

export function getConfig(): RuntimeConfig {
  return {
    url: sessionStorage.getItem("nous_server_url") || config.url,
    token: sessionStorage.getItem("nous_server_token") || config.token,
  };
}

export async function api<T = unknown>(path: string, options: RequestInit = {}): Promise<T> {
  const { url, token } = getConfig();
  const response = await fetch(`${url}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options.headers,
    },
  });
  const envelope = await response.json() as Envelope<T>;
  if (!response.ok || !envelope.ok) {
    throw new Error(envelope.error?.message || envelope.error?.code || `HTTP ${response.status}`);
  }
  return envelope.data as T;
}

export async function testConnection() {
  try {
    await api("/api/v1/status");
    return true;
  } catch {
    return false;
  }
}

export function subscribeRunEvents(
  runId: string,
  onEvent: (event: unknown) => void,
  options: { intervalMs?: number; afterSequence?: number } = {},
) {
  let active = true;
  let afterSequence = Math.max(0, options.afterSequence || 0);
  const intervalMs = Math.max(250, options.intervalMs || 1000);

  const poll = async () => {
    if (!active) return;
    try {
      const page = await api<{events: Array<Record<string, unknown>>; next_after_sequence: number}>(
        `/api/runtime/runs/${encodeURIComponent(runId)}/events?after_sequence=${afterSequence}&limit=200`,
      );
      for (const event of page.events) onEvent(event);
      afterSequence = page.next_after_sequence;
    } catch {
      // Preserve the cursor and retry after transient disconnects.
    } finally {
      if (active) window.setTimeout(poll, intervalMs);
    }
  };
  void poll();
  return { close: () => { active = false; }, cursor: () => afterSequence };
}

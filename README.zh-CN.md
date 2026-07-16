# Nous Runtime

Nous 是一个为人类服务，帮助人类理解、创造和管理复杂系统的长周期智能运行时。

Nous 通过一条受治理的运行路径协调对话、智能体、工作流、知识、工具、审批、事件、恢复与连接节点。Server Runtime 保持权威；终端和设备客户端仅作为视图与控制入口。

当前目标版本：`v0.1.0-alpha`。

## 为什么是 Nous

复杂工作往往跨越多次对话、多个进程和多台设备。Nous 在保留持久上下文与执行证据的同时，让状态变化、审批、失败与恢复对用户可见。系统以明确的状态归属和用户控制为基础。

## 核心能力

- 持久对话、受限上下文、滚动摘要、分页历史与流式导出。
- Agent 与 Multi-Agent 复用 Runtime、Workspace、Governance、Event 和 Artifact 合约。
- 受治理的 Workflow、Plugin、Connector 与 Knowledge Retrieval。
- 能力感知调度、资源限制、恢复、重放和检查。
- 支持 JSON 与非交互模式的原生终端体验。
- 面向本地及连接设备的 Server-authoritative 控制。

## 架构

```text
Terminal / SDK / HTTP / Mobile / Node
                 |
          Server Runtime
                 |
 Intent -> Context -> Decision -> Governance -> Execution
                 |                       |
          ConversationStore       ApprovalBroker
                 |
     RunStore / EventStream / Workflow / Agent
                 |
  Capability / Plugin / Connector / Knowledge / Node
```

权威状态保留在既有 Runtime Store 与 Registry 中。客户端不会创建平行的 Run、Event、Conversation、Approval、Workflow、Capability、Node 或 Workspace 状态。

## 快速开始

需要 Python 3.10 或更高版本。

```powershell
git clone https://github.com/kicoyini45-blip/nous-runtime.git
cd nous-runtime
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e .
nous
```

Linux：

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e .
nous
```

首次交互启动可创建本地 `.nous` 工作区。检查类命令不要求模型服务；自然语言模型能力需要配置兼容 Provider。

## 终端体验

运行 `nous` 会进入持久终端界面。自然语言输入沿受治理的执行路径处理。核心命令：

```text
/status    /runs      /run show   /approve
/pause     /resume    /cancel     /dashboard
/inspect   /context   /files      /tests
/clear     /help      /quit
```

- `Ctrl+C` 取消当前操作，但保留会话。
- `Ctrl+D` 或 `/quit` 正常退出。
- `--session ID` 重连指定会话。
- `--json` 输出 JSON Lines；`--quiet` 隐藏终端装饰。
- `--no-color` 和 `NO_COLOR` 环境变量关闭样式输出。
- 管道输入自动进入无提示的非 TTY 模式。
- 对话历史和事件重放按受限页面加载。

## 安全模型

Nous 在受治理操作前执行授权、策略和审批。Plugin 与 Connector 在声明、权限、版本、校验和或隔离条件不满足时应当失败关闭。Workspace 与 Library 身份沿 Runtime 请求传播。

Alpha 版本不宣称提供操作系统级沙箱。进程、容器和设备隔离取决于具体平台配置。HTTP 默认只绑定 localhost；若要暴露到受信主机之外，操作方必须配置认证与传输保护。

不要提交凭据、私钥、数据库、对话日志、Runtime JSONL 状态或本地配置。

## Alpha 范围

`v0.1.0-alpha` 面向本地开发、集成评估和 Runtime 合约审阅，包括终端客户端、HTTP Runtime 接口、受治理的产品集成、恢复、检查工具、SDK 基础能力与实验性多设备支持。

稳定版本发布前接口可能变化；除明确说明外，不承诺生产可用性或安全认证。

## 已知限制

- 模型对话需要配置兼容 Provider。
- 部分检索、语音、文档与 UI 功能需要可选依赖。
- Plugin 隔离依赖已配置的隔离后端；不把不受信的进程内执行视为已隔离。
- Multi-node 与 Mobile 路径仍为 Alpha，需要显式配对和部署配置。
- 可信进程内 Workflow Handler 使用协作式取消。
- 主要终端覆盖 Windows 与 Linux，其他平台尚不是发布目标。

## 平台支持

| 使用面 | Alpha 支持状态 |
| --- | --- |
| Windows Terminal | 支持 |
| Linux 终端 | 支持 |
| 中文与 Unicode | 支持 |
| 非 TTY / JSON Lines | 支持 |
| HTTP Server Runtime | 支持本地使用 |
| Android 控制客户端 | 实验性 |
| 分布式节点 | 实验性 |

## 开发

```bash
python -m pip install -e ".[dev]"
python -m ruff check nous_runtime tests
python -m compileall nous_runtime
python -m pytest -q
```

测试可能生成本地 Runtime 状态。请使用可丢弃工作区，并避免把生成状态加入源码管理。

## 贡献

提交变更前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [SECURITY.md](SECURITY.md)。变更应保持权威状态归属、失败关闭的安全行为、受限资源使用和用户控制。

## 许可证

Apache License 2.0，见 [LICENSE](LICENSE)。第三方声明与依赖许可证继续遵循各自条款。

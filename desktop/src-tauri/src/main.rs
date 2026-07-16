// Nous Control Center — Tauri Backend
// System tray, native notifications, auto-launch.

#![cfg_attr(
    all(not(debug_assertions), target_os = "windows"),
    windows_subsystem = "windows"
)]

use tauri::{
    Manager, SystemTray, SystemTrayEvent, SystemTrayMenu, SystemTrayMenuItem,
    CustomMenuItem, WindowEvent,
};

#[tauri::command]
fn get_version() -> String {
    env!("CARGO_PKG_VERSION").to_string()
}

#[tauri::command]
fn show_window(window: tauri::Window) {
    window.show().unwrap();
    window.set_focus().unwrap();
}

fn main() {
    let tray_menu = SystemTrayMenu::new()
        .add_item(CustomMenuItem::new("show", "Show Window"))
        .add_item(CustomMenuItem::new("status", "Brain: Disconnected"))
        .add_native_item(SystemTrayMenuItem::Separator)
        .add_item(CustomMenuItem::new("quit", "Quit"));

    let tray = SystemTray::new().with_menu(tray_menu);

    tauri::Builder::default()
        .system_tray(tray)
        .on_system_tray_event(|app, event| match event {
            SystemTrayEvent::MenuItemClick { id, .. } => match id.as_str() {
                "show" => {
                    if let Some(window) = app.get_window("main") {
                        window.show().unwrap();
                        window.set_focus().unwrap();
                    }
                }
                "quit" => std::process::exit(0),
                _ => {}
            },
            SystemTrayEvent::LeftClick { .. } => {
                if let Some(window) = app.get_window("main") {
                    window.show().unwrap();
                    window.set_focus().unwrap();
                }
            }
            _ => {}
        })
        .on_window_event(|event| {
            if let WindowEvent::CloseRequested { .. } = event.event() {
                event.window().hide().unwrap();
            }
        })
        .invoke_handler(tauri::generate_handler![get_version, show_window])
        .run(tauri::generate_context!())
        .expect("Failed to launch Nous Control Center");
}

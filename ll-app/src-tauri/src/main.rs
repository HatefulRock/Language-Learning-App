// CORRECT: This line MUST be the absolute first line of the file.
// No comments, no `use` statements, no blank lines before it.
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

#[tauri::command]
fn ping() -> &'static str {
    "pong"
}

fn main() {
    tauri::Builder::default()
        // The invoke_handler uses the `generate_handler!` macro
        // to find all functions marked as `#[tauri::command]`.
        .invoke_handler(tauri::generate_handler![ping])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
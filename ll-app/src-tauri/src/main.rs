// Prevents additional console window on Windows in release, DO NOT REMOVE!!
mod db;
mod models;
mod llm;


#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]


#[tauri::command]
async fn greet(name: String) -> String {
    format!("Hello, {}! You've been greeted from Rust!", name)
}



fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![greet]) // Add your command here
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
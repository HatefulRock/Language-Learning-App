use sea_orm::{Database, DatabaseConnection, DbErr};
use std::path::Path;

// This is the path where your database file will be stored.
const DB_PATH: &str = "app_data.sqlite";

pub async fn establish_connection() -> Result<DatabaseConnection, DbErr> {
    let db_exists = Path::new(DB_PATH).exists();

    if !db_exists {
        // Create the database file if it doesn't exist.
        // In a real app, you might want more robust error handling.
        std::fs::File::create(DB_PATH).expect("Failed to create database file");
    }

    // The database URL for SQLite is just "sqlite:" followed by the path.
    let db_url = format!("sqlite://{}", DB_PATH);
    
    // Establish the connection. SeaORM handles the connection pooling.
    Database::connect(&db_url).await
}
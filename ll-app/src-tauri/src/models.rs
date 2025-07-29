use sea_orm::entity::prelude::*;

// This defines the 'words' table in your database.
#[derive(Clone, Debug, PartialEq, DeriveEntityModel, Eq)]
#[sea_orm(table_name = "words")]
pub struct Model {
    #[sea_orm(primary_key)] // This field is the primary key
    pub id: i32,

    pub original_word: String,

    #[sea_orm(column_type = "Text")]
    pub translation: Option<String>,
    
    #[sea_orm(default_value = 1)]
    pub lookup_count: i32,
    
    // SeaORM can automatically manage timestamps
    pub created_at: ChronoDateTime,
}

#[derive(Copy, Clone, Debug, EnumIter, DeriveRelation)]
pub enum Relation {}

impl ActiveModelBehavior for ActiveModel {}
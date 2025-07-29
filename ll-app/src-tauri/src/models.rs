use sea_orm::entity::prelude::*;

// This defines the 'words' table in your database.
#[derive(Clone, Debug, PartialEq, DeriveEntityModel, Eq)]
#[sea_orm(table_name = "words")]
pub struct Model {
    #[sea_orm(primary_key)]
    pub id: i32,
    pub text: String,
    pub familiarity_score: i32,
    #[sea_orm(column_type = "Text", nullable = true)]
    pub source_sentence: Option<String>,
}

#[derive(Copy, Clone, Debug, EnumIter, DeriveRelation)]
pub enum Relation {}

impl ActiveModelBehavior for ActiveModel {}
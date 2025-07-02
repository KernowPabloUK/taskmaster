# Entity Relationship Diagram (ERD) for Category Model

## Category Entity

```
┌─────────────────────────────────┐
│            Category             │
├─────────────────────────────────┤
│ PK │ id          │ AutoField    │
│    │ name        │ CharField    │
│    │ created_at  │ DateTimeField│
│    │ updated_at  │ DateTimeField│
└─────────────────────────────────┘
```

### Field Details:
- **id**: Primary Key (AutoField) - Automatically generated unique identifier
- **name**: CharField(max_length=100) - Category name
- **created_at**: DateTimeField(auto_now_add=True) - Timestamp when record is created
- **updated_at**: DateTimeField(auto_now=True) - Timestamp when record is last updated

### Relationships:
- This is a standalone entity with no foreign key relationships shown
- In a task management system, this would typically have a One-to-Many relationship with Tasks

### Sample Data:
```
| id | name        | created_at          | updated_at          |
|----|-------------|---------------------|---------------------|
| 1  | Work        | 2025-07-02 10:00:00 | 2025-07-02 10:00:00 |
| 2  | Personal    | 2025-07-02 10:01:00 | 2025-07-02 10:01:00 |
| 3  | Urgent      | 2025-07-02 10:02:00 | 2025-07-02 10:02:00 |
```

### Business Rules:
- Category name should be unique
- Category name is required (not null)
- Category name should have reasonable length limit (100 characters)

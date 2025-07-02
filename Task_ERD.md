# Entity Relationship Diagram (ERD) for Task Model

## Task Entity with Category Relationship

```
┌─────────────────────────────────┐      ┌─────────────────────────────────┐
│             Task                │      │           Category              │
├─────────────────────────────────┤      ├─────────────────────────────────┤
│ PK │ id          │ AutoField    │      │ PK │ id          │ AutoField    │
│    │ title       │ CharField    │      │    │ name        │ CharField    │
│    │ due_date    │ DateField    │      │    │ created_at  │ DateTimeField│
│    │ completed   │ BooleanField │      │    │ updated_at  │ DateTimeField│
│ FK │ category_id │ ForeignKey   │ ───→ │                                 │
│    │ created_at  │ DateTimeField│      └─────────────────────────────────┘
│    │ updated_at  │ DateTimeField│
└─────────────────────────────────┘
```

## Field Details

### Task Model
- **id**: Primary Key (AutoField) - Automatically generated unique identifier
- **title**: CharField(max_length=200) - Task title/description
- **due_date**: DateField - When the task is due (nullable)
- **completed**: BooleanField(default=False) - Task completion status
- **category_id**: ForeignKey(Category) - Reference to Category model
- **created_at**: DateTimeField(auto_now_add=True) - Creation timestamp
- **updated_at**: DateTimeField(auto_now=True) - Last update timestamp

### Category Model (existing)
- **id**: Primary Key (AutoField) - Automatically generated unique identifier
- **name**: CharField(max_length=100, unique=True) - Category name
- **created_at**: DateTimeField(auto_now_add=True) - Creation timestamp
- **updated_at**: DateTimeField(auto_now=True) - Last update timestamp

## Relationships

### One-to-Many: Category → Task
- **Relationship**: One Category can have Many Tasks
- **Foreign Key**: Task.category_id references Category.id
- **Cardinality**: 1:N
- **Delete Behavior**: CASCADE (when category is deleted, all related tasks are deleted)

## Sample Data

### Categories
```
| id | name        | created_at          | updated_at          |
|----|-------------|---------------------|---------------------|
| 1  | Work        | 2025-07-02 10:00:00 | 2025-07-02 10:00:00 |
| 2  | Personal    | 2025-07-02 10:01:00 | 2025-07-02 10:01:00 |
| 3  | Urgent      | 2025-07-02 10:02:00 | 2025-07-02 10:02:00 |
```

### Tasks
```
| id | title              | due_date   | completed | category_id | created_at          |
|----|-------------------|------------|-----------|-------------|---------------------|
| 1  | Finish project    | 2025-07-05 | false     | 1           | 2025-07-02 11:00:00 |
| 2  | Buy groceries     | 2025-07-03 | true      | 2           | 2025-07-02 11:01:00 |
| 3  | Call client       | 2025-07-02 | false     | 3           | 2025-07-02 11:02:00 |
| 4  | Review documents  | NULL       | false     | 1           | 2025-07-02 11:03:00 |
```

## Business Rules

### Task Rules
- Task title is required (not null)
- Task title should have reasonable length limit (200 characters)
- Due date is optional (can be null)
- Completed defaults to False for new tasks
- Category is required (not null) - every task must belong to a category
- Tasks are ordered by due_date (null dates last), then by created_at

### Relationship Rules
- When a category is deleted, all associated tasks are also deleted (CASCADE)
- A task must always belong to exactly one category
- A category can have zero or many tasks

## Database Indexes
- Index on `due_date` for efficient date-based queries
- Index on `completed` for filtering completed/incomplete tasks
- Index on `category_id` (automatically created for foreign key)
- Composite index on `(completed, due_date)` for common filter combinations

# camel Folder - Python Best Practices

## Variable Naming Convention
- ALL VARIABLES MUST BE IN camelCase
- Use lowercase for first word, then uppercase first letter of subsequent words
- Example: `myVariableName = 5`, `apiKey = "abc123"`, `userId = 123`

## Functions
- Use camelCase for function names
- Example: `def calculateTotal()`, `def getUserData()`

## Classes
- Use PascalCase for class names (different from variables)
- Example: `class UserManager:`, `class DatabaseConnection:`

## Constants
- Use UPPER_SNAKE_CASE for constants (following Python convention)
- Example: `MAX_RETRIES = 5`, `DEFAULT_TIMEOUT = 30`

## Best Practices
- Avoid ambiguous abbreviations (e.g., use `userId` instead of `uid`)
- Keep naming consistent within modules
- Document complex variables/classes with docstrings
- Follow best practices from @../CLAUDE.md
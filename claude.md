# Claude Instructions for every Project

## Project Structure

- `DayXX/` - корневая папка для задания каждого дня
- `src/` — исходный код проекта
- `tests/` — тесты
- `pytest.ini` — конфигурация pytest

## Code Style & Standards

- Python 3.9+
- Use type hints for function parameters and return types
- Follow PEP 8 style guide
- Add docstrings to classes and public methods

## Testing

- Run tests with: `python -m pytest tests/ -v`
- All tests must pass before committing
- Write tests for new functionality

## Import Conventions

- Use relative imports from `src/` module
- Example: `from src.number import Number`

## Git Workflow

- Keep commits atomic and well-documented
- Use Russian for commit messages (if preferred by user)
- Test before committing

## Code Quality

- Remove trailing whitespace
- Use meaningful variable names
- Keep methods focused and single-responsibility
- Avoid side effects in pure functions

## Process

- Организуй процесс используя TDD подход: Тест - Код - Рефакторинг
- Двигайся маленькими шагами, запускай тесты после каждого изменения
- Используй принципы KISS и YAGNI
- Начинай с самого простого решения
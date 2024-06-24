## Assumptions

1. **Python 3 Installation**:
   - It is assumed that Python 3 (`python3`) is installed on the system and accessible via the command `python3`.

2. **Project Directory Structure**:
   - The project assumes the following directory structure:
     ```
     EverCraft/
     ├── src/
     │   └── character.py
     └── tests/
         └── test_character.py (or other test files)
     ```
   - `src/character.py` contains the `Character` class definition.
   - `tests/` directory includes unit test files such as `test_character.py`.

3. **Running Unit Tests**:
   - Unit tests are written using Python's `unittest` framework.
   - To execute tests, use the command:
     ```bash
     python3 -m unittest discover tests
     ```
   - This command discovers and runs all unit tests located in the `tests/` directory.

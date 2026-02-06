Perfect! I’ve gone through and **updated the full step-by-step assignment guide** for your colleague. Now, for **each section**, I’ve added a **one-line list of key concepts** learners are practising. I’ve also **removed tasks that involve features already in the base code**, so learners focus on improving, refactoring, testing, or adding new *extra* functionality, not repeating what already works.

---

# Book App Copilot CLI Assignment — Task Examples

---

## **Step 0 — Quick Start / Verification**

**Sub-Tasks:**

1. Run `python book_app.py list` to check the starter books.

   * Example: Verify that "The Hobbit", "1984", and "Dune" are listed correctly.
2. Open `data.json` to confirm starter data.

   * Example: Check the `read` property is correct (`true` for "1984", `false` for "The Hobbit").
3. Run `pytest` to ensure tests pass.

   * Example: Confirm that `test_add_book`, `test_mark_book_as_read`, and `test_remove_book` pass without errors.

**Key concepts:** environment setup, verification, test execution, basic app usage

---

## **Step 1 — First Steps (Targeting One File / Command)**

**Sub-Tasks:**

1. Analyse `book_app.py` with Copilot CLI.

   * Example: `@book_app.py Summarise the main() function and the responsibilities of each handler function.`
2. Improve a single function for readability.

   * Example: Refactor `show_books()` to align columns neatly or add separators between books.
3. Fix minor typos or unclear comments.

   * Example: Add a docstring to `handle_find()` explaining what it does.

**Key concepts:** file summarisation, function analysis, code readability, commenting

---

## **Step 1.5 — Modes of Interaction**

**Sub-Tasks:**

1. Use **Interactive mode** to improve a function line-by-line.

   * Example: Run `copilot` then ask it to refactor `get_user_choice()` in `utils.py` to validate input and handle invalid options.
2. Use **Plan mode** to outline improvements for `books.py`.

   * Example: Type `/plan` then ask: "How should I refactor the BookCollection class to separate data persistence from business logic?"
3. Use **Programmatic mode** to generate a helper function.

   * Example: `copilot -p "@books.py Add a list_unread_books() method that returns only books with read=False"`
4. Use **Auto-approve mode** (`/yolo`) to apply changes without confirmation prompts. **(ONLY INCLDUING THIS BECAUSE IT'LL BE IN THE VIDEO, WE DON'T TO INCLUDE IT)**

   * Example: Use `/yolo` then ask Copilot to add a "✅" emoji for read books in `print_books()` in `utils.py`.

**Key concepts:** Copilot CLI modes, planning, interactive edits, programmatic generation

---

## **Step 2 — Context and Conversations (Multi-File Analysis)**

**Sub-Tasks:**

1. Analyse `books.py` and `book_app.py` together.

   * Example: `@books.py @book_app.py Identify which functions modify the book collection and which only display data.`
2. Generate a **summary report** of all functions interacting with `data.json`.

   * Example: `@books.py List all methods in BookCollection that call save_books() or load_books().`
3. Suggest improvements across files.

   * Example: `@books.py @utils.py The utils.py has print_books() but book_app.py uses show_books(). Should we consolidate these?`

**Key concepts:** multi-file analysis, cross-file context, summarisation, improvement suggestions

---

## **Step 3 — Development Workflows**

**Sub-Tasks:**

1. Refactor an existing feature or helper function.

   * Example: `@books.py Refactor mark_as_read() to return the updated Book object instead of just True/False.`
2. Improve test coverage for existing features.

   * Example: `@tests/test_books.py @books.py Add tests for find_by_author() including edge cases like partial name matches and no results.`
3. Use Copilot CLI to review code quality.

   * Example: `/review` to review your staged changes, or `@book_app.py Review for code style, missing error handling, and potential improvements.`

**Key concepts:** refactoring, testing, code quality, workflow improvements

---

## **Step 4 — Create Specialised AI Assistants (Agents)**

**Sub-Tasks:**

1. Define 2-3 Copilot CLI agents relevant to the project.

   * Example: Create `.agent.md` files in the project:

     * `test-helper.agent.md` → generates or improves unit tests for `books.py`
     * `doc-helper.agent.md` → updates README and adds docstrings to functions
     * `data-validator.agent.md` → checks `data.json` for missing or malformed data (empty authors, year=0)
2. Use agents to complete tasks.

   * Example: `/agent data-validator` then ask: "Check data.json for books with empty author fields or invalid years."

**Key concepts:** agent creation, task delegation, automated reasoning

---

## **Step 5 — Automate Repetitive Tasks (Skills)**

**Sub-Tasks:**

1. Create skills for repetitive actions.

   * Example: Create a `book-summary` skill that generates a formatted markdown summary of all books in the collection.
2. Test skills with Copilot CLI.

   * Example: After creating the skill, run `/skills list` to verify it's installed, then trigger it with a matching prompt.
3. Use skills to improve workflow.

   * Example: Create a `test-stub` skill that automatically generates a pytest test function when you describe a new feature.

**Key concepts:** skill creation, automation, workflow efficiency

---

## **Step 6 — Connect to GitHub MCP**
**NOT SURE HOW THIS WILL GO, SINCE THIS PROJECT IS INSIDE THE COURSE REPO**


**Sub-Tasks:**

1. Use **GitHub MCP** to explore repository context.

   * Example: `List recent commits that modified books.py`
   * Example: `Show me the git history for the tests/ folder`
2. Use Copilot CLI with GitHub MCP to suggest improvements.

   * Example: `Based on recent changes to this repo, what features are still incomplete?`
3. Create issues or PRs using natural language.

   * Example: `Create an issue titled "Add export to CSV feature" with a description of the requirements.`

**Key concepts:** GitHub MCP integration, commit analysis, contextual code suggestions

---

## **Step 7 — Putting It All Together (Complete Feature Workflow)**

**Sub-Tasks:**

1. Plan and implement a new feature.

   * Example: `/plan Add a "list unread" command that shows only books with read=False`
2. Generate tests for the new feature.

   * Example: `@books.py @tests/test_books.py Generate a test for list_unread_books() that verifies it excludes read books.`
3. Refactor code as needed.

   * Example: Move the new `list_unread_books()` method into `BookCollection` class and add a `handle_unread()` function in `book_app.py`.
4. Update README to reflect the new feature.

   * Example: `@README.md Add documentation for the new "list unread" command.`

**Key concepts:** full workflow, feature implementation, testing, documentation updates

---

## **Optional / Extra Tasks**

* Improve README formatting and add usage examples for each command.
* Validate edge cases in `data.json` (empty authors, year=0) — see "Mysterious Book" entry.
* Consolidate `print_books()` in `utils.py` with `show_books()` in `book_app.py` (they do similar things).
* Add new commands like "mark" (mark a book as read) or "export" (export collection to CSV).
* Add a `list_by_year()` method to filter books by publication year range.

**Key concepts:** documentation, validation, refactoring, optional feature enhancement

---

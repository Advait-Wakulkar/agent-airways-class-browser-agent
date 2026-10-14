# Start Programming: Your First Browser Tool

This is a **real coding exercise** using the shared Agent Airways website. You can begin before your team is announced. You will use Python and Playwright, which we have already practiced. You **do not need Ollama or a language model** for this exercise.

## Goal

Write a Python function that selects a choice from a dropdown menu.

On the [Agent Airways practice website](https://onyourmark.github.io/browser-agent-form/travel/), the opening page contains three dropdown menus:

- **From:** the departure airport
- **To:** the destination airport
- **Passengers:** how many people are flying

You will write **one function** that works for all three.

## Get the code onto your computer

1. Open the [shared GitHub repository](https://github.com/onyourmark/agent-airways-class-browser-agent).
2. Click **Code** and then **Download ZIP**.
3. Extract the ZIP and open its folder in **VS Code**.
4. Open the file **`practice_dropdown.py`**. This is the file you will edit during class.

Downloading a ZIP is enough to start this exercise. Later, your team will use a GitHub fork and pull request to contribute its assigned tool to the shared project. Do not upload individual practice copies to the class repository's `main` branch.

## Make sure Playwright is installed

Open the VS Code terminal in the extracted folder. If you already installed Playwright for an earlier assignment, these commands may finish quickly.

**Windows:**

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
```

**Mac:**

```sh
python3 -m pip install -r requirements.txt
python3 -m playwright install chromium
```

If your computer uses `python` rather than `python3`, use `python`.

## Write your function

In `practice_dropdown.py`, find:

```python
def select_dropdown(field_id, choice):
```

Right now, the function has instructions and a line that raises `NotImplementedError`. Replace that line with Python statements that:

1. Find the dropdown using `browser_tools.page.locator("#" + field_id)`.
2. Select the requested choice using `.select_option(choice)`.
3. Read back the selected value using `.input_value()` and return it.

Try writing those statements yourself. The rest of the file is already written so that you can try your function.

## Run it

**Windows:**

```powershell
python practice_dropdown.py
```

**Mac:**

```sh
python3 practice_dropdown.py
```

You should see a real Chromium browser open the Agent Airways website. Your program should select:

- **From:** DCA (Washington Reagan)
- **To:** BOS (Boston)
- **Passengers:** 1

When your function works, the terminal prints:

```text
SUCCESS: The three dropdowns contain the requested values.
```

If the script shows `NotImplementedError`, you have not replaced the unfinished line. If it reports an exception, read the error and try to correct the code.

## If you finish early

Change the airport choices in the program and try another valid route. Then try an airport code that does **not** exist in the dropdown. Notice what Playwright does when it cannot find the option. This gives you the beginning of the error-handling work we will develop later.

## What happens after teams are announced?

Each team will be assigned **a specific browser capability** to develop for the shared agent. Some teams will work on form fields, some on buttons or seats, and others on observations or reliability. The class exercise above lets everyone begin programming immediately; it is **not** the team's final assignment.

Your team will eventually write its assigned tool, try it on the practice website, show that it works, and submit the contribution as a GitHub **pull request**. The TA will review it before it becomes part of the main program. You are **not expected to submit a pull request for this first practice exercise**.

The practice website makes no actual bookings and takes no payment.

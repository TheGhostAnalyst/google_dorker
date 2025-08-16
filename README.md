# The Ghost Analyst Google Dorker v1

⚠️ **Disclaimer:** This tool is for **educational purposes only**. Do **not** use it to access unauthorized data or hack websites. Use responsibly and ethically.

---

## Overview

The **Google Dorker** is a Python-based tool that allows users to perform **Google Dorking** in a structured way. It can:

- Open random default Google dorks.
- Let users input their own custom search queries.
- Display a list of default dorks for exploration.
- Provide ethical guidelines for using Google dorks.

This tool is intended for **OSINT practice, learning, and research purposes only**.



## Features

1. **Random Dork Opening**  
   Automatically opens a random Google Dork in your default web browser.

2. **Custom Search Query**  
   Input your own search query (e.g., `site:example.com intext:password`) and open it directly in your browser.

3. **Explore Default Dorks**  
   See a predefined list of popular Google Dorks and open any custom query.

4. **Ethics & Guidelines**  
   Educates users on responsible and ethical use of Google Dorking.

5. **Graceful Exit**  
   Handles `KeyboardInterrupt` to exit cleanly.


## Installation

1. Make sure you have **Python 3** installed.  
2. Install the required module:

```bash
pip install pyinputplus
````

3. Clone or download this repository and run the script:

```bash
git clone https://www.github.com/TheGhostAnalyst/google_dorker.git
```

---

## Usage

Run the script:

```bash
cd google_dorker
python3 google_dorker.py
```

Choose an option:

```
1. Directly open a random Google Dork
2. Input search query to open your own specified dork
3. Explore default dorks and choose which to open
4. Ethics and guidelines of Google Dorking
5. Exit
```

Follow the on-screen prompts to execute your desired option.

---

## Example

* **Random Dork:**
  Opens a Google search for something like:
  `https://www.google.com/search?q=site:example.com+intitle:index.of`

* **Custom Query:**
  Input `site:example.com intext:password` and open the corresponding Google search automatically.

---

## Ethics Reminder

* Only use on sites you **own** or have **permission** to test.
* Do **not** attempt to exploit sensitive or private data.
* Treat this tool as a **learning and OSINT aid** — not a hacking tool.

---

## License

This project is free to use for **educational purposes**. Use responsibly.

---

Created by **The Ghost Analyst 👻**

```

# programming-exercises

## About

A public repository where I share my programming exercises from <img src="https://cdn.simpleicons.org/codewars" width="15"/> **CodeWars**, <img src="https://cdn.simpleicons.org/leetcode" width="15"/> **LeetCode**, <img src="https://judge.beecrowd.com/favicon.ico?1756240500" width="15"/> **BeeCrowd** and others.

---

## How this repository is organized

This repository is structured by platform, programming language, and problem.

### 📁 General structure

```bash
platform/
└── language/
    └── problem_identifier/
        ├── solution.py
```

#### 📂 `platform/`

Represents the source of the problem (e.g., CodeWars, LeetCode, BeeCrowd).

#### 🧩 `language/`

Indicates the programming language used to solve the problem (e.g., python, javascript, go).

#### 🏷️ `problem_identifier/`

A unique folder for each problem.

* **CodeWars:** uses difficulty and name (e.g., `6kyu/array_diff`)
* **LeetCode:** uses problem ID and name (e.g., `1_two_sum`)
* **BeeCrowd:** uses problem ID and name (e.g., `1001_extremely_basic`)

---

#### 🧠 `solution.py`

Contains the main solution to the problem.

* Focused on logic and clarity
* No unnecessary input/output (except for platforms like BeeCrowd)

---

### 🟣 CodeWars

Problems are organized by difficulty (kyu level):

```
codewars/language/difficulty/exercise-name/
```

---

### 🟡 LeetCode

Problems are organized by their ID and name:

```
leetcode/language/difficult/
```

---

### 🟢 BeeCrowd

Problems are organized by their numeric ID and name:

```
beecrowd/language/difficult/
```

---

## Notes

* Each problem has its own folder
* Solutions are written to be clean and reusable
* README files may include explanations and complexity analysis

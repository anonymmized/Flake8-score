# Flake8 Score Calculator

A Python tool that calculates a code quality score based on Flake8 errors and maintainability index.

## Description

This tool analyzes Python code files and provides a comprehensive code quality report by combining:
- Flake8 style checks and error detection
- Radon maintainability index
- Custom scoring system (0-10 scale)

## Requirements

- Python 3.6+
- flake8
- radon

## Installation

1. Clone the repository:
```bash
git clone https://github.com/anonymmized/Flake8-score
```

2. Install dependencies:
```bash
pip install flake8 radon
```

## Usage

Run the script with a Python file as an argument:

```bash
python flake_score.py path/to/your/file.py
```

### Example Output
```
Analyzing example.py...
============================================================
Code Quality Report:
------------------------------------------------------------
Flake8 errors:           5
Maintainability Index:   85.5/100
Final Score:            8.5/10
Rating:                 Very Good
------------------------------------------------------------

Detailed Flake8 errors:
example.py:10:80: E501 line too long (82 > 79 characters)
...
```

## Scoring System

The final score (0-10) is calculated based on:
- Number of Flake8 errors (-0.5 points per error, max -5.0)
- Maintainability Index:
  - 90+ : No deduction
  - 80-89: -1 point
  - 70-79: -2 points
  - <70: -3 points

### Ratings
- 9.5-10.0: Perfect
- 8.5-9.4: Very Good
- 7.5-8.4: Good
- 6.5-7.4: Fair
- <6.5: Needs Improvement

## Contributing

Feel free to submit issues and enhancement requests!

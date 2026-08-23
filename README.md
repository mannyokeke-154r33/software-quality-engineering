# Software Quality Engineering

A testing-focused software engineering project built to demonstrate how requirements can be turned into meaningful automated tests.

## Overview

I built this project to practice software quality engineering through concrete test design instead of only checking whether code runs.

The repository uses a small Python module as the system under test and applies several testing techniques against it, including boundary-value analysis, equivalence partitioning, exception testing, stubs, and regression tests.

## What This Project Demonstrates

- Requirements-based test design
- Boundary-value analysis
- Equivalence partitioning
- Exception testing
- Stubbed dependencies
- Regression testing
- Parameterized tests
- Automated testing with Pytest
- Continuous integration with GitHub Actions

## Project Structure

```text
software-quality-engineering/
├── .github/
│   └── workflows/
│       └── tests.yml
├── src/
│   ├── discount_service.py
│   └── token_service.py
├── tests/
│   ├── test_discount_service.py
│   └── test_token_service.py
├── docs/
│   └── test-strategy.md
├── pyproject.toml
└── README.md
```

## System Under Test

The main example is a discount calculator with clear business rules:

- Purchase totals below $0 are invalid.
- Totals from $0 through $49.99 receive no discount.
- Totals from $50 through $99.99 receive a 5% discount.
- Totals of $100 or more receive a 10% discount.
- A maximum discount cap prevents unrealistic results.

These rules make the module useful for demonstrating test design around input classes and boundaries.

## Testing Approach

### Boundary-Value Analysis

The tests focus on values directly around important thresholds such as:

```text
49.99
50.00
50.01
99.99
100.00
100.01
```

This helps catch off-by-one and comparison errors near business-rule boundaries.

### Equivalence Partitioning

Inputs are grouped into behaviorally similar classes:

```text
Invalid totals:       total < 0
No-discount range:    0 <= total < 50
5% range:             50 <= total < 100
10% range:            total >= 100
```

Representative values from each class are tested instead of attempting every possible input.

### Exception Testing

The test suite verifies that invalid totals fail predictably with a clear exception rather than producing an incorrect financial result.

### Stubbed Dependency

The token service normally depends on a random token generator. Tests replace that dependency with a deterministic stub so the output is repeatable and easy to verify.

### Regression Testing

A regression test protects a previously identified edge case involving the exact $100 threshold. If later code changes accidentally move the threshold, the test fails immediately.

## Running the Tests

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[test]"
pytest -q
```

On Windows:

```text
.venv\Scripts\activate
```

## Continuous Integration

GitHub Actions runs the full Pytest suite automatically on pushes and pull requests to `main`.

That means changes are checked against the existing test suite before they are treated as safe.

## Why I Built It

I wanted a project that showed testing as an engineering activity rather than a final checklist.

The most useful shift for me was thinking in terms of questions such as:

- What are the valid and invalid input classes?
- Where are the important boundaries?
- What should fail, and how should it fail?
- Which dependencies make tests unpredictable?
- Which past defects should be protected with regression tests?

Those questions lead to stronger tests than simply writing a large number of test cases.

## Next Steps

- Add code coverage reporting
- Add mutation testing
- Add property-based testing
- Add integration tests for a small API
- Add defect reports linked to regression tests
- Compare black-box and white-box testing strategies

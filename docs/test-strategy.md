# Test Strategy

## Purpose

This project uses a small, understandable codebase to demonstrate deliberate test design. The goal is not to maximize the number of tests. The goal is to choose tests that provide useful evidence about software behavior.

## Requirements Under Test

### Discount Service

| ID | Requirement |
|---|---|
| R1 | Negative purchase totals must be rejected. |
| R2 | Totals below $50 receive a 0% discount. |
| R3 | Totals from $50 through $99.99 receive a 5% discount. |
| R4 | Totals of $100 or more receive a 10% discount. |
| R5 | Calculated discounts are rounded to cents. |
| R6 | A discount cannot exceed $250. |

### Token Service

| ID | Requirement |
|---|---|
| T1 | A user ID is required. |
| T2 | Token length must be at least eight characters. |
| T3 | The generator must return the requested number of characters. |
| T4 | Random generation must be replaceable during testing. |

## Equivalence Partitions

For the discount service, the input domain is divided into four main partitions:

1. Negative totals, invalid
2. $0.00 to $49.99, valid with 0% discount
3. $50.00 to $99.99, valid with 5% discount
4. $100.00 and above, valid with 10% discount

Representative inputs are selected from each partition.

## Boundary Analysis

The most important boundaries are $50 and $100. Tests therefore include values immediately below, exactly on, and immediately above each boundary.

| Boundary | Below | Exact | Above |
|---|---:|---:|---:|
| $50 | $49.99 | $50.00 | $50.01 |
| $100 | $99.99 | $100.00 | $100.01 |

## Exception Tests

Invalid inputs are expected to raise `ValueError`. Tests verify both the exception type and a meaningful part of the error message.

## Test Stubs

Random token generation creates nondeterministic output. The tests inject a fixed token generator instead. This isolates the service logic and makes each test repeatable.

A second intentionally broken stub verifies that the service detects an invalid dependency response.

## Regression Test

The exact $100 case is kept as an explicit regression test. A comparison written as `total > 100` instead of `total >= 100` would incorrectly give a $100 purchase the lower rate. Keeping a named test for this case documents the risk and protects it from returning.

## Automation

The suite is executed with Pytest locally and through GitHub Actions on pushes and pull requests to `main`.

## Exit Criteria

A change is considered test-clean when:

- All automated tests pass.
- No existing regression test is removed without justification.
- New business rules include tests for their valid, invalid, and boundary behavior where applicable.
- Tests remain deterministic and independent of external state.

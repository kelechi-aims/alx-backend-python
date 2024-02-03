# 0x03. Unittests and Integration Tests

This project focuses on understanding and implementing unit tests and integration tests for software development. Below, we'll discuss the concepts of unit testing, integration testing, and common testing patterns such as mocking, parametrizations, and fixtures.

**By**: Emmanuel Turlay, Staff Software Engineer at Cruise

**Weight**: 1

## Introduction

Unit testing is the process of testing individual units or components of a software application. These tests verify that each unit of the software performs as designed. On the other hand, integration testing focuses on testing how different parts of a system work together. Both unit tests and integration tests play a crucial role in ensuring the quality and reliability of software.

## Unit Tests

Unit testing involves testing a particular function or method to ensure it returns the expected results for various inputs. These tests typically cover standard inputs and corner cases. Unit tests should only focus on testing the logic defined within the tested function. Mocking is often used in unit testing to simulate the behavior of external dependencies, such as network or database calls.

## Integration Tests
Integration tests aim to test the end-to-end functionality of a code path. Unlike unit tests, integration tests involve testing interactions between different parts of the code, including external dependencies such as HTTP requests, file I/O, and database I/O. Low-level functions that make external calls are usually not mocked in integration tests.

## Common Testing Patterns

### Mocking

Mocking involves creating simulated versions of parts of the code that interact with other parts during testing. This allows developers to isolate the code being tested and control its behavior, especially when dealing with external dependencies.

### Parametrization

Parametrization allows developers to write a single test and run it with different inputs to verify the behavior of the code under various conditions. This helps ensure that the code handles different scenarios correctly.

### Fixtures
Fixtures are resources or setup steps required for testing, such as setting up a database or creating test data. Fixtures ensure that tests have access to the necessary resources and can be executed consistently.

## Resources
#### Read or watch:

- [unittest — Unit testing framework](https://intranet.alxswe.com/rltoken/a_AEObGK8jeqPtTPmm-gIA)
- [unittest.mock — mock object library](https://intranet.alxswe.com/rltoken/PKetnACd7FfRiU8_kpe5EA)
- [How to mock a readonly property with mock?](https://intranet.alxswe.com/rltoken/2ueVPK1kWZuz525FvZ1v2Q)
- [parameterized](https://intranet.alxswe.com/rltoken/mI7qc3Y42aZ7GTlLXDxgEg)
- [Memoization](https://intranet.alxswe.com/rltoken/x83Hdr54q4Vax5xQ2Z3HSA)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, **without the help of Google**:

- The difference between unit and integration tests.
- Common testing patterns such as mocking, parametrizations and fixtures

## Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- All your files must be executable
- All modules, classes, and functions should have proper documentation.
- All functions and coroutines must be type-annotated.

## Files

- [utils.py](https://intranet-projects-files.s3.amazonaws.com/webstack/utils.py)
- [client.py](https://intranet-projects-files.s3.amazonaws.com/webstack/client.py) 
- [fixtures.py](https://intranet-projects-files.s3.amazonaws.com/webstack/fixtures.py)

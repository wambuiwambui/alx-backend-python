Unittests and Integration Tests - README
This project is focused on unit testing and integration testing in Python. The goal is to understand the concepts of unit testing, mocking, parameterization, and integration testing using the unittest framework.

Project Overview
The project consists of several tasks that involve writing test cases for different Python functions and classes. We will be using the unittest framework, along with unittest.mock for mocking external dependencies.

Requirements
Python version: 3.7
Operating System: Ubuntu 18.04 LTS
Style guide: pycodestyle (version 2.5)
Task Descriptions
Task 0: Parameterize a unit test
In this task, we are provided with a function called utils.access_nested_map, and our objective is to write the first unit test for this function. We'll use the @parameterized.expand decorator to test the function for different inputs.

Task 1: Parameterize a unit test (exception case)
Continuing from Task 0, we will implement another unit test to check the exception handling of utils.access_nested_map when a KeyError is raised for certain inputs.

Task 2: Mock HTTP calls
In this task, we'll work with the function utils.get_json, which makes HTTP requests. We want to write unit tests for this function, but we don't want to make actual external HTTP calls. Instead, we will use unittest.mock.patch to mock the requests.get function.

Task 3: Parameterize and patch
The goal of this task is to test the functionality of the @memoize decorator. We'll use unittest.mock.patch to mock a method and then check if the @memoize decorator properly caches the results.

Task 4: Parameterize and patch as decorators
In this task, we'll write test cases for a class that interacts with an external API. We will use @patch as a decorator to mock the API calls and @parameterized.expand to test the class with different inputs.

Task 5: Mocking a property
Here, we'll learn how to mock a property that has been memoized using the @memoize decorator. We'll use unittest.mock.patch to test the behavior of the property.

Task 6: More patching
Continuing from the previous task, we'll extend our testing to cover more functionality of the API client class. We'll use @patch to mock the external API calls and verify the interactions.

Task 7: Parameterize
In this task, we'll implement a test case that uses @parameterized_class to test a class method with different inputs.

Task 8: Integration test: fixtures
Now, we'll move on to integration testing. The goal is to test a class method that interacts with an external API. We'll use fixtures to provide example payloads and unittest.mock.patch to mock the API calls.

Task 9: Integration tests (advanced)
In this final task, we'll perform integration tests for a class method using fixtures and unittest.mock.patch. We'll also use @parameterized_class to test the method with different inputs.
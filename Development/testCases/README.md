# Testing Applications
A test scenario measures functionality across a set of actions or conditions to verify the expected results. There is manual testing and automated testing.<br>
A key thing to remember when writing test cases is that they are intended to test a basic variable or task such as whether or not a discount code applaies to the right product on an e-commerce web page. 

## Test Script vs. Test Case
The difference between test cases vs. test scripts should also be clarified. A test script is a short program to test certain functionality. A test case is a document with steps to be completed as planned out ahead of time.<br>
Consider test cases as meticulously planned trip and test scripts to be more like a quick trip to the grocery store. 

- Functionality test case
- User interface test case
- Unit test case
- Integration test case
- Performance test case
- Security test case
- Database test case
- Usability test case

## How to Write Software Test Cases
1. Test Case ID - All test cases should bear a unique ID to represent them.
2. Test Description - This description should detail what unit, feature, or function is being tested or what is being verified
3. Assumptions and Pre-Conditions - Conditions that must be met before test case execution
4. Test Data - Variables and their value in the test case. 
5. Steps to be Executed - Easily repeatable steps as executed from teh end user's perspective. 
6. Expected Results - This indicates the result expected after the test case step execution
7. Actual Result and Post-Condition - What occurs as a result of the step execution 
8. Pass/Fail - Determine the pass/fail status depends on how the expected result and the actual result compare

## Standard Unit Test Case Format
1. Functions performed by the test
2. Data used in the test
3. Expected result from the test execution
4. Ensuring the test was executed in isolation from other parts of the codebase

## Types of Tests
There are three types of tests to be considered
1. Unit
2. Functional
3. End-to-end

Unit tests test the functionality of an individual unit of code isolated from its dependencies. These are the first liine of defense agains errors and inconsistencies.<br>
Functional tests test multiple components of a software product to make sure the components are working together properly. These tests focus on functionality that the user will be utilizing.<br>

## What to Test
In a Flask app, you may use a unit test to test:
1. Database models
2. Utility functions that your view functions call

Functional tests, meanwhile, should focus on how the view functions operate. For example:
1. Nominal conditions (GET, POST, etc) for a view function
2. Invalid HTTP methods are handled properly for a view function
3. Invalid data is passed to a view function

Focus on testing scenarios that the end user will interact with. The experience that the users of your product have is paramount.
*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page
Test TearDown  Reset Application

*** Test Cases ***
Register With Valid Username And Password
    Enter Username  pia
    Enter Password  valid789
    Confirm Password  valid789
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Enter Username  pi
    Enter Password  valid789
    Confirm Password  valid789
    Submit Registration
    Registration Should Fail With Message  Username is too short (min 3 characters)

Register With Valid Username And Too Short Password
    Enter username  pia
    Enter Password  short78
    Confirm Password  short78
    Submit Registration
    Registration Should Fail With Message  Password is too short (min 8 characters)

Register With Nonmatching Password And Password Confirmation
    Enter username  pia
    Enter Password  valid789
    Confirm Password  calid789
    Submit Registration
    Registration Should Fail With Message  Passwords do not match!

*** Keywords ***
Enter Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Enter Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Registration
    Click Button  Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page
Test TearDown  Reset Application

*** Test Cases ***
Register With Valid Username And Password
    Set Username  pia
    Set Password  valid789
    Confirm Password  valid789
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  pi
    Set Password  valid789
    Confirm Password  valid789
    Submit Registration
    Registration Should Fail With Message  Username is too short (min 3 characters)

Register With Valid Username And Too Short Password
    Set Username  pia
    Set Password  short78
    Confirm Password  short78
    Submit Registration
    Registration Should Fail With Message  Password is too short (min 8 characters)

Register With Nonmatching Password And Password Confirmation
    Set Username  pia
    Set Password  valid789
    Confirm Password  calid789
    Submit Registration
    Registration Should Fail With Message  Passwords do not match!

Login After Succesful Registration
    Set Username  pia
    Set Password  valid789
    Confirm Password  valid789
    Submit Registration
    Registration Should Succeed
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  pia
    Set Password  valid789
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  pi
    Set Password  valid789
    Confirm Password  valid789
    Submit Registration
    Registration Should Fail With Message  Username is too short (min 3 characters)
    Click Link  Login
    Set Username  pi
    Set Password  valid789
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Settings ***
Resource  resource.robot
Test Setup  Create User and Input New Command

*** Keywords ***
Create User and Input New Command
    Create User  kalle  kalle123
    Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pia  pia456789
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  valid789
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  pi  valid789
    Output Should Contain  Username is too short (min 3 characters)

Register With Username With Forbidden Characters And Valid Password
    Input Credentials  f00  valid789
    Output Should Contain  Username contains forbidden characters (only a-z allowed)

Register With Valid Username And Too Short Password
    Input Credentials  pia  p123
    Output Should Contain  Password is too short (min 8 characters)

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pia  lotsofletters
    Output Should Contain  Password cannot contain only letters

# py-passwords

![](https://github.com/michaelniemand/py-passwords/actions/workflows/docker-image.yml/badge.svg)

Prototype of a REST API that generates secure passwords written in Python using Flask.

## URI parameters

Generated passwords can be configured using URI parameters; Parameters are optional - if omitted, [defaults](#env-vars) are used

| Param | Type | Default | Description |
|-----|------|---------|-------------|
| length | Int | DEFAULT_LENGTH | length of password generated |
| special | Int | DEFAULT_SPECIAL | amount of special characters in the password generated |
| numbers | Int | DEFAULT_NUMBERS | amount of numbers in the password generated |
| pwcount | Int | DEFAULT_COUNT | amount of passwords generated |

## ENV vars

All parameters have defaults that can be provided as ENV vars. Also constraints for maximum length and maximum amount of passwords generated can be provided this way.

| Var | Type | Default | Description |
|-----|------|---------|-------------|
| DEFAULT_LENGTH | Int | 12 | length of password generated, corresponds to length parameter |
| DEFAULT_SPECIAL | Int | 0 | amount of special characters the password(s) should contain, corresponds to special parameter |
| DEFAULT_NUMBERS | Int | 0 | amount of digits the password(s) should contain, corresponds to numbers parameter |
| DEFAULT_COUNT | Int | 1 | amount of passwords to be generated, corresponds to pwcount parameter |
| MAXLENGTH | Int | 24 | maximum length of passwords a user can request |
| MAXCOUNT | Int | 100 | maximum amount of passwords a user can request |

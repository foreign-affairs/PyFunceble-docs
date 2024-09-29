# HTTP Status Code

## Why do we need it?

As we want to determine the availability of a domain, IP, or URL; one of our
testing method is the gathering of the HTTP status code.

## How does it work?

!!! note "Note"

    We never send a generic User-Agent. You can define your own or let
    PyFunceble choose one of the latest one of one of the major browser for
    you.

When it is the turn of the HTTP status code lookup tool to try to gather a
status for the given subject, an HTTP query is made to the given IP, domain
or subject.

When testing for a domain, a successful HTTP response is considered as
`ACTIVE`.

Otherwise, the following default classification applies.

!!! note "Note"

    The classification can be changed by end-user through their configuration
    file.

### As ACTIVE

Please note that the following HTTP status codes are considered as ACTIVE.

If you are using the CLI with the analytic files generated, you will get any
matching subject flagged as ACTIVE officially and into your analytic files.

- `100`: Continue
- `101`: Switching Protocols
- `102`: Processing
- `200`: OK
- `201`: Created
- `202`: Accepted
- `203`: Non-Authoritative Information
- `204`: No Content
- `205`: Reset Content
- `206`: Partial Content
- `207`: Multi-Status
- `208`: Already Reported
- `226`: IM User
- `429`: Too Many Request.

## As potentially ACTIVE

Please note that the following HTTP status codes are considered as potentially
ACTIVE but still officially reported as ACTIVE when caught.

If you are using the CLI with the analytic files generated, you will get any
matching subject flagged as ACTIVE officially and into your analytic files as
potentially ACTIVE.

- `300`: Multiple Choices
- `301`: Moved Permanently
- `302`: Found
- `303`: See Other
- `304`: Not Modified
- `305`: Use Proxy
- `307`: Temporary Redirect
- `308`: Permanent Redirect
- `403`: Forbidden
- `405`: Method Not Allowed
- `406`: Not Acceptable
- `407`: Proxy Authentication Required
- `408`: Request Timeout
- `411`: Length Required
- `413`: Payload Too Large
- `417`: Expectation Failed
- `418`: I'm a teapot
- `421`: Misdirect Request
- `422`: Unprocessable Entity
- `423`: Locked
- `424`: Failed Dependency
- `426`: Upgrade Required
- `428`: Precondition Required
- `431`: Request Header Fields Too Large
- `500`: Internal Server Error
- `501`: Not Implemented
- `502`: Bad Gateway
- `503`: Service Unavailable
- `504`: Gateway Timeout
- `505`: HTTP Version Not Supported
- `506`: Variant Also Negotiates
- `507`: Insufficient Storage
- `508`: Loop Detected
- `510`: Not Extended
- `511`: Network Authentication Required

### As INACTIVE or potentially INACTIVE

Please note that the following HTTP status codes are considered as INACTIVE or
potentially INACTIVE. Therefore officially reported as INACTIVE when caught.

If you are using the CLI with the analytic files generated, you will get any
matching subject flagged as INACTIVE officially and into your analytic files as
potentially INACTIVE.

- `400`: Bad Request
- `402`: Payment Required
- `404`: Not Found
- `409`: Conflict
- `410`: Gone
- `412`: Precondition Failed
- `414`: Request-URI Too Long
- `415`: Unsupported Media Type
- `416`: Request Range Not Satisfiable
- `451`: Unavailable For Legal Reasons

## How to use it?

You can simply allow the usage of the HTTP status code lookup through:

- the (Python) API,
- the CLI argument,
- or, your configuration file.

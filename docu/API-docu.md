# API-documentation

## Authentification

### <code>GET /login</code>
- Description <br>
    Return login page
- URL Params: <br>
    None
- Body Params: <br>
    None
- Responses:
    - Success respone (200): <br>
            "GET /sign-in HTTP/1.1" 200

### <code>POST /login</code>
- Description <br>
    Logs user in.
- URL Params: <br>
    None
- Body Params: <br>
    - email:string
    - password:string
- Responses:
    - Redirection (302): <br>
        - if password is correct, redirects to <code>/</code><br>
                "POST /login HTTP/1.1" 302 <br>
                "GET / HTTP/1.1" 200

### <code>GET /register</code>
- Description <br>
    Return register page
- URL Params: <br>
    None
- Responses:
    - Success respone (200): <br>
            "GET /register HTTP/1.1" 200

### <code>POST /register</code>
- Description <br>
    Creates user account.
- URL Params: <br>
    None
- Body Params: <br>
    - email:string
    - password:string
- Responses:
    - Redirection (302): <br>
        - if inputs filled, it creates the account and redirects to <code>/login</code><br>
                "POST /register HTTP/1.1" 302 <br>
                "GET /login HTTP/1.1" 200


### <code>GET /logout</code>
- Description <br>
    Logs user out.
- URL Params: <br>
    None
- Body Params: <br>
    None
- Responses:
    - Redirection (302): logs user out and redirects to <code>/login</code><br>
        
            "GET /logout HTTP/1.1" 302
            "GET /sign-in HTTP/1.1" 200

## Lamp API

### <code> GET /api/lamp/<lamp_id>/ </code>
- Description <br>
    Return lamp luminosity in json format (require login)
- URL Params: <br>
    - lamp_id:string (example:lamp1a)
- Body Params: <br>
    None
- Responses:
    - Success respone (200): Return value of specified lamp<br>
            "GET /api/lamp/ HTTP/1.1" 200

### <code> POST /api/lamp/<lamp_id>/ </code>
- Description <br>
    Set the lumunosity of specified lamp (require login)
- URL Params: <br>
    - lamp_id:string (example:lamp1a)
- Body Params: <br>
    None
- Responses:
    - Success respone (200): Set brightness of specified lamp<br>
            "POST /api/lamp/ HTTP/1.1" 200

### <code>GET /api/lamp/all/ </code>
- Description <br>
    Return lamp luminosity of all the lamps in json format (require login)
- URL Params: <br>
    None
- Body Params: <br>
    None
- Responses:
    - Success respone (200): Return value of all lamps<br>
            "GET /api/lamp/all HTTP/1.1" 200

### <code> POST /api/lamp/all/ </code>
- Description <br>
    Set the lumunosity of all lamps. (require login)
- URL Params: <br>
    None
- Body Params: <br>
    - dimming:integer
- Responses:
    - Success respone (200): Set brightness of all the lamps<br>
            "POST /api/lamp/all HTTP/1.1" 200

## Other pages

### <code>GET /</code>
- Description <br>
    Return the lamp dashboard page. (require login)
- URL Params: <br>
    None
- Body Params: <br>
    None
- Responses:
    - Success respone (200): <br>
            "GET / HTTP/1.1" 200

### <code>GET /history</code>
- Description <br>
    Return the lamp history page. (require login)
- URL Params: <br>
    None
- Body Params: <br>
    None
- Responses:
    - Success respone (200): <br>
            "GET /history HTTP/1.1" 200
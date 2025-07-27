# Security Measures Implemented

## Django Settings

- DEBUG = False
- SECURE_BROWSER_XSS_FILTER = True
- X_FRAME_OPTIONS = 'DENY'
- SECURE_CONTENT_TYPE_NOSNIFF = True
- SESSION_COOKIE_SECURE = True
- CSRF_COOKIE_SECURE = True

## Forms

- `{% csrf_token %}` included in all POST forms

## Content Security Policy

- Configured via `django-csp` middleware
- Blocks untrusted JS and CSS

## Input Validation

- Used Django ORM and `Q` objects
- Avoided raw SQL

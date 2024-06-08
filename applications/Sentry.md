# Sentry

At Nexirift, we use Sentry to track errors and exceptions.

1. Visit Applications > Applications > Create With Wizard:
    - **Name:** Sentry
    - **Slug:** sentry
    - **Group:** Internal
    - **Policy engine mode:** All
    - **Launch URL:** https://sentry.nexirift.com
    - **Provider type:** SAML (Security Assertion Markup Language)
2. Follow Authentik docs:
   https://docs.goauthentik.io/integrations/services/sentry/
3. Go to `Policy / Group / User Bindings` section for the `Sentry` application.
4. Bind existing policy as `Group` for the `Nexirift Developers` group.

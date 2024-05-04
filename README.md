<p align="center">
<img src="https://raw.githubusercontent.com/Nexirift/.github/main/banner.svg" width="300" />
</p>

# Authentik

A repository to hold configs for the authentication solution we use:
[Authentik](https://goauthentik.io/).

## Policies

### Nexirift-User-Settings-Authorization

The purpose of this policy is to allow users to upload avatars, banners and
backgrounds.

#### Setup

1. Create a new **expression** policy (Customization > Policies):
    - **Name:** nexirift-user-settings-authorization
    - **Expression:** _Copy the contents of this
      [file](https://raw.githubusercontent.com/Nexirift/authentik/main/policies/nexirift-user-settings-authorization.py)_.
2. Create a three new prompts (Flow and Stages > Prompts):
    1. Avatar
        - **Name:** nexirift-user-settings-field-avatar
        - **Field Key:** attributes.avatar
        - **Label:** User Avatar
        - **Type:** File
        - **Order:** 300
    2. Banner
        - **Name:** nexirift-user-settings-field-banner
        - **Field Key:** attributes.banner
        - **Label:** User Banner
        - **Type:** File
        - **Order:** 301
    3. Background
        - **Name:** nexirift-user-settings-field-background
        - **Field Key:** attributes.background
        - **Label:** User Background
        - **Type:** File
        - **Order:** 302
3. Edit `default-user-settings` (Flow and Stages > Stages):
    - Select the fields that we created earlier.
    - Select the validation (expression) policy.

### Nexirift-Enforce-Case-Sensitive-Usernames

The purpose of this policy is to ensure that usernames are case-sensitive.

#### Setup

1. Create a new **expression** policy (Customization > Policies):
    - **Name:** nexirift-enforce-case-sensitive-usernames
    - **Expression:** _Copy the contents of this
      [file](https://raw.githubusercontent.com/Nexirift/authentik/main/policies/nexirift-enforce-case-sensitive-usernames.py)_.
2. Enforce it on all enrollment flows (Flow and Stages > Stages).

## Property Mappings

### Profile

The purpose of this property mapping is to expose picture, avatar, banner, and
backgrounds.

#### Setup

1. Uncheck `Hide managed mappings` (Customization > Property Mappings).
2. Edit `authentik default OAuth Mapping: OpenID 'profile'`:
    - **Expression:** _Copy the contents of this
      [file](https://raw.githubusercontent.com/Nexirift/authentik/main/property-mappings/profile.py)_.

## Credits

Media upload expressions were taken from
[this discussion](https://github.com/goauthentik/authentik/discussions/6824) and
edited to fit our needs.

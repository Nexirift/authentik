# Policies

## Nexirift-User-Settings-Authorization

The purpose of this policy is to allow users to upload avatars, banners and
backgrounds.

### Setup

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
4. Edit `Avatars` in System > Settings:
    - Add `attributes.avatar` is before all other fields.
    - Final example: `attributes.avatar,gravatar,initials`.

## Nexirift-Enforce-Case-Sensitive-Usernames

The purpose of this policy is to ensure that usernames are case-sensitive.

### Setup

1. Create a new **expression** policy (Customization > Policies):
    - **Name:** nexirift-enforce-case-sensitive-usernames
    - **Expression:** _Copy the contents of this
      [file](https://raw.githubusercontent.com/Nexirift/authentik/main/policies/nexirift-enforce-case-sensitive-usernames.py)_.
2. Enforce it on all enrollment flows (Flow and Stages > Stages).

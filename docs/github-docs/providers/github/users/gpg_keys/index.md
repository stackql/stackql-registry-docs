---
title: gpg_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - gpg_keys
  - users
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gpg_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.users.gpg_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `integer` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="can_certify" /> | `boolean` |
| <CopyableCode code="can_encrypt_comms" /> | `boolean` |
| <CopyableCode code="can_encrypt_storage" /> | `boolean` |
| <CopyableCode code="can_sign" /> | `boolean` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="emails" /> | `array` |
| <CopyableCode code="expires_at" /> | `string` |
| <CopyableCode code="key_id" /> | `string` |
| <CopyableCode code="primary_key_id" /> | `integer` |
| <CopyableCode code="public_key" /> | `string` |
| <CopyableCode code="raw_key" /> | `string` |
| <CopyableCode code="revoked" /> | `boolean` |
| <CopyableCode code="subkeys" /> | `array` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_gpg_key_for_authenticated_user" /> | `SELECT` | <CopyableCode code="gpg_key_id" /> | View extended details for a single GPG key. Requires that you are authenticated via Basic Auth or via OAuth with at least `read:gpg_key` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
| <CopyableCode code="list_gpg_keys_for_authenticated_user" /> | `SELECT` |  | Lists the current user's GPG keys. Requires that you are authenticated via Basic Auth or via OAuth with at least `read:gpg_key` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
| <CopyableCode code="list_gpg_keys_for_user" /> | `SELECT` | <CopyableCode code="username" /> | Lists the GPG keys for a user. This information is accessible by anyone. |
| <CopyableCode code="create_gpg_key_for_authenticated_user" /> | `INSERT` | <CopyableCode code="data__armored_public_key" /> | Adds a GPG key to the authenticated user's GitHub account. Requires that you are authenticated via Basic Auth, or OAuth with at least `write:gpg_key` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
| <CopyableCode code="delete_gpg_key_for_authenticated_user" /> | `DELETE` | <CopyableCode code="gpg_key_id" /> | Removes a GPG key from the authenticated user's GitHub account. Requires that you are authenticated via Basic Auth or via OAuth with at least `admin:gpg_key` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |

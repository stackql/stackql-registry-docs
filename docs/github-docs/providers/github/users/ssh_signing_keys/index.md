---
title: ssh_signing_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - ssh_signing_keys
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
<tr><td><b>Name</b></td><td><code>ssh_signing_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.users.ssh_signing_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `integer` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="key" /> | `string` |
| <CopyableCode code="title" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_ssh_signing_key_for_authenticated_user" /> | `SELECT` | <CopyableCode code="ssh_signing_key_id" /> | Gets extended details for an SSH signing key. You must authenticate with Basic Authentication, or you must authenticate with OAuth with at least `read:ssh_signing_key` scope. For more information, see "[Understanding scopes for OAuth apps](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/)." |
| <CopyableCode code="list_ssh_signing_keys_for_authenticated_user" /> | `SELECT` |  | Lists the SSH signing keys for the authenticated user's GitHub account. You must authenticate with Basic Authentication, or you must authenticate with OAuth with at least `read:ssh_signing_key` scope. For more information, see "[Understanding scopes for OAuth apps](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/)." |
| <CopyableCode code="list_ssh_signing_keys_for_user" /> | `SELECT` | <CopyableCode code="username" /> | Lists the SSH signing keys for a user. This operation is accessible by anyone. |
| <CopyableCode code="create_ssh_signing_key_for_authenticated_user" /> | `INSERT` | <CopyableCode code="data__key" /> | Creates an SSH signing key for the authenticated user's GitHub account. You must authenticate with Basic Authentication, or you must authenticate with OAuth with at least `write:ssh_signing_key` scope. For more information, see "[Understanding scopes for OAuth apps](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/)." |
| <CopyableCode code="delete_ssh_signing_key_for_authenticated_user" /> | `DELETE` | <CopyableCode code="ssh_signing_key_id" /> | Deletes an SSH signing key from the authenticated user's GitHub account. You must authenticate with Basic Authentication, or you must authenticate with OAuth with at least `admin:ssh_signing_key` scope. For more information, see "[Understanding scopes for OAuth apps](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/)." |

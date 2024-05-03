---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
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
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.users.keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `integer` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="key" /> | `string` |
| <CopyableCode code="read_only" /> | `boolean` |
| <CopyableCode code="title" /> | `string` |
| <CopyableCode code="url" /> | `string` |
| <CopyableCode code="verified" /> | `boolean` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_public_ssh_key_for_authenticated_user" /> | `SELECT` | <CopyableCode code="key_id" /> | View extended details for a single public SSH key. Requires that you are authenticated via Basic Auth or via OAuth with at least `read:public_key` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
| <CopyableCode code="list_public_ssh_keys_for_authenticated_user" /> | `SELECT` |  | Lists the public SSH keys for the authenticated user's GitHub account. Requires that you are authenticated via Basic Auth or via OAuth with at least `read:public_key` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
| <CopyableCode code="create_public_ssh_key_for_authenticated_user" /> | `INSERT` | <CopyableCode code="data__key" /> | Adds a public SSH key to the authenticated user's GitHub account. Requires that you are authenticated via Basic Auth, or OAuth with at least `write:public_key` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
| <CopyableCode code="delete_public_ssh_key_for_authenticated_user" /> | `DELETE` | <CopyableCode code="key_id" /> | Removes a public SSH key from the authenticated user's GitHub account. Requires that you are authenticated via Basic Auth or via OAuth with at least `admin:public_key` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |

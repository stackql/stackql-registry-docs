---
title: social_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - social_accounts
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
<tr><td><b>Name</b></td><td><code>social_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.users.social_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="provider" /> | `string` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_social_accounts_for_authenticated_user" /> | `SELECT` |  | Lists all of your social accounts. |
| <CopyableCode code="list_social_accounts_for_user" /> | `SELECT` | <CopyableCode code="username" /> | Lists social media accounts for a user. This endpoint is accessible by anyone. |
| <CopyableCode code="add_social_account_for_authenticated_user" /> | `INSERT` | <CopyableCode code="data__account_urls" /> | Add one or more social accounts to the authenticated user's profile. This endpoint is accessible with the `user` scope. |
| <CopyableCode code="delete_social_account_for_authenticated_user" /> | `DELETE` | <CopyableCode code="data__account_urls" /> | Deletes one or more social accounts from the authenticated user's profile. This endpoint is accessible with the `user` scope. |

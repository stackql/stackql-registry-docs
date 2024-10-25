---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - users
  - openai    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage OpenAI and ChatGPT resources using SQL.
custom_edit_url: null
image: /img/providers/openai/stackql-openai-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.users.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier, which can be referenced in API endpoints |
| <CopyableCode code="name" /> | `string` | The name of the user |
| <CopyableCode code="added_at" /> | `integer` | The Unix timestamp (in seconds) of when the user was added. |
| <CopyableCode code="email" /> | `string` | The email address of the user |
| <CopyableCode code="object" /> | `string` | The object type, which is always `organization.user` |
| <CopyableCode code="role" /> | `string` | `owner` or `reader` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_users" /> | `SELECT` |  |
| <CopyableCode code="retrieve_user" /> | `SELECT` | <CopyableCode code="user_id" /> |
| <CopyableCode code="delete_user" /> | `DELETE` | <CopyableCode code="user_id" /> |
| <CopyableCode code="modify_user" /> | `UPDATE` | <CopyableCode code="user_id, data__role" /> |

---
title: project_users
hide_title: false
hide_table_of_contents: false
keywords:
  - project_users
  - projects
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
<tr><td><b>Name</b></td><td><code>project_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.projects.project_users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier, which can be referenced in API endpoints |
| <CopyableCode code="name" /> | `string` | The name of the user |
| <CopyableCode code="added_at" /> | `integer` | The Unix timestamp (in seconds) of when the project was added. |
| <CopyableCode code="email" /> | `string` | The email address of the user |
| <CopyableCode code="object" /> | `string` | The object type, which is always `organization.project.user` |
| <CopyableCode code="role" /> | `string` | `owner` or `member` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_project_users" /> | `SELECT` | <CopyableCode code="project_id" /> |
| <CopyableCode code="retrieve_project_user" /> | `SELECT` | <CopyableCode code="project_id, user_id" /> |
| <CopyableCode code="create_project_user" /> | `INSERT` | <CopyableCode code="project_id, data__role, data__user_id" /> |
| <CopyableCode code="delete_project_user" /> | `DELETE` | <CopyableCode code="project_id, user_id" /> |
| <CopyableCode code="modify_project_user" /> | `UPDATE` | <CopyableCode code="project_id, user_id, data__role" /> |

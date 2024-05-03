---
title: projects_members
hide_title: false
hide_table_of_contents: false
keywords:
  - projects_members
  - project_members
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.project_members.projects_members" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of this user. |
| <CopyableCode code="avatar" /> | `string` | ID of the file for the Avatar of this member. |
| <CopyableCode code="createdAt" /> | `number` | Timestamp in milliseconds when this member was added. |
| <CopyableCode code="email" /> | `string` | The email of this member. |
| <CopyableCode code="role" /> | `string` | Role of this user in the project. |
| <CopyableCode code="uid" /> | `string` | The ID of this user. |
| <CopyableCode code="username" /> | `string` | The unique username of this user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_project_members" /> | `SELECT` | <CopyableCode code="idOrName, teamId" /> | Lists all members of a project. |
| <CopyableCode code="remove_project_member" /> | `DELETE` | <CopyableCode code="idOrName, teamId, uid" /> | Remove a member from a specific project |
| <CopyableCode code="_get_project_members" /> | `EXEC` | <CopyableCode code="idOrName, teamId" /> | Lists all members of a project. |
| <CopyableCode code="add_project_member" /> | `EXEC` | <CopyableCode code="idOrName, teamId, data__role" /> | Adds a new member to the project. |

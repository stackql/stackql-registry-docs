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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.project_members.projects_members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of this user. |
| `avatar` | `string` | ID of the file for the Avatar of this member. |
| `createdAt` | `number` | Timestamp in milliseconds when this member was added. |
| `email` | `string` | The email of this member. |
| `role` | `string` | Role of this user in the project. |
| `uid` | `string` | The ID of this user. |
| `username` | `string` | The unique username of this user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_project_members` | `SELECT` | `idOrName, teamId` | Lists all members of a project. |
| `remove_project_member` | `DELETE` | `idOrName, teamId, uid` | Remove a member from a specific project |
| `_get_project_members` | `EXEC` | `idOrName, teamId` | Lists all members of a project. |
| `add_project_member` | `EXEC` | `idOrName, teamId, data__role` | Adds a new member to the project. |

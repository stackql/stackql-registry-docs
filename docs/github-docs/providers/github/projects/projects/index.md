---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - projects
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.projects.projects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` | Name of the project |
| `state` | `string` | State of the project; either 'open' or 'closed' |
| `body` | `string` | Body of the project |
| `organization_permission` | `string` | The baseline permission that all organization members have on this project. Only present if owner is an organization. |
| `owner_url` | `string` |  |
| `url` | `string` |  |
| `created_at` | `string` |  |
| `columns_url` | `string` |  |
| `node_id` | `string` |  |
| `creator` | `object` | A GitHub user. |
| `private` | `boolean` | Whether or not this project can be seen by everyone. Only present if owner is an organization. |
| `html_url` | `string` |  |
| `updated_at` | `string` |  |
| `number` | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `project_id` | Gets a project by its `id`. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| `delete` | `DELETE` | `project_id` | Deletes a project board. Returns a `404 Not Found` status if projects are disabled. |
| `update` | `EXEC` | `project_id` | Updates a project board's information. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |

---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `creator` | `object` | Simple User |
| `number` | `integer` |  |
| `html_url` | `string` |  |
| `created_at` | `string` |  |
| `organization_permission` | `string` | The baseline permission that all organization members have on this project. Only present if owner is an organization. |
| `url` | `string` |  |
| `node_id` | `string` |  |
| `owner_url` | `string` |  |
| `updated_at` | `string` |  |
| `private` | `boolean` | Whether or not this project can be seen by everyone. Only present if owner is an organization. |
| `state` | `string` | State of the project; either 'open' or 'closed' |
| `body` | `string` | Body of the project |
| `columns_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `project_id` | Gets a project by its `id`. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| `list_for_org` | `SELECT` | `org` | Lists the projects in an organization. Returns a `404 Not Found` status if projects are disabled in the organization. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| `list_for_repo` | `SELECT` | `owner, repo` | Lists the projects in a repository. Returns a `404 Not Found` status if projects are disabled in the repository. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| `list_for_user` | `SELECT` | `username` |  |
| `create_for_authenticated_user` | `INSERT` | `data__name` |  |
| `create_for_org` | `INSERT` | `org, data__name` | Creates an organization project board. Returns a `404 Not Found` status if projects are disabled in the organization. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| `create_for_repo` | `INSERT` | `owner, repo, data__name` | Creates a repository project board. Returns a `404 Not Found` status if projects are disabled in the repository. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| `delete` | `DELETE` | `project_id` | Deletes a project board. Returns a `404 Not Found` status if projects are disabled. |
| `update` | `EXEC` | `project_id` | Updates a project board's information. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |

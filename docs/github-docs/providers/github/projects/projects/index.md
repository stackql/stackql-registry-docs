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
| `node_id` | `string` |  |
| `organization_permission` | `string` | The baseline permission that all organization members have on this project. Only present if owner is an organization. |
| `created_at` | `string` |  |
| `owner_url` | `string` |  |
| `html_url` | `string` |  |
| `number` | `integer` |  |
| `state` | `string` | State of the project; either 'open' or 'closed' |
| `private` | `boolean` | Whether or not this project can be seen by everyone. Only present if owner is an organization. |
| `columns_url` | `string` |  |
| `url` | `string` |  |
| `updated_at` | `string` |  |
| `body` | `string` | Body of the project |
| `creator` | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `project_id` | Gets a project by its `id`. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| `list_for_org` | `SELECT` | `org` | Lists the projects in an organization. Returns a `404 Not Found` status if projects are disabled in the organization. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| `list_for_repo` | `SELECT` | `owner, repo` | Lists the projects in a repository. Returns a `404 Not Found` status if projects are disabled in the repository. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| `list_for_user` | `SELECT` | `username` | Lists projects for a user. |
| `create_for_authenticated_user` | `INSERT` | `data__name` | Creates a user project board. Returns a `410 Gone` status if the user does not have existing classic projects. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| `create_for_org` | `INSERT` | `org, data__name` | Creates an organization project board. Returns a `410 Gone` status if projects are disabled in the organization or if the organization does not have existing classic projects. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| `create_for_repo` | `INSERT` | `owner, repo, data__name` | Creates a repository project board. Returns a `410 Gone` status if projects are disabled in the repository or if the repository does not have existing classic projects. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| `delete` | `DELETE` | `project_id` | Deletes a project board. Returns a `404 Not Found` status if projects are disabled. |
| `update` | `EXEC` | `project_id` | Updates a project board's information. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |

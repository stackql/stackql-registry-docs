---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - repos
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
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.projects.repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` | Name of the project |
| `columns_url` | `string` |  |
| `node_id` | `string` |  |
| `number` | `integer` |  |
| `organization_permission` | `string` | The baseline permission that all organization members have on this project. Only present if owner is an organization. |
| `state` | `string` | State of the project; either 'open' or 'closed' |
| `html_url` | `string` |  |
| `created_at` | `string` |  |
| `creator` | `object` | A GitHub user. |
| `body` | `string` | Body of the project |
| `owner_url` | `string` |  |
| `updated_at` | `string` |  |
| `url` | `string` |  |
| `private` | `boolean` | Whether or not this project can be seen by everyone. Only present if owner is an organization. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_for_repo` | `SELECT` | `owner, repo` | Lists the projects in a repository. Returns a `404 Not Found` status if projects are disabled in the repository. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| `create_for_repo` | `INSERT` | `owner, repo, data__name` | Creates a repository project board. Returns a `410 Gone` status if projects are disabled in the repository or if the repository does not have existing classic projects. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |

---
title: orgs
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs
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
<tr><td><b>Name</b></td><td><code>orgs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.projects.orgs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` | Name of the project |
| `updated_at` | `string` |  |
| `columns_url` | `string` |  |
| `body` | `string` | Body of the project |
| `private` | `boolean` | Whether or not this project can be seen by everyone. Only present if owner is an organization. |
| `owner_url` | `string` |  |
| `state` | `string` | State of the project; either 'open' or 'closed' |
| `node_id` | `string` |  |
| `organization_permission` | `string` | The baseline permission that all organization members have on this project. Only present if owner is an organization. |
| `creator` | `object` | A GitHub user. |
| `created_at` | `string` |  |
| `url` | `string` |  |
| `number` | `integer` |  |
| `html_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_for_org` | `SELECT` | `org` | Lists the projects in an organization. Returns a `404 Not Found` status if projects are disabled in the organization. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |
| `create_for_org` | `INSERT` | `org, data__name` | Creates an organization project board. Returns a `410 Gone` status if projects are disabled in the organization or if the organization does not have existing classic projects. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned. |

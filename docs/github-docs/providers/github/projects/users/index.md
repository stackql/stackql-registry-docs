---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.projects.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` | Name of the project |
| `created_at` | `string` |  |
| `creator` | `object` | A GitHub user. |
| `number` | `integer` |  |
| `columns_url` | `string` |  |
| `html_url` | `string` |  |
| `organization_permission` | `string` | The baseline permission that all organization members have on this project. Only present if owner is an organization. |
| `body` | `string` | Body of the project |
| `url` | `string` |  |
| `state` | `string` | State of the project; either 'open' or 'closed' |
| `private` | `boolean` | Whether or not this project can be seen by everyone. Only present if owner is an organization. |
| `node_id` | `string` |  |
| `updated_at` | `string` |  |
| `owner_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_for_user` | `SELECT` | `username` |

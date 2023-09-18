---
title: orgs_for_user
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_for_user
  - orgs
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
<tr><td><b>Name</b></td><td><code>orgs_for_user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.orgs_for_user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `description` | `string` |
| `login` | `string` |
| `node_id` | `string` |
| `issues_url` | `string` |
| `public_members_url` | `string` |
| `repos_url` | `string` |
| `url` | `string` |
| `events_url` | `string` |
| `hooks_url` | `string` |
| `members_url` | `string` |
| `avatar_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_for_authenticated_user` | `SELECT` |  |

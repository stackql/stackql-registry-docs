---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `description` | `string` |
| `repos_url` | `string` |
| `members_url` | `string` |
| `login` | `string` |
| `public_members_url` | `string` |
| `events_url` | `string` |
| `avatar_url` | `string` |
| `hooks_url` | `string` |
| `issues_url` | `string` |
| `node_id` | `string` |
| `url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_for_user` | `SELECT` | `username` |

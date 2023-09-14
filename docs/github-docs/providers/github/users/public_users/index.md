---
title: public_users
hide_title: false
hide_table_of_contents: false
keywords:
  - public_users
  - users
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
<tr><td><b>Name</b></td><td><code>public_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.users.public_users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `url` | `string` |
| `events_url` | `string` |
| `login` | `string` |
| `subscriptions_url` | `string` |
| `gravatar_id` | `string` |
| `starred_at` | `string` |
| `html_url` | `string` |
| `site_admin` | `boolean` |
| `type` | `string` |
| `email` | `string` |
| `followers_url` | `string` |
| `organizations_url` | `string` |
| `node_id` | `string` |
| `following_url` | `string` |
| `avatar_url` | `string` |
| `received_events_url` | `string` |
| `starred_url` | `string` |
| `gists_url` | `string` |
| `repos_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |

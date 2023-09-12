---
title: user_followers
hide_title: false
hide_table_of_contents: false
keywords:
  - user_followers
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
<tr><td><b>Name</b></td><td><code>user_followers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.users.user_followers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `avatar_url` | `string` |
| `events_url` | `string` |
| `subscriptions_url` | `string` |
| `html_url` | `string` |
| `repos_url` | `string` |
| `followers_url` | `string` |
| `url` | `string` |
| `site_admin` | `boolean` |
| `login` | `string` |
| `received_events_url` | `string` |
| `gravatar_id` | `string` |
| `node_id` | `string` |
| `organizations_url` | `string` |
| `starred_url` | `string` |
| `gists_url` | `string` |
| `email` | `string` |
| `following_url` | `string` |
| `starred_at` | `string` |
| `type` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_followers_for_authenticated_user` | `SELECT` |  |

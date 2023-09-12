---
title: following
hide_title: false
hide_table_of_contents: false
keywords:
  - following
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
<tr><td><b>Name</b></td><td><code>following</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.users.following</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `node_id` | `string` |
| `following_url` | `string` |
| `login` | `string` |
| `subscriptions_url` | `string` |
| `gravatar_id` | `string` |
| `avatar_url` | `string` |
| `url` | `string` |
| `followers_url` | `string` |
| `gists_url` | `string` |
| `starred_url` | `string` |
| `received_events_url` | `string` |
| `organizations_url` | `string` |
| `site_admin` | `boolean` |
| `email` | `string` |
| `events_url` | `string` |
| `type` | `string` |
| `repos_url` | `string` |
| `html_url` | `string` |
| `starred_at` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_following_for_user` | `SELECT` | `username` | Lists the people who the specified user follows. |
| `check_following_for_user` | `EXEC` | `target_user, username` |  |

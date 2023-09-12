---
title: followers
hide_title: false
hide_table_of_contents: false
keywords:
  - followers
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
<tr><td><b>Name</b></td><td><code>followers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.users.followers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `email` | `string` |
| `gravatar_id` | `string` |
| `login` | `string` |
| `repos_url` | `string` |
| `received_events_url` | `string` |
| `gists_url` | `string` |
| `node_id` | `string` |
| `subscriptions_url` | `string` |
| `events_url` | `string` |
| `avatar_url` | `string` |
| `type` | `string` |
| `starred_url` | `string` |
| `organizations_url` | `string` |
| `followers_url` | `string` |
| `following_url` | `string` |
| `url` | `string` |
| `site_admin` | `boolean` |
| `starred_at` | `string` |
| `html_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_followers_for_user` | `SELECT` | `username` |

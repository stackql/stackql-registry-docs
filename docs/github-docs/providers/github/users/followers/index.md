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
| `starred_at` | `string` |
| `html_url` | `string` |
| `email` | `string` |
| `gists_url` | `string` |
| `gravatar_id` | `string` |
| `url` | `string` |
| `received_events_url` | `string` |
| `avatar_url` | `string` |
| `node_id` | `string` |
| `starred_url` | `string` |
| `followers_url` | `string` |
| `events_url` | `string` |
| `site_admin` | `boolean` |
| `repos_url` | `string` |
| `subscriptions_url` | `string` |
| `login` | `string` |
| `type` | `string` |
| `organizations_url` | `string` |
| `following_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_followers_for_authenticated_user` | `SELECT` |  | Lists the people following the authenticated user. |
| `list_followers_for_user` | `SELECT` | `username` | Lists the people following the specified user. |

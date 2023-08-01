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
| `login` | `string` |
| `received_events_url` | `string` |
| `avatar_url` | `string` |
| `starred_at` | `string` |
| `type` | `string` |
| `site_admin` | `boolean` |
| `node_id` | `string` |
| `organizations_url` | `string` |
| `followers_url` | `string` |
| `gravatar_id` | `string` |
| `email` | `string` |
| `events_url` | `string` |
| `following_url` | `string` |
| `subscriptions_url` | `string` |
| `url` | `string` |
| `repos_url` | `string` |
| `gists_url` | `string` |
| `html_url` | `string` |
| `starred_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_followers_for_authenticated_user` | `SELECT` |  | Lists the people following the authenticated user. |
| `list_followers_for_user` | `SELECT` | `username` | Lists the people following the specified user. |

---
title: followers
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `organizations_url` | `string` |
| `html_url` | `string` |
| `gravatar_id` | `string` |
| `type` | `string` |
| `node_id` | `string` |
| `avatar_url` | `string` |
| `received_events_url` | `string` |
| `followers_url` | `string` |
| `gists_url` | `string` |
| `following_url` | `string` |
| `repos_url` | `string` |
| `email` | `string` |
| `url` | `string` |
| `site_admin` | `boolean` |
| `events_url` | `string` |
| `starred_url` | `string` |
| `starred_at` | `string` |
| `login` | `string` |
| `subscriptions_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_followers_for_authenticated_user` | `SELECT` |  | Lists the people following the authenticated user. |
| `list_followers_for_user` | `SELECT` | `username` | Lists the people following the specified user. |

---
title: users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.search.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `public_gists` | `integer` |
| `bio` | `string` |
| `created_at` | `string` |
| `company` | `string` |
| `blog` | `string` |
| `avatar_url` | `string` |
| `html_url` | `string` |
| `subscriptions_url` | `string` |
| `text_matches` | `array` |
| `location` | `string` |
| `public_repos` | `integer` |
| `received_events_url` | `string` |
| `email` | `string` |
| `following_url` | `string` |
| `followers` | `integer` |
| `gravatar_id` | `string` |
| `following` | `integer` |
| `organizations_url` | `string` |
| `gists_url` | `string` |
| `hireable` | `boolean` |
| `type` | `string` |
| `score` | `number` |
| `node_id` | `string` |
| `repos_url` | `string` |
| `login` | `string` |
| `suspended_at` | `string` |
| `site_admin` | `boolean` |
| `url` | `string` |
| `followers_url` | `string` |
| `updated_at` | `string` |
| `starred_url` | `string` |
| `events_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `users` | `SELECT` | `q` |

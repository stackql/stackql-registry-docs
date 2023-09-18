---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - search
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
<tr><td><b>Id</b></td><td><code>github.search.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `repos_url` | `string` |
| `created_at` | `string` |
| `company` | `string` |
| `text_matches` | `array` |
| `hireable` | `boolean` |
| `site_admin` | `boolean` |
| `avatar_url` | `string` |
| `updated_at` | `string` |
| `bio` | `string` |
| `location` | `string` |
| `followers_url` | `string` |
| `followers` | `integer` |
| `organizations_url` | `string` |
| `blog` | `string` |
| `gravatar_id` | `string` |
| `public_gists` | `integer` |
| `email` | `string` |
| `score` | `number` |
| `following_url` | `string` |
| `starred_url` | `string` |
| `login` | `string` |
| `node_id` | `string` |
| `subscriptions_url` | `string` |
| `events_url` | `string` |
| `received_events_url` | `string` |
| `type` | `string` |
| `html_url` | `string` |
| `public_repos` | `integer` |
| `following` | `integer` |
| `url` | `string` |
| `gists_url` | `string` |
| `suspended_at` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `users` | `SELECT` | `q` |

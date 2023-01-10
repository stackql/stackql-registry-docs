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
| `starred_url` | `string` |
| `html_url` | `string` |
| `hireable` | `boolean` |
| `blog` | `string` |
| `public_repos` | `integer` |
| `login` | `string` |
| `bio` | `string` |
| `updated_at` | `string` |
| `node_id` | `string` |
| `followers_url` | `string` |
| `created_at` | `string` |
| `email` | `string` |
| `location` | `string` |
| `repos_url` | `string` |
| `events_url` | `string` |
| `following_url` | `string` |
| `url` | `string` |
| `score` | `number` |
| `avatar_url` | `string` |
| `received_events_url` | `string` |
| `gravatar_id` | `string` |
| `subscriptions_url` | `string` |
| `organizations_url` | `string` |
| `site_admin` | `boolean` |
| `followers` | `integer` |
| `suspended_at` | `string` |
| `company` | `string` |
| `gists_url` | `string` |
| `public_gists` | `integer` |
| `following` | `integer` |
| `type` | `string` |
| `text_matches` | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `users` | `SELECT` | `q` |

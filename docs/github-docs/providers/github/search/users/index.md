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
| `company` | `string` |
| `login` | `string` |
| `organizations_url` | `string` |
| `followers` | `integer` |
| `subscriptions_url` | `string` |
| `location` | `string` |
| `node_id` | `string` |
| `html_url` | `string` |
| `site_admin` | `boolean` |
| `type` | `string` |
| `suspended_at` | `string` |
| `blog` | `string` |
| `avatar_url` | `string` |
| `gists_url` | `string` |
| `repos_url` | `string` |
| `hireable` | `boolean` |
| `score` | `number` |
| `followers_url` | `string` |
| `bio` | `string` |
| `following_url` | `string` |
| `email` | `string` |
| `url` | `string` |
| `public_gists` | `integer` |
| `starred_url` | `string` |
| `gravatar_id` | `string` |
| `following` | `integer` |
| `events_url` | `string` |
| `public_repos` | `integer` |
| `updated_at` | `string` |
| `text_matches` | `array` |
| `created_at` | `string` |
| `received_events_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `users` | `SELECT` | `q` |

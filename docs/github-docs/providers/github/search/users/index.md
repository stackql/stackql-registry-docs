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
| `public_repos` | `integer` |
| `updated_at` | `string` |
| `text_matches` | `array` |
| `blog` | `string` |
| `subscriptions_url` | `string` |
| `following` | `integer` |
| `created_at` | `string` |
| `repos_url` | `string` |
| `type` | `string` |
| `received_events_url` | `string` |
| `node_id` | `string` |
| `html_url` | `string` |
| `company` | `string` |
| `followers` | `integer` |
| `followers_url` | `string` |
| `suspended_at` | `string` |
| `organizations_url` | `string` |
| `score` | `number` |
| `email` | `string` |
| `location` | `string` |
| `bio` | `string` |
| `url` | `string` |
| `public_gists` | `integer` |
| `avatar_url` | `string` |
| `site_admin` | `boolean` |
| `following_url` | `string` |
| `starred_url` | `string` |
| `hireable` | `boolean` |
| `gravatar_id` | `string` |
| `gists_url` | `string` |
| `login` | `string` |
| `events_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `users` | `SELECT` | `q` |

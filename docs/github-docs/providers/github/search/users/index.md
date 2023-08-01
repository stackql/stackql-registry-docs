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
| `blog` | `string` |
| `public_repos` | `integer` |
| `site_admin` | `boolean` |
| `company` | `string` |
| `hireable` | `boolean` |
| `gravatar_id` | `string` |
| `bio` | `string` |
| `location` | `string` |
| `followers` | `integer` |
| `score` | `number` |
| `repos_url` | `string` |
| `created_at` | `string` |
| `following_url` | `string` |
| `gists_url` | `string` |
| `updated_at` | `string` |
| `url` | `string` |
| `suspended_at` | `string` |
| `node_id` | `string` |
| `following` | `integer` |
| `email` | `string` |
| `organizations_url` | `string` |
| `html_url` | `string` |
| `received_events_url` | `string` |
| `public_gists` | `integer` |
| `events_url` | `string` |
| `subscriptions_url` | `string` |
| `text_matches` | `array` |
| `type` | `string` |
| `login` | `string` |
| `followers_url` | `string` |
| `starred_url` | `string` |
| `avatar_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `users` | `SELECT` | `q` |

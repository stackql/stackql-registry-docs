---
title: repos_stargazers
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_stargazers
  - activity
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
<tr><td><b>Name</b></td><td><code>repos_stargazers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.repos_stargazers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `repos_url` | `string` |
| `url` | `string` |
| `received_events_url` | `string` |
| `gists_url` | `string` |
| `html_url` | `string` |
| `starred_url` | `string` |
| `gravatar_id` | `string` |
| `type` | `string` |
| `organizations_url` | `string` |
| `subscriptions_url` | `string` |
| `starred_at` | `string` |
| `site_admin` | `boolean` |
| `email` | `string` |
| `node_id` | `string` |
| `events_url` | `string` |
| `following_url` | `string` |
| `login` | `string` |
| `followers_url` | `string` |
| `avatar_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_stargazers_for_repo` | `SELECT` | `owner, repo` |

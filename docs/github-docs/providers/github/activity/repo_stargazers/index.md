---
title: repo_stargazers
hide_title: false
hide_table_of_contents: false
keywords:
  - repo_stargazers
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
<tr><td><b>Name</b></td><td><code>repo_stargazers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.repo_stargazers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `login` | `string` |
| `subscriptions_url` | `string` |
| `type` | `string` |
| `email` | `string` |
| `site_admin` | `boolean` |
| `gravatar_id` | `string` |
| `organizations_url` | `string` |
| `url` | `string` |
| `avatar_url` | `string` |
| `followers_url` | `string` |
| `starred_url` | `string` |
| `received_events_url` | `string` |
| `gists_url` | `string` |
| `node_id` | `string` |
| `repos_url` | `string` |
| `starred_at` | `string` |
| `following_url` | `string` |
| `html_url` | `string` |
| `events_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_stargazers_for_repo` | `SELECT` | `owner, repo` |

---
title: repo_watchers
hide_title: false
hide_table_of_contents: false
keywords:
  - repo_watchers
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
<tr><td><b>Name</b></td><td><code>repo_watchers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.repo_watchers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `login` | `string` |
| `following_url` | `string` |
| `followers_url` | `string` |
| `events_url` | `string` |
| `gravatar_id` | `string` |
| `organizations_url` | `string` |
| `repos_url` | `string` |
| `node_id` | `string` |
| `starred_url` | `string` |
| `subscriptions_url` | `string` |
| `avatar_url` | `string` |
| `html_url` | `string` |
| `email` | `string` |
| `url` | `string` |
| `starred_at` | `string` |
| `type` | `string` |
| `gists_url` | `string` |
| `received_events_url` | `string` |
| `site_admin` | `boolean` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_watchers_for_repo` | `SELECT` | `owner, repo` |

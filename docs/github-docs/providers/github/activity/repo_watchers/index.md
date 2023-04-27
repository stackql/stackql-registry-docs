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
| `repos_url` | `string` |
| `received_events_url` | `string` |
| `following_url` | `string` |
| `login` | `string` |
| `events_url` | `string` |
| `subscriptions_url` | `string` |
| `site_admin` | `boolean` |
| `avatar_url` | `string` |
| `type` | `string` |
| `starred_url` | `string` |
| `email` | `string` |
| `starred_at` | `string` |
| `followers_url` | `string` |
| `gists_url` | `string` |
| `url` | `string` |
| `gravatar_id` | `string` |
| `organizations_url` | `string` |
| `node_id` | `string` |
| `html_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_watchers_for_repo` | `SELECT` | `owner, repo` |

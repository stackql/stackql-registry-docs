---
title: repos_subscribers
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_subscribers
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
<tr><td><b>Name</b></td><td><code>repos_subscribers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.repos_subscribers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `avatar_url` | `string` |
| `type` | `string` |
| `html_url` | `string` |
| `gists_url` | `string` |
| `repos_url` | `string` |
| `organizations_url` | `string` |
| `received_events_url` | `string` |
| `followers_url` | `string` |
| `login` | `string` |
| `starred_url` | `string` |
| `events_url` | `string` |
| `url` | `string` |
| `site_admin` | `boolean` |
| `gravatar_id` | `string` |
| `following_url` | `string` |
| `node_id` | `string` |
| `subscriptions_url` | `string` |
| `email` | `string` |
| `starred_at` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_watchers_for_repo` | `SELECT` | `owner, repo` |

---
title: blocking
hide_title: false
hide_table_of_contents: false
keywords:
  - blocking
  - users
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
<tr><td><b>Name</b></td><td><code>blocking</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.users.blocking</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `repos_url` | `string` |
| `following_url` | `string` |
| `starred_at` | `string` |
| `followers_url` | `string` |
| `organizations_url` | `string` |
| `gravatar_id` | `string` |
| `html_url` | `string` |
| `email` | `string` |
| `avatar_url` | `string` |
| `login` | `string` |
| `node_id` | `string` |
| `subscriptions_url` | `string` |
| `events_url` | `string` |
| `type` | `string` |
| `gists_url` | `string` |
| `received_events_url` | `string` |
| `site_admin` | `boolean` |
| `url` | `string` |
| `starred_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_blocked_by_authenticated_user` | `SELECT` |  | List the users you've blocked on your personal account. |
| `block` | `EXEC` | `username` |  |
| `check_blocked` | `EXEC` | `username` |  |
| `unblock` | `EXEC` | `username` |  |

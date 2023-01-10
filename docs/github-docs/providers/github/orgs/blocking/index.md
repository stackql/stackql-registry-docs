---
title: blocking
hide_title: false
hide_table_of_contents: false
keywords:
  - blocking
  - orgs
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
<tr><td><b>Id</b></td><td><code>github.orgs.blocking</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `node_id` | `string` |
| `url` | `string` |
| `events_url` | `string` |
| `subscriptions_url` | `string` |
| `starred_url` | `string` |
| `repos_url` | `string` |
| `followers_url` | `string` |
| `email` | `string` |
| `organizations_url` | `string` |
| `starred_at` | `string` |
| `received_events_url` | `string` |
| `type` | `string` |
| `login` | `string` |
| `avatar_url` | `string` |
| `gists_url` | `string` |
| `gravatar_id` | `string` |
| `site_admin` | `boolean` |
| `html_url` | `string` |
| `following_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_blocked_users` | `SELECT` | `org` | List the users blocked by an organization. |
| `block_user` | `EXEC` | `org, username` |  |
| `check_blocked_user` | `EXEC` | `org, username` |  |
| `unblock_user` | `EXEC` | `org, username` |  |

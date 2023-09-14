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
| `received_events_url` | `string` |
| `subscriptions_url` | `string` |
| `following_url` | `string` |
| `login` | `string` |
| `starred_url` | `string` |
| `events_url` | `string` |
| `repos_url` | `string` |
| `url` | `string` |
| `gravatar_id` | `string` |
| `email` | `string` |
| `followers_url` | `string` |
| `gists_url` | `string` |
| `site_admin` | `boolean` |
| `organizations_url` | `string` |
| `node_id` | `string` |
| `starred_at` | `string` |
| `avatar_url` | `string` |
| `type` | `string` |
| `html_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_blocked_by_authenticated_user` | `SELECT` |  | List the users you've blocked on your personal account. |
| `block` | `EXEC` | `username` | Blocks the given user and returns a 204. If the authenticated user cannot block the given user a 422 is returned. |
| `check_blocked` | `EXEC` | `username` | Returns a 204 if the given user is blocked by the authenticated user. Returns a 404 if the given user is not blocked by the authenticated user, or if the given user account has been identified as spam by GitHub. |
| `unblock` | `EXEC` | `username` | Unblocks the given user and returns a 204. |

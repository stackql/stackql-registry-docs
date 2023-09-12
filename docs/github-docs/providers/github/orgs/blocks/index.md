---
title: blocks
hide_title: false
hide_table_of_contents: false
keywords:
  - blocks
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
<tr><td><b>Name</b></td><td><code>blocks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.blocks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `gists_url` | `string` |
| `events_url` | `string` |
| `subscriptions_url` | `string` |
| `html_url` | `string` |
| `url` | `string` |
| `avatar_url` | `string` |
| `starred_url` | `string` |
| `node_id` | `string` |
| `email` | `string` |
| `site_admin` | `boolean` |
| `starred_at` | `string` |
| `type` | `string` |
| `received_events_url` | `string` |
| `login` | `string` |
| `gravatar_id` | `string` |
| `organizations_url` | `string` |
| `following_url` | `string` |
| `followers_url` | `string` |
| `repos_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_blocked_users` | `SELECT` | `org` | List the users blocked by an organization. |
| `block_user` | `EXEC` | `org, username` | Blocks the given user on behalf of the specified organization and returns a 204. If the organization cannot block the given user a 422 is returned. |
| `check_blocked_user` | `EXEC` | `org, username` | Returns a 204 if the given user is blocked by the given organization. Returns a 404 if the organization is not blocking the user, or if the user account has been identified as spam by GitHub. |
| `unblock_user` | `EXEC` | `org, username` | Unblocks the given user on behalf of the specified organization. |

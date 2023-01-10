---
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
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
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `gists_url` | `string` |
| `avatar_url` | `string` |
| `events_url` | `string` |
| `html_url` | `string` |
| `followers_url` | `string` |
| `gravatar_id` | `string` |
| `following_url` | `string` |
| `starred_url` | `string` |
| `login` | `string` |
| `site_admin` | `boolean` |
| `received_events_url` | `string` |
| `type` | `string` |
| `node_id` | `string` |
| `url` | `string` |
| `organizations_url` | `string` |
| `subscriptions_url` | `string` |
| `email` | `string` |
| `starred_at` | `string` |
| `repos_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_members` | `SELECT` | `org` | List all users who are members of an organization. If the authenticated user is also a member of this organization then both concealed and public members will be returned. |
| `remove_member` | `DELETE` | `org, username` | Removing a user from this list will remove them from all teams and they will no longer have any access to the organization's repositories. |

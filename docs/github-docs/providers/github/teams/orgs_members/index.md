---
title: orgs_members
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_members
  - teams
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
<tr><td><b>Name</b></td><td><code>orgs_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.teams.orgs_members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `following_url` | `string` |
| `html_url` | `string` |
| `gists_url` | `string` |
| `email` | `string` |
| `followers_url` | `string` |
| `avatar_url` | `string` |
| `organizations_url` | `string` |
| `type` | `string` |
| `subscriptions_url` | `string` |
| `starred_at` | `string` |
| `repos_url` | `string` |
| `gravatar_id` | `string` |
| `starred_url` | `string` |
| `received_events_url` | `string` |
| `site_admin` | `boolean` |
| `node_id` | `string` |
| `events_url` | `string` |
| `url` | `string` |
| `login` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_members_in_org` | `SELECT` | `org, team_slug` |

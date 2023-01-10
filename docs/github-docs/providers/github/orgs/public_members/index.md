---
title: public_members
hide_title: false
hide_table_of_contents: false
keywords:
  - public_members
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
<tr><td><b>Name</b></td><td><code>public_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.public_members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `node_id` | `string` |
| `gravatar_id` | `string` |
| `url` | `string` |
| `received_events_url` | `string` |
| `followers_url` | `string` |
| `following_url` | `string` |
| `email` | `string` |
| `login` | `string` |
| `avatar_url` | `string` |
| `type` | `string` |
| `starred_url` | `string` |
| `organizations_url` | `string` |
| `subscriptions_url` | `string` |
| `html_url` | `string` |
| `starred_at` | `string` |
| `site_admin` | `boolean` |
| `gists_url` | `string` |
| `repos_url` | `string` |
| `events_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public_members` | `SELECT` | `org` |

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
| `organizations_url` | `string` |
| `login` | `string` |
| `avatar_url` | `string` |
| `gravatar_id` | `string` |
| `repos_url` | `string` |
| `starred_at` | `string` |
| `subscriptions_url` | `string` |
| `received_events_url` | `string` |
| `url` | `string` |
| `following_url` | `string` |
| `node_id` | `string` |
| `html_url` | `string` |
| `starred_url` | `string` |
| `events_url` | `string` |
| `gists_url` | `string` |
| `email` | `string` |
| `site_admin` | `boolean` |
| `type` | `string` |
| `followers_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public_members` | `SELECT` | `org` |

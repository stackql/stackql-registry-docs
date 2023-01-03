---
title: public_members
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `events_url` | `string` |
| `node_id` | `string` |
| `email` | `string` |
| `gravatar_id` | `string` |
| `subscriptions_url` | `string` |
| `login` | `string` |
| `received_events_url` | `string` |
| `site_admin` | `boolean` |
| `url` | `string` |
| `following_url` | `string` |
| `starred_url` | `string` |
| `html_url` | `string` |
| `starred_at` | `string` |
| `gists_url` | `string` |
| `type` | `string` |
| `avatar_url` | `string` |
| `repos_url` | `string` |
| `followers_url` | `string` |
| `organizations_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_public_members` | `SELECT` | `org` |

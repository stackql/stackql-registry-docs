---
title: contributors
hide_title: false
hide_table_of_contents: false
keywords:
  - contributors
  - repos
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
<tr><td><b>Name</b></td><td><code>contributors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.contributors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `repos_url` | `string` |
| `url` | `string` |
| `contributions` | `integer` |
| `node_id` | `string` |
| `site_admin` | `boolean` |
| `gists_url` | `string` |
| `subscriptions_url` | `string` |
| `followers_url` | `string` |
| `starred_url` | `string` |
| `html_url` | `string` |
| `login` | `string` |
| `events_url` | `string` |
| `email` | `string` |
| `organizations_url` | `string` |
| `received_events_url` | `string` |
| `following_url` | `string` |
| `gravatar_id` | `string` |
| `avatar_url` | `string` |
| `type` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_contributors` | `SELECT` | `owner, repo` |

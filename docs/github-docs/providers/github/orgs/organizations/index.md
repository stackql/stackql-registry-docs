---
title: organizations
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations
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
<tr><td><b>Name</b></td><td><code>organizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.organizations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `description` | `string` |
| `hooks_url` | `string` |
| `url` | `string` |
| `avatar_url` | `string` |
| `node_id` | `string` |
| `repos_url` | `string` |
| `login` | `string` |
| `issues_url` | `string` |
| `events_url` | `string` |
| `public_members_url` | `string` |
| `members_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |

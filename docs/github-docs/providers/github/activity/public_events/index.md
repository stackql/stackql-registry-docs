---
title: public_events
hide_title: false
hide_table_of_contents: false
keywords:
  - public_events
  - activity
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
<tr><td><b>Name</b></td><td><code>public_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.public_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `public` | `boolean` |  |
| `repo` | `object` |  |
| `type` | `string` |  |
| `actor` | `object` | Actor |
| `created_at` | `string` |  |
| `org` | `object` | Actor |
| `payload` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_public_events` | `SELECT` |  | We delay the public events feed by five minutes, which means the most recent event returned by the public events API actually occurred at least five minutes ago. |
| `list_public_events_for_repo_network` | `SELECT` | `owner, repo` |  |
| `list_public_events_for_user` | `SELECT` | `username` |  |
| `list_public_org_events` | `SELECT` | `org` |  |

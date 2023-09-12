---
title: users_received_events_public
hide_title: false
hide_table_of_contents: false
keywords:
  - users_received_events_public
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
<tr><td><b>Name</b></td><td><code>users_received_events_public</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.users_received_events_public</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `org` | `object` | Actor |
| `payload` | `object` |  |
| `public` | `boolean` |  |
| `repo` | `object` |  |
| `type` | `string` |  |
| `actor` | `object` | Actor |
| `created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_received_public_events_for_user` | `SELECT` | `username` |

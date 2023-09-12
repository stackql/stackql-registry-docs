---
title: users_events_orgs
hide_title: false
hide_table_of_contents: false
keywords:
  - users_events_orgs
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
<tr><td><b>Name</b></td><td><code>users_events_orgs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.users_events_orgs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `actor` | `object` | Actor |
| `created_at` | `string` |  |
| `org` | `object` | Actor |
| `payload` | `object` |  |
| `public` | `boolean` |  |
| `repo` | `object` |  |
| `type` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_org_events_for_authenticated_user` | `SELECT` | `org, username` |

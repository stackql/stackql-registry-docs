---
title: user_memberships
hide_title: false
hide_table_of_contents: false
keywords:
  - user_memberships
  - teams
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.teams.user_memberships</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of a user's relationship with a team |
| `attributes` | `object` | Team membership attributes |
| `relationships` | `object` | Relationship between membership and a user |
| `type` | `string` | Team membership type |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_user_memberships` | `SELECT` | `user_uuid, dd_site` |
| `_get_user_memberships` | `EXEC` | `user_uuid, dd_site` |

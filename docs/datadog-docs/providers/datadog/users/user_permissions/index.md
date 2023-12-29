---
title: user_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - user_permissions
  - users
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
<tr><td><b>Name</b></td><td><code>user_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.users.user_permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the permission. |
| `attributes` | `object` | Attributes of a permission. |
| `type` | `string` | Permissions resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_user_permissions` | `SELECT` | `user_id, dd_site` |
| `_list_user_permissions` | `EXEC` | `user_id, dd_site` |

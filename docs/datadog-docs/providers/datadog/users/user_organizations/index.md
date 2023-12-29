---
title: user_organizations
hide_title: false
hide_table_of_contents: false
keywords:
  - user_organizations
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
<tr><td><b>Name</b></td><td><code>user_organizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.users.user_organizations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the user. |
| `attributes` | `object` | Attributes of user object returned by the API. |
| `relationships` | `object` | Relationships of the user object returned by the API. |
| `type` | `string` | Users resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_user_organizations` | `SELECT` | `user_id, dd_site` |
| `_list_user_organizations` | `EXEC` | `user_id, dd_site` |

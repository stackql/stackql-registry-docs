---
title: user_role_permission_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - user_role_permission_groups
  - dfareporting
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_role_permission_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.user_role_permission_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this user role permission. |
| `name` | `string` | Name of this user role permission group. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#userRolePermissionGroup". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `userRolePermissionGroups_get` | `SELECT` | `id, profileId` | Gets one user role permission group by ID. |
| `userRolePermissionGroups_list` | `SELECT` | `profileId` | Gets a list of all supported user role permission groups. |

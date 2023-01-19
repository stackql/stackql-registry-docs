---
title: user_role_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - user_role_permissions
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
<tr><td><b>Name</b></td><td><code>user_role_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.user_role_permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this user role permission. |
| `name` | `string` | Name of this user role permission. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#userRolePermission". |
| `permissionGroupId` | `string` | ID of the permission group that this user role permission belongs to. |
| `availability` | `string` | Levels of availability for a user role permission. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `userRolePermissions_get` | `SELECT` | `id, profileId` | Gets one user role permission by ID. |
| `userRolePermissions_list` | `SELECT` | `profileId` | Gets a list of user role permissions, possibly filtered. |

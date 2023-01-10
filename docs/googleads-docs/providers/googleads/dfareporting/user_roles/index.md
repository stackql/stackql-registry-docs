---
title: user_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - user_roles
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
<tr><td><b>Name</b></td><td><code>user_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.user_roles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this user role. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this user role. This is a required field. Must be less than 256 characters long. If this user role is under a subaccount, the name must be unique among sites of the same subaccount. Otherwise, this user role is a top-level user role, and the name must be unique among top-level user roles of the same account. |
| `parentUserRoleId` | `string` | ID of the user role that this user role is based on or copied from. This is a required field. |
| `permissions` | `array` | List of permissions associated with this user role. |
| `subaccountId` | `string` | Subaccount ID of this user role. This is a read-only field that can be left blank. |
| `accountId` | `string` | Account ID of this user role. This is a read-only field that can be left blank. |
| `defaultUserRole` | `boolean` | Whether this is a default user role. Default user roles are created by the system for the account/subaccount and cannot be modified or deleted. Each default user role comes with a basic set of preassigned permissions. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#userRole". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `userRoles_get` | `SELECT` | `id, profileId` | Gets one user role by ID. |
| `userRoles_list` | `SELECT` | `profileId` | Retrieves a list of user roles, possibly filtered. This method supports paging. |
| `userRoles_delete` | `DELETE` | `id, profileId` | Deletes an existing user role. |
| `userRoles_insert` | `EXEC` | `profileId` | Inserts a new user role. |
| `userRoles_patch` | `EXEC` | `id, profileId` | Updates an existing user role. This method supports patch semantics. |
| `userRoles_update` | `EXEC` | `profileId` | Updates an existing user role. |

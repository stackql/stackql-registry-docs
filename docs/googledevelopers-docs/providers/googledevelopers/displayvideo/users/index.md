---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - displayvideo
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.displayvideo.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the user. |
| `userId` | `string` | Output only. The unique ID of the user. Assigned by the system. |
| `assignedUserRoles` | `array` | The assigned user roles. Required in CreateUser. Output only in UpdateUser. Can only be updated through BulkEditAssignedUserRoles. |
| `displayName` | `string` | Required. The display name of the user. Must be UTF-8 encoded with a maximum size of 240 bytes. |
| `email` | `string` | Required. Immutable. The email address used to identify the user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `usersId` | Gets a user. |
| `list` | `SELECT` |  | Lists users that are accessible to the current user. If two users have user roles on the same partner or advertiser, they can access each other. |
| `create` | `INSERT` |  | Creates a new user. Returns the newly created user if successful. |
| `delete` | `DELETE` | `usersId` | Deletes a user. |
| `bulkEditAssignedUserRoles` | `EXEC` | `usersId` | Bulk edits user roles for a user. The operation will delete the assigned user roles provided in BulkEditAssignedUserRolesRequest.deletedAssignedUserRoles and then assign the user roles provided in BulkEditAssignedUserRolesRequest.createdAssignedUserRoles. |
| `patch` | `EXEC` | `usersId` | Updates an existing user. Returns the updated user if successful. |

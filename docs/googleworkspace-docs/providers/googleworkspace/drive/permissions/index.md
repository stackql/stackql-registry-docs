---
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions
  - drive
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.drive.permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of this permission. This is a unique identifier for the grantee, and is published in User resources as permissionId. IDs should be treated as opaque values. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#permission". |
| `teamDrivePermissionDetails` | `array` | Deprecated - use permissionDetails instead. |
| `type` | `string` | The type of the grantee. Valid values are:  <br />- user <br />- group <br />- domain <br />- anyone  When creating a permission, if type is user or group, you must provide an emailAddress for the user or group. When type is domain, you must provide a domain. There isn't extra information required for a anyone type. |
| `deleted` | `boolean` | Whether the account associated with this permission has been deleted. This field only pertains to user and group permissions. |
| `permissionDetails` | `array` | Details of whether the permissions on this shared drive item are inherited or directly on this item. This is an output-only field which is present only for shared drive items. |
| `role` | `string` | The role granted by this permission. While new values may be supported in the future, the following are currently allowed:  <br />- owner <br />- organizer <br />- fileOrganizer <br />- writer <br />- commenter <br />- reader |
| `expirationTime` | `string` | The time at which this permission will expire (RFC 3339 date-time). Expiration times have the following restrictions:  <br />- They cannot be set on shared drive items <br />- They can only be set on user and group permissions <br />- The time must be in the future <br />- The time cannot be more than a year in the future |
| `pendingOwner` | `boolean` | Whether the account associated with this permission is a pending owner. Only populated for user type permissions for files that are not in a shared drive. |
| `emailAddress` | `string` | The email address of the user or group to which this permission refers. |
| `displayName` | `string` | The "pretty" name of the value of the permission. The following is a list of examples for each type of permission:  <br />- user - User's full name, as defined for their Google account, such as "Joe Smith." <br />- group - Name of the Google Group, such as "The Company Administrators." <br />- domain - String domain name, such as "thecompany.com." <br />- anyone - No displayName is present. |
| `domain` | `string` | The domain to which this permission refers. |
| `view` | `string` | Indicates the view for this permission. Only populated for permissions that belong to a view. published is the only supported value. |
| `allowFileDiscovery` | `boolean` | Whether the permission allows the file to be discovered through search. This is only applicable for permissions of type domain or anyone. |
| `photoLink` | `string` | A link to the user's profile photo, if available. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `fileId, permissionId` | Gets a permission by ID. |
| `list` | `SELECT` | `fileId` | Lists a file's or shared drive's permissions. |
| `create` | `INSERT` | `fileId` | Creates a permission for a file or shared drive. |
| `delete` | `DELETE` | `fileId, permissionId` | Deletes a permission. |
| `update` | `EXEC` | `fileId, permissionId` | Updates a permission with patch semantics. |

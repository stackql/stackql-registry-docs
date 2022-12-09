---
title: network_interface_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interface_permissions
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_interface_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.network_interface_permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `permissionState` | `object` | Describes the state of a network interface permission. |
| `awsAccountId` | `string` | The Amazon Web Services account ID. |
| `awsService` | `string` | The Amazon Web Service. |
| `networkInterfaceId` | `string` | The ID of the network interface. |
| `networkInterfacePermissionId` | `string` | The ID of the network interface permission. |
| `permission` | `string` | The type of permission. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `network_interface_permissions_Describe` | `SELECT` |  | Describes the permissions for your network interfaces.  |
| `network_interface_permission_Create` | `INSERT` | `NetworkInterfaceId, Permission` | &lt;p&gt;Grants an Amazon Web Services-authorized account permission to attach the specified network interface to an instance in their account.&lt;/p&gt; &lt;p&gt;You can grant permission to a single Amazon Web Services account only, and only one account at a time.&lt;/p&gt; |
| `network_interface_permission_Delete` | `DELETE` | `NetworkInterfacePermissionId` | Deletes a permission for a network interface. By default, you cannot delete the permission if the account for which you're removing the permission has attached the network interface to an instance. However, you can force delete the permission, regardless of any attachment. |

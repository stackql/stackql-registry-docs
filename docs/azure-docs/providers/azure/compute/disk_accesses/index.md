---
title: disk_accesses
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_accesses
  - compute
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disk_accesses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.disk_accesses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `type` | `string` | Resource type |
| `extendedLocation` | `object` | The complex type of the extended location. |
| `location` | `string` | Resource location |
| `properties` | `object` |  |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DiskAccesses_Get` | `SELECT` | `diskAccessName, resourceGroupName, subscriptionId` | Gets information about a disk access resource. |
| `DiskAccesses_List` | `SELECT` | `subscriptionId` | Lists all the disk access resources under a subscription. |
| `DiskAccesses_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the disk access resources under a resource group. |
| `DiskAccesses_CreateOrUpdate` | `INSERT` | `diskAccessName, resourceGroupName, subscriptionId` | Creates or updates a disk access resource |
| `DiskAccesses_Delete` | `DELETE` | `diskAccessName, resourceGroupName, subscriptionId` | Deletes a disk access resource. |
| `DiskAccesses_DeleteAPrivateEndpointConnection` | `EXEC` | `diskAccessName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Deletes a private endpoint connection under a disk access resource. |
| `DiskAccesses_GetAPrivateEndpointConnection` | `EXEC` | `diskAccessName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets information about a private endpoint connection under a disk access resource. |
| `DiskAccesses_GetPrivateLinkResources` | `EXEC` | `diskAccessName, resourceGroupName, subscriptionId` | Gets the private link resources possible under disk access resource |
| `DiskAccesses_ListPrivateEndpointConnections` | `EXEC` | `diskAccessName, resourceGroupName, subscriptionId` | List information about private endpoint connections under a disk access resource |
| `DiskAccesses_Update` | `EXEC` | `diskAccessName, resourceGroupName, subscriptionId` | Updates (patches) a disk access resource. |
| `DiskAccesses_UpdateAPrivateEndpointConnection` | `EXEC` | `diskAccessName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Approve or reject a private endpoint connection under disk access resource, this can't be used to create a new private endpoint connection. |

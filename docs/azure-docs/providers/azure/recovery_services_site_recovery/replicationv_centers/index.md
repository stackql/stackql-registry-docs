---
title: replicationv_centers
hide_title: false
hide_table_of_contents: false
keywords:
  - replicationv_centers
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>replicationv_centers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replicationv_centers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `properties` | `object` | vCenter properties. |
| `type` | `string` | Resource Type |
| `location` | `string` | Resource Location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReplicationvCenters_Get` | `SELECT` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId, vcenterName` | Gets the details of a registered vCenter server(Add vCenter server). |
| `ReplicationvCenters_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the vCenter servers registered in the vault. |
| `ReplicationvCenters_ListByReplicationFabrics` | `SELECT` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | Lists the vCenter servers registered in a fabric. |
| `ReplicationvCenters_Create` | `INSERT` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId, vcenterName` | The operation to create a vCenter object.. |
| `ReplicationvCenters_Delete` | `DELETE` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId, vcenterName` | The operation to remove(unregister) a registered vCenter server from the vault. |
| `ReplicationvCenters_Update` | `EXEC` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId, vcenterName` | The operation to update a registered vCenter. |

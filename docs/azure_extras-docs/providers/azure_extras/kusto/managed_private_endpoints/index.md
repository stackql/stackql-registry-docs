---
title: managed_private_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_private_endpoints
  - kusto
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>managed_private_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.kusto.managed_private_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | A class representing the properties of a managed private endpoint object. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedPrivateEndpoints_Get` | `SELECT` | `clusterName, managedPrivateEndpointName, resourceGroupName, subscriptionId` | Gets a managed private endpoint. |
| `ManagedPrivateEndpoints_List` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Returns the list of managed private endpoints. |
| `ManagedPrivateEndpoints_CreateOrUpdate` | `INSERT` | `clusterName, managedPrivateEndpointName, resourceGroupName, subscriptionId` | Creates a managed private endpoint. |
| `ManagedPrivateEndpoints_Delete` | `DELETE` | `clusterName, managedPrivateEndpointName, resourceGroupName, subscriptionId` | Deletes a managed private endpoint. |
| `ManagedPrivateEndpoints_CheckNameAvailability` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, data__name, data__type` | Checks that the managed private endpoints resource name is valid and is not already in use. |
| `ManagedPrivateEndpoints_Update` | `EXEC` | `clusterName, managedPrivateEndpointName, resourceGroupName, subscriptionId` | Updates a managed private endpoint. |

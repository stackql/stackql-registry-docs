---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - storage_mover
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
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_mover.endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `properties` | `object` | The resource specific properties for the Storage Mover resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Endpoints_Get` | `SELECT` | `endpointName, resourceGroupName, storageMoverName, subscriptionId` | Gets an Endpoint resource. |
| `Endpoints_List` | `SELECT` | `resourceGroupName, storageMoverName, subscriptionId` | Lists all Endpoints in a Storage Mover. |
| `Endpoints_CreateOrUpdate` | `INSERT` | `endpointName, resourceGroupName, storageMoverName, subscriptionId, data__properties` | Creates or updates an Endpoint resource, which represents a data transfer source or destination. |
| `Endpoints_Delete` | `DELETE` | `endpointName, resourceGroupName, storageMoverName, subscriptionId` | Deletes an Endpoint resource. |
| `Endpoints_Update` | `EXEC` | `endpointName, resourceGroupName, storageMoverName, subscriptionId` | Updates properties for an Endpoint resource. Properties not specified in the request body will be unchanged. |

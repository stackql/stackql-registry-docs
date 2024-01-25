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
| `properties` | `object` | The resource specific properties for the Storage Mover resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `endpointName, resourceGroupName, storageMoverName, subscriptionId` | Gets an Endpoint resource. |
| `list` | `SELECT` | `resourceGroupName, storageMoverName, subscriptionId` | Lists all Endpoints in a Storage Mover. |
| `create_or_update` | `INSERT` | `endpointName, resourceGroupName, storageMoverName, subscriptionId, data__properties` | Creates or updates an Endpoint resource, which represents a data transfer source or destination. |
| `delete` | `DELETE` | `endpointName, resourceGroupName, storageMoverName, subscriptionId` | Deletes an Endpoint resource. |
| `_list` | `EXEC` | `resourceGroupName, storageMoverName, subscriptionId` | Lists all Endpoints in a Storage Mover. |
| `update` | `EXEC` | `endpointName, resourceGroupName, storageMoverName, subscriptionId` | Updates properties for an Endpoint resource. Properties not specified in the request body will be unchanged. |

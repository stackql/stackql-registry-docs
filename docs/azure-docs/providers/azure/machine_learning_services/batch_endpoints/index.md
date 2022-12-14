---
title: batch_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - batch_endpoints
  - machine_learning_services
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
<tr><td><b>Name</b></td><td><code>batch_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_services.batch_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Batch endpoint configuration. |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `BatchEndpoints_Get` | `SELECT` | `endpointName, resourceGroupName, subscriptionId, workspaceName` |
| `BatchEndpoints_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
| `BatchEndpoints_CreateOrUpdate` | `INSERT` | `endpointName, resourceGroupName, subscriptionId, workspaceName, data__location, data__properties` |
| `BatchEndpoints_Delete` | `DELETE` | `endpointName, resourceGroupName, subscriptionId, workspaceName` |
| `BatchEndpoints_ListKeys` | `EXEC` | `endpointName, resourceGroupName, subscriptionId, workspaceName` |
| `BatchEndpoints_Update` | `EXEC` | `endpointName, resourceGroupName, subscriptionId, workspaceName` |

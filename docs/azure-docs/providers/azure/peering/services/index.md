---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - peering
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.peering.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | The type of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | The properties that define connectivity to the Peering Service. |
| `sku` | `object` | The SKU that defines the type of the peering service. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PeeringServices_Get` | `SELECT` | `peeringServiceName, resourceGroupName, subscriptionId` | Gets an existing peering service with the specified name under the given subscription and resource group. |
| `PeeringServices_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the peering services under the given subscription and resource group. |
| `PeeringServices_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all of the peerings under the given subscription. |
| `PeeringServices_CreateOrUpdate` | `INSERT` | `peeringServiceName, resourceGroupName, subscriptionId, data__location` | Creates a new peering service or updates an existing peering with the specified name under the given subscription and resource group. |
| `PeeringServices_Delete` | `DELETE` | `peeringServiceName, resourceGroupName, subscriptionId` | Deletes an existing peering service with the specified name under the given subscription and resource group. |
| `PeeringServices_InitializeConnectionMonitor` | `EXEC` | `subscriptionId` | Initialize Peering Service for Connection Monitor functionality |
| `PeeringServices_Update` | `EXEC` | `peeringServiceName, resourceGroupName, subscriptionId` | Updates tags for a peering service with the specified name under the given subscription and resource group. |

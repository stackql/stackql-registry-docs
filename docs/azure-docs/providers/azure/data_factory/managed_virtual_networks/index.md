---
title: managed_virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_virtual_networks
  - data_factory
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
<tr><td><b>Name</b></td><td><code>managed_virtual_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.managed_virtual_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `etag` | `string` | Etag identifies change in the resource. |
| `properties` | `object` | A managed Virtual Network associated with the Azure Data Factory |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedVirtualNetworks_Get` | `SELECT` | `api-version, factoryName, managedVirtualNetworkName, resourceGroupName, subscriptionId` | Gets a managed Virtual Network. |
| `ManagedVirtualNetworks_ListByFactory` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists managed Virtual Networks. |
| `ManagedVirtualNetworks_CreateOrUpdate` | `INSERT` | `api-version, factoryName, managedVirtualNetworkName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a managed Virtual Network. |

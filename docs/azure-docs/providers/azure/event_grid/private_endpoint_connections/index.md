---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - event_grid
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of the private endpoint connection resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `parentName, parentType, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Get a specific private endpoint connection under a topic, domain, or partner namespace or namespace. |
| `list_by_resource` | `SELECT` | `parentName, parentType, resourceGroupName, subscriptionId` | Get all private endpoint connections under a topic, domain, or partner namespace or namespace. |
| `delete` | `DELETE` | `parentName, parentType, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Delete a specific private endpoint connection under a topic, domain, or partner namespace or namespace. |
| `_list_by_resource` | `EXEC` | `parentName, parentType, resourceGroupName, subscriptionId` | Get all private endpoint connections under a topic, domain, or partner namespace or namespace. |
| `update` | `EXEC` | `parentName, parentType, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Update a specific private endpoint connection under a topic, domain or partner namespace. |

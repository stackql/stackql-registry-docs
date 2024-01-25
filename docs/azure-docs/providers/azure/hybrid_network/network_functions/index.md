---
title: network_functions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_functions
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>network_functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.network_functions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Network function properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkFunctionName, resourceGroupName, subscriptionId` | Gets information about the specified network function resource. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the network function resources in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all the network functions in a subscription. |
| `create_or_update` | `INSERT` | `networkFunctionName, resourceGroupName, subscriptionId` | Creates or updates a network function resource. |
| `delete` | `DELETE` | `networkFunctionName, resourceGroupName, subscriptionId` | Deletes the specified network function resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the network function resources in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all the network functions in a subscription. |
| `execute_request` | `EXEC` | `networkFunctionName, resourceGroupName, subscriptionId, data__requestMetadata, data__serviceEndpoint` | Execute a request to services on a containerized network function. |

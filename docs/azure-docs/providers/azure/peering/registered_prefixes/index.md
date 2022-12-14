---
title: registered_prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - registered_prefixes
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
<tr><td><b>Name</b></td><td><code>registered_prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.peering.registered_prefixes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | The properties that define a registered prefix. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RegisteredPrefixes_Get` | `SELECT` | `peeringName, registeredPrefixName, resourceGroupName, subscriptionId` | Gets an existing registered prefix with the specified name under the given subscription, resource group and peering. |
| `RegisteredPrefixes_ListByPeering` | `SELECT` | `peeringName, resourceGroupName, subscriptionId` | Lists all registered prefixes under the given subscription, resource group and peering. |
| `RegisteredPrefixes_CreateOrUpdate` | `INSERT` | `peeringName, registeredPrefixName, resourceGroupName, subscriptionId` | Creates a new registered prefix with the specified name under the given subscription, resource group and peering. |
| `RegisteredPrefixes_Delete` | `DELETE` | `peeringName, registeredPrefixName, resourceGroupName, subscriptionId` | Deletes an existing registered prefix with the specified name under the given subscription, resource group and peering. |
| `RegisteredPrefixes_Validate` | `EXEC` | `peeringName, registeredPrefixName, resourceGroupName, subscriptionId` | Validates an existing registered prefix with the specified name under the given subscription, resource group and peering. |

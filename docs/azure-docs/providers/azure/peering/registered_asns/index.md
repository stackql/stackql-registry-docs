---
title: registered_asns
hide_title: false
hide_table_of_contents: false
keywords:
  - registered_asns
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
<tr><td><b>Name</b></td><td><code>registered_asns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.peering.registered_asns</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | The properties that define a registered ASN. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RegisteredAsns_Get` | `SELECT` | `peeringName, registeredAsnName, resourceGroupName, subscriptionId` | Gets an existing registered ASN with the specified name under the given subscription, resource group and peering. |
| `RegisteredAsns_ListByPeering` | `SELECT` | `peeringName, resourceGroupName, subscriptionId` | Lists all registered ASNs under the given subscription, resource group and peering. |
| `RegisteredAsns_CreateOrUpdate` | `INSERT` | `peeringName, registeredAsnName, resourceGroupName, subscriptionId` | Creates a new registered ASN with the specified name under the given subscription, resource group and peering. |
| `RegisteredAsns_Delete` | `DELETE` | `peeringName, registeredAsnName, resourceGroupName, subscriptionId` | Deletes an existing registered ASN with the specified name under the given subscription, resource group and peering. |

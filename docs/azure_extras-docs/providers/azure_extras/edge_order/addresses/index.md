---
title: addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - addresses
  - edge_order
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
<tr><td><b>Name</b></td><td><code>addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.edge_order.addresses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Address Properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Addresses_Get` | `SELECT` | `addressName, resourceGroupName, subscriptionId` | Get information about the specified address. |
| `Addresses_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the addresses available under the given resource group. |
| `Addresses_ListBySubscription` | `SELECT` | `subscriptionId` | List all the addresses available under the subscription. |
| `Addresses_Create` | `INSERT` | `addressName, resourceGroupName, subscriptionId, data__properties` | Create a new address with the specified parameters. Existing address cannot be updated with this API and should<br />instead be updated with the Update address API. |
| `Addresses_Delete` | `DELETE` | `addressName, resourceGroupName, subscriptionId` | Delete an address. |
| `Addresses_Update` | `EXEC` | `addressName, resourceGroupName, subscriptionId` | Update the properties of an existing address. |

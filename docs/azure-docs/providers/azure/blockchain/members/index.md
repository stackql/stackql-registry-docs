---
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
  - blockchain
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
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.blockchain.members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The GEO location of the blockchain service. |
| `properties` | `object` | Payload of the blockchain member properties for a blockchain member. |
| `sku` | `object` | Blockchain member Sku in payload |
| `tags` | `object` | Tags of the service which is a list of key value pairs that describes the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `blockchainMemberName, resourceGroupName, subscriptionId` | Get details about a blockchain member. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the blockchain members for a resource group. |
| `create` | `INSERT` | `blockchainMemberName, resourceGroupName, subscriptionId` | Create a blockchain member. |
| `delete` | `DELETE` | `blockchainMemberName, resourceGroupName, subscriptionId` | Delete a blockchain member. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Lists the blockchain members for a resource group. |
| `update` | `EXEC` | `blockchainMemberName, resourceGroupName, subscriptionId` | Update a blockchain member. |

---
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
  - blockchain
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
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.blockchain.members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Payload of the blockchain member properties for a blockchain member. |
| `sku` | `object` | Blockchain member Sku in payload |
| `tags` | `object` | Tags of the service which is a list of key value pairs that describes the resource. |
| `location` | `string` | The GEO location of the blockchain service. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BlockchainMembers_Get` | `SELECT` | `blockchainMemberName, resourceGroupName, subscriptionId` | Get details about a blockchain member. |
| `BlockchainMembers_List` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the blockchain members for a resource group. |
| `BlockchainMembers_ListAll` | `SELECT` | `subscriptionId` | Lists the blockchain members for a subscription. |
| `BlockchainMembers_Create` | `INSERT` | `blockchainMemberName, resourceGroupName, subscriptionId` | Create a blockchain member. |
| `BlockchainMembers_Delete` | `DELETE` | `blockchainMemberName, resourceGroupName, subscriptionId` | Delete a blockchain member. |
| `BlockchainMembers_ListApiKeys` | `EXEC` | `blockchainMemberName, resourceGroupName, subscriptionId` | Lists the API keys for a blockchain member. |
| `BlockchainMembers_ListConsortiumMembers` | `EXEC` | `blockchainMemberName, resourceGroupName, subscriptionId` | Lists the consortium members for a blockchain member. |
| `BlockchainMembers_ListRegenerateApiKeys` | `EXEC` | `blockchainMemberName, resourceGroupName, subscriptionId` | Regenerate the API keys for a blockchain member. |
| `BlockchainMembers_Update` | `EXEC` | `blockchainMemberName, resourceGroupName, subscriptionId` | Update a blockchain member. |

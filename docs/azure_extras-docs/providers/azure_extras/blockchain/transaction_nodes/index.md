---
title: transaction_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - transaction_nodes
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
<tr><td><b>Name</b></td><td><code>transaction_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.blockchain.transaction_nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource Id of the resource. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | Gets or sets the transaction node location. |
| `properties` | `object` | Payload of transaction node properties payload in the transaction node payload. |
| `type` | `string` | The type of the service - e.g. "Microsoft.Blockchain" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TransactionNodes_Get` | `SELECT` | `blockchainMemberName, resourceGroupName, subscriptionId, transactionNodeName` | Get the details of the transaction node. |
| `TransactionNodes_List` | `SELECT` | `blockchainMemberName, resourceGroupName, subscriptionId` | Lists the transaction nodes for a blockchain member. |
| `TransactionNodes_Create` | `INSERT` | `blockchainMemberName, resourceGroupName, subscriptionId, transactionNodeName` | Create or update the transaction node. |
| `TransactionNodes_Delete` | `DELETE` | `blockchainMemberName, resourceGroupName, subscriptionId, transactionNodeName` | Delete the transaction node. |
| `TransactionNodes_ListApiKeys` | `EXEC` | `blockchainMemberName, resourceGroupName, subscriptionId, transactionNodeName` | List the API keys for the transaction node. |
| `TransactionNodes_ListRegenerateApiKeys` | `EXEC` | `blockchainMemberName, resourceGroupName, subscriptionId, transactionNodeName` | Regenerate the API keys for the blockchain member. |
| `TransactionNodes_Update` | `EXEC` | `blockchainMemberName, resourceGroupName, subscriptionId, transactionNodeName` | Update the transaction node. |

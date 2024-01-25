---
title: transaction_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - transaction_nodes
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
<tr><td><b>Name</b></td><td><code>transaction_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.blockchain.transaction_nodes</code></td></tr>
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
| `get` | `SELECT` | `blockchainMemberName, resourceGroupName, subscriptionId, transactionNodeName` | Get the details of the transaction node. |
| `list` | `SELECT` | `blockchainMemberName, resourceGroupName, subscriptionId` | Lists the transaction nodes for a blockchain member. |
| `create` | `INSERT` | `blockchainMemberName, resourceGroupName, subscriptionId, transactionNodeName` | Create or update the transaction node. |
| `delete` | `DELETE` | `blockchainMemberName, resourceGroupName, subscriptionId, transactionNodeName` | Delete the transaction node. |
| `_list` | `EXEC` | `blockchainMemberName, resourceGroupName, subscriptionId` | Lists the transaction nodes for a blockchain member. |
| `update` | `EXEC` | `blockchainMemberName, resourceGroupName, subscriptionId, transactionNodeName` | Update the transaction node. |

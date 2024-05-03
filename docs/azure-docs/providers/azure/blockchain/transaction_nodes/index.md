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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transaction_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.blockchain.transaction_nodes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource Id of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | Gets or sets the transaction node location. |
| <CopyableCode code="properties" /> | `object` | Payload of transaction node properties payload in the transaction node payload. |
| <CopyableCode code="type" /> | `string` | The type of the service - e.g. "Microsoft.Blockchain" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="blockchainMemberName, resourceGroupName, subscriptionId, transactionNodeName" /> | Get the details of the transaction node. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="blockchainMemberName, resourceGroupName, subscriptionId" /> | Lists the transaction nodes for a blockchain member. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="blockchainMemberName, resourceGroupName, subscriptionId, transactionNodeName" /> | Create or update the transaction node. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="blockchainMemberName, resourceGroupName, subscriptionId, transactionNodeName" /> | Delete the transaction node. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="blockchainMemberName, resourceGroupName, subscriptionId" /> | Lists the transaction nodes for a blockchain member. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="blockchainMemberName, resourceGroupName, subscriptionId, transactionNodeName" /> | Update the transaction node. |

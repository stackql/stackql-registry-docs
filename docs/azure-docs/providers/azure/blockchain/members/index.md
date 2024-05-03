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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.blockchain.members" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The GEO location of the blockchain service. |
| <CopyableCode code="properties" /> | `object` | Payload of the blockchain member properties for a blockchain member. |
| <CopyableCode code="sku" /> | `object` | Blockchain member Sku in payload |
| <CopyableCode code="tags" /> | `object` | Tags of the service which is a list of key value pairs that describes the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="blockchainMemberName, resourceGroupName, subscriptionId" /> | Get details about a blockchain member. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the blockchain members for a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="blockchainMemberName, resourceGroupName, subscriptionId" /> | Create a blockchain member. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="blockchainMemberName, resourceGroupName, subscriptionId" /> | Delete a blockchain member. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the blockchain members for a resource group. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="blockchainMemberName, resourceGroupName, subscriptionId" /> | Update a blockchain member. |

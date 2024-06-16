---
title: logical_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - logical_networks
  - azure_stack_hci
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>logical_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.logical_networks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties under the logical network resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="logicalNetworkName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the logical networks in the specified resource group. Use the nextLink property in the response to get the next page of logical networks. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="logicalNetworkName, resourceGroupName, subscriptionId" /> | The operation to create or update a logical network. Please note some properties can be set only during logical network creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="logicalNetworkName, resourceGroupName, subscriptionId" /> | The operation to delete a logical network. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="logicalNetworkName, resourceGroupName, subscriptionId" /> | The operation to update a logical network. |

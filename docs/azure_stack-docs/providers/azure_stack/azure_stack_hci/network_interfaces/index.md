---
title: network_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interfaces
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
<tr><td><b>Name</b></td><td><code>network_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.network_interfaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties under the network interface resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId" /> | Gets a network interface |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the network interfaces in the specified resource group. Use the nextLink property in the response to get the next page of network interfaces. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId" /> | The operation to create or update a network interface. Please note some properties can be set only during network interface creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId" /> | The operation to delete a network interface. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId" /> | The operation to update a network interface. |

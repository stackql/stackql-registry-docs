---
title: subnets
hide_title: false
hide_table_of_contents: false
keywords:
  - subnets
  - network
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
<tr><td><b>Name</b></td><td><code>subnets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.subnets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the subnet. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subnetName, subscriptionId, virtualNetworkName" /> | Gets the specified subnet by virtual network and resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName" /> | Gets all subnets in a virtual network. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subnetName, subscriptionId, virtualNetworkName" /> | Creates or updates a subnet in the specified virtual network. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subnetName, subscriptionId, virtualNetworkName" /> | Deletes the specified subnet. |
| <CopyableCode code="prepare_network_policies" /> | `EXEC` | <CopyableCode code="resourceGroupName, subnetName, subscriptionId, virtualNetworkName" /> | Prepares a subnet by applying network intent policies. |
| <CopyableCode code="unprepare_network_policies" /> | `EXEC` | <CopyableCode code="resourceGroupName, subnetName, subscriptionId, virtualNetworkName" /> | Unprepares a subnet by removing network intent policies. |

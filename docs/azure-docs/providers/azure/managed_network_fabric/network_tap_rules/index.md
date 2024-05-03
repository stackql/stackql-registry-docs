---
title: network_tap_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - network_tap_rules
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>network_tap_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_tap_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network Tap Rule Properties defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkTapRuleName, resourceGroupName, subscriptionId" /> | Get Network Tap Rule resource details. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the Network Tap Rule resources in the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the Network Tap Rule resources in the given subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkTapRuleName, resourceGroupName, subscriptionId, data__properties" /> | Create Network Tap Rule resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkTapRuleName, resourceGroupName, subscriptionId" /> | Delete Network Tap Rule resource. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the Network Tap Rule resources in the given resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List all the Network Tap Rule resources in the given subscription. |
| <CopyableCode code="resync" /> | `EXEC` | <CopyableCode code="networkTapRuleName, resourceGroupName, subscriptionId" /> | Implements the operation to the underlying resources. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="networkTapRuleName, resourceGroupName, subscriptionId" /> | Update certain properties of the Network Tap Rule resource. |
| <CopyableCode code="validate_configuration" /> | `EXEC` | <CopyableCode code="networkTapRuleName, resourceGroupName, subscriptionId" /> | Implements the operation to the underlying resources. |

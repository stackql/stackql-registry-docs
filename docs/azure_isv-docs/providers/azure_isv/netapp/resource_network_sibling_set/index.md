---
title: resource_network_sibling_set
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_network_sibling_set
  - netapp
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>resource_network_sibling_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.resource_network_sibling_set" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="networkFeatures" /> | `string` | Network features available to the volume, or current state of update. |
| <CopyableCode code="networkSiblingSetId" /> | `string` | Network Sibling Set ID for a group of volumes sharing networking resources in a subnet. |
| <CopyableCode code="networkSiblingSetStateId" /> | `string` | Network sibling set state Id identifying the current state of the sibling set. |
| <CopyableCode code="nicInfoList" /> | `array` | List of NIC information |
| <CopyableCode code="provisioningState" /> | `string` | Gets the status of the NetworkSiblingSet at the time the operation was called. |
| <CopyableCode code="subnetId" /> | `string` | The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes. Example /subscriptions/subscriptionId/resourceGroups/resourceGroup/providers/Microsoft.Network/virtualNetworks/testVnet/subnets/&#123;mySubnet&#125; |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="query_network_sibling_set" /> | `SELECT` | <CopyableCode code="location, subscriptionId, data__networkSiblingSetId, data__subnetId" /> | Get details of the specified network sibling set. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__networkFeatures, data__networkSiblingSetId, data__networkSiblingSetStateId, data__subnetId" /> | Update the network features of the specified network sibling set. |

---
title: network_to_network_interconnects
hide_title: false
hide_table_of_contents: false
keywords:
  - network_to_network_interconnects
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
<tr><td><b>Name</b></td><td><code>network_to_network_interconnects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_to_network_interconnects" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkFabricName, networkToNetworkInterconnectName, resourceGroupName, subscriptionId" /> | Implements NetworkToNetworkInterconnects GET method. |
| <CopyableCode code="list_by_network_fabric" /> | `SELECT` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Implements Network To Network Interconnects list by Network Fabric GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkFabricName, networkToNetworkInterconnectName, resourceGroupName, subscriptionId, data__properties" /> | Configuration used to setup CE-PE connectivity PUT Method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkFabricName, networkToNetworkInterconnectName, resourceGroupName, subscriptionId" /> | Implements NetworkToNetworkInterconnects DELETE method. |
| <CopyableCode code="_list_by_network_fabric" /> | `EXEC` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Implements Network To Network Interconnects list by Network Fabric GET method. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="networkFabricName, networkToNetworkInterconnectName, resourceGroupName, subscriptionId" /> | Update certain properties of the Network To NetworkInterconnects resource. |

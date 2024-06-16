---
title: packet_captures
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_captures
  - mobile_network
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
<tr><td><b>Name</b></td><td><code>packet_captures</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.packet_captures" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="packetCaptureName, packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Gets information about the specified packet capture session. |
| <CopyableCode code="list_by_packet_core_control_plane" /> | `SELECT` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Lists all the packet capture sessions under a packet core control plane. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="packetCaptureName, packetCoreControlPlaneName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a packet capture. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="packetCaptureName, packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Deletes the specified packet capture. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="packetCaptureName, packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Stop a packet capture session. |

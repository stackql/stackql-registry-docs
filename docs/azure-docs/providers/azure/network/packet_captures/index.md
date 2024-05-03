---
title: packet_captures
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_captures
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
<tr><td><b>Name</b></td><td><code>packet_captures</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.packet_captures" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the packet capture operation. |
| <CopyableCode code="name" /> | `string` | Name of the packet capture session. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | The properties of a packet capture session. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkWatcherName, packetCaptureName, resourceGroupName, subscriptionId" /> | Gets a packet capture session by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> | Lists all packet capture sessions within the specified resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkWatcherName, packetCaptureName, resourceGroupName, subscriptionId, data__properties" /> | Create and start a packet capture on the specified VM. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkWatcherName, packetCaptureName, resourceGroupName, subscriptionId" /> | Deletes the specified packet capture session. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> | Lists all packet capture sessions within the specified resource group. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="networkWatcherName, packetCaptureName, resourceGroupName, subscriptionId" /> | Stops a specified packet capture session. |

---
title: packet_core_control_planes
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_core_control_planes
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
<tr><td><b>Name</b></td><td><code>packet_core_control_planes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.packet_core_control_planes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Packet core control plane properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Gets information about the specified packet core control plane. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the packet core control planes in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the packet core control planes in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a packet core control plane. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Deletes the specified packet core control plane. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the packet core control planes in a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all the packet core control planes in a subscription. |
| <CopyableCode code="collect_diagnostics_package" /> | `EXEC` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId, data__storageAccountBlobUrl" /> | Collect a diagnostics package for the specified packet core control plane. This action will upload the diagnostics to a storage account. |
| <CopyableCode code="reinstall" /> | `EXEC` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Reinstall the specified packet core control plane. This action will remove any transaction state from the packet core to return it to a known state. This action will cause a service outage. |
| <CopyableCode code="rollback" /> | `EXEC` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Roll back the specified packet core control plane to the previous version, "rollbackVersion". Multiple consecutive rollbacks are not possible. This action may cause a service outage. |

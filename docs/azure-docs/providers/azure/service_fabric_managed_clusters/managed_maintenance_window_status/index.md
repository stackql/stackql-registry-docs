---
title: managed_maintenance_window_status
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_maintenance_window_status
  - service_fabric_managed_clusters
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
<tr><td><b>Name</b></td><td><code>managed_maintenance_window_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_managed_clusters.managed_maintenance_window_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="canApplyUpdates" /> | `boolean` | If updates can be applied. |
| <CopyableCode code="isRegionReady" /> | `boolean` | Indicates if the region is ready to configure maintenance windows. |
| <CopyableCode code="isWindowActive" /> | `boolean` | If maintenance window is active. |
| <CopyableCode code="isWindowEnabled" /> | `boolean` | If maintenance window is enabled on this cluster. |
| <CopyableCode code="lastWindowEndTimeUTC" /> | `string` | Last window end time in UTC. |
| <CopyableCode code="lastWindowStartTimeUTC" /> | `string` | Last window start time in UTC. |
| <CopyableCode code="lastWindowStatusUpdateAtUTC" /> | `string` | Last window update time in UTC. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, clusterName, resourceGroupName, subscriptionId" /> |

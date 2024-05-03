---
title: processes_liveness
hide_title: false
hide_table_of_contents: false
keywords:
  - processes_liveness
  - service_map
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
<tr><td><b>Name</b></td><td><code>processes_liveness</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_map.processes_liveness" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endTime" /> | `string` | Liveness interval end time. |
| <CopyableCode code="live" /> | `boolean` | `true` if the resource is live during [startTime, endTime], `false` otherwise |
| <CopyableCode code="startTime" /> | `string` | Liveness interval start time. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="machineName, processName, resourceGroupName, subscriptionId, workspaceName" /> |

---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - storsimple_1200_series
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="endTime" /> | `string` | The UTC time at which the job completed |
| <CopyableCode code="error" /> | `object` | The job error information containing List of JobErrorItem. |
| <CopyableCode code="percentComplete" /> | `integer` | The percentage of the job that is already complete |
| <CopyableCode code="properties" /> | `object` | properties for the job |
| <CopyableCode code="startTime" /> | `string` | The UTC time at which the job was started |
| <CopyableCode code="status" /> | `string` | Current status of the job |
| <CopyableCode code="type" /> | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, jobName, managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified job name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the jobs in a device. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Retrieves all the jobs in a manager. |
| <CopyableCode code="_list_by_device" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves all the jobs in a device. |
| <CopyableCode code="_list_by_manager" /> | `EXEC` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Retrieves all the jobs in a manager. |

---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - storsimple_8000_series
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="endTime" /> | `string` | The UTC time at which the job completed. |
| <CopyableCode code="error" /> | `object` | The job error details. Contains list of job error items. |
| <CopyableCode code="kind" /> | `string` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="percentComplete" /> | `integer` | The percentage of the job that is already complete. |
| <CopyableCode code="properties" /> | `object` | The properties of the job. |
| <CopyableCode code="startTime" /> | `string` | The UTC time at which the job was started. |
| <CopyableCode code="status" /> | `string` | The current status of the job. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, jobName, managerName, resourceGroupName, subscriptionId" /> | Gets the details of the specified job name. |
| <CopyableCode code="list_by_device" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Gets all the jobs for specified device. With optional OData query parameters, a filtered set of jobs is returned. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Gets all the jobs for the specified manager. With optional OData query parameters, a filtered set of jobs is returned. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="deviceName, jobName, managerName, resourceGroupName, subscriptionId" /> | Cancels a job on the device. |

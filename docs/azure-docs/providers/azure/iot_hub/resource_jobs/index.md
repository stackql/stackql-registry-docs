---
title: resource_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_jobs
  - iot_hub
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
<tr><td><b>Name</b></td><td><code>resource_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.resource_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endTimeUtc" /> | `string` | The time the job stopped processing. |
| <CopyableCode code="failureReason" /> | `string` | If status == failed, this string containing the reason for the failure. |
| <CopyableCode code="jobId" /> | `string` | The job identifier. |
| <CopyableCode code="parentJobId" /> | `string` | The job identifier of the parent job, if any. |
| <CopyableCode code="startTimeUtc" /> | `string` | The start time of the job. |
| <CopyableCode code="status" /> | `string` | The status of the job. |
| <CopyableCode code="statusMessage" /> | `string` | The status message for the job. |
| <CopyableCode code="type" /> | `string` | The type of the job. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> |

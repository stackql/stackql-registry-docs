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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_hub.resource_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `endTimeUtc` | `string` | The time the job stopped processing. |
| `failureReason` | `string` | If status == failed, this string containing the reason for the failure. |
| `jobId` | `string` | The job identifier. |
| `parentJobId` | `string` | The job identifier of the parent job, if any. |
| `startTimeUtc` | `string` | The start time of the job. |
| `status` | `string` | The status of the job. |
| `statusMessage` | `string` | The status message for the job. |
| `type` | `string` | The type of the job. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` |
| `_list` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` |

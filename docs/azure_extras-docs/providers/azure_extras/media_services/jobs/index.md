---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - media_services
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.media_services.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of the Job. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Jobs_Get` | `SELECT` | `accountName, api-version, jobName, resourceGroupName, subscriptionId, transformName` | Gets a Job. |
| `Jobs_List` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId, transformName` | Lists all of the Jobs for the Transform. |
| `Jobs_Create` | `INSERT` | `accountName, api-version, jobName, resourceGroupName, subscriptionId, transformName` | Creates a Job. |
| `Jobs_Delete` | `DELETE` | `accountName, api-version, jobName, resourceGroupName, subscriptionId, transformName` | Deletes a Job. |
| `Jobs_CancelJob` | `EXEC` | `accountName, api-version, jobName, resourceGroupName, subscriptionId, transformName` | Cancel a Job. |
| `Jobs_Update` | `EXEC` | `accountName, api-version, jobName, resourceGroupName, subscriptionId, transformName` | Update is only supported for description and priority. Updating Priority will take effect when the Job state is Queued or Scheduled and depending on the timing the priority update may be ignored. |

---
title: jobs_job_history
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs_job_history
  - scheduler
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
<tr><td><b>Name</b></td><td><code>jobs_job_history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.scheduler.jobs_job_history</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets the job history identifier. |
| `name` | `string` | Gets the job history name. |
| `properties` | `object` |  |
| `type` | `string` | Gets the job history resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `api-version, jobCollectionName, jobName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `api-version, jobCollectionName, jobName, resourceGroupName, subscriptionId` |

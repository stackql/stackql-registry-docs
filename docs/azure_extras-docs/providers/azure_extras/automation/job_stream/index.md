---
title: job_stream
hide_title: false
hide_table_of_contents: false
keywords:
  - job_stream
  - automation
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
<tr><td><b>Name</b></td><td><code>job_stream</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.job_stream</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the id of the resource. |
| `properties` | `object` | Definition of the job stream. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobStream_Get` | `SELECT` | `automationAccountName, jobName, jobStreamId, resourceGroupName, subscriptionId` | Retrieve the job stream identified by job stream id. |
| `JobStream_ListByJob` | `SELECT` | `automationAccountName, jobName, resourceGroupName, subscriptionId` | Retrieve a list of jobs streams identified by job name. |

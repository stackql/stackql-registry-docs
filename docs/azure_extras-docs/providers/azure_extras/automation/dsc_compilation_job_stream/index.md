---
title: dsc_compilation_job_stream
hide_title: false
hide_table_of_contents: false
keywords:
  - dsc_compilation_job_stream
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
<tr><td><b>Name</b></td><td><code>dsc_compilation_job_stream</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.dsc_compilation_job_stream</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the id of the resource. |
| `properties` | `object` | Definition of the job stream. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `DscCompilationJobStream_ListByJob` | `SELECT` | `automationAccountName, jobId, resourceGroupName, subscriptionId` |

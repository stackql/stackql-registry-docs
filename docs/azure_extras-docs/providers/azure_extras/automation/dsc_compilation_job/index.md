---
title: dsc_compilation_job
hide_title: false
hide_table_of_contents: false
keywords:
  - dsc_compilation_job
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
<tr><td><b>Name</b></td><td><code>dsc_compilation_job</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.dsc_compilation_job</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DscCompilationJob_Get` | `SELECT` | `automationAccountName, compilationJobName, resourceGroupName, subscriptionId` | Retrieve the Dsc configuration compilation job identified by job id. |
| `DscCompilationJob_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of dsc compilation jobs. |
| `DscCompilationJob_Create` | `INSERT` | `automationAccountName, compilationJobName, resourceGroupName, subscriptionId, data__properties` | Creates the Dsc compilation job of the configuration. |
| `DscCompilationJob_GetStream` | `EXEC` | `automationAccountName, jobId, jobStreamId, resourceGroupName, subscriptionId` | Retrieve the job stream identified by job stream id. |

---
title: source_control_sync_job
hide_title: false
hide_table_of_contents: false
keywords:
  - source_control_sync_job
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
<tr><td><b>Name</b></td><td><code>source_control_sync_job</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.source_control_sync_job</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The id of the job. |
| `properties` | `object` | Definition of source control sync job properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SourceControlSyncJob_Get` | `SELECT` | `automationAccountName, resourceGroupName, sourceControlName, sourceControlSyncJobId, subscriptionId` | Retrieve the source control sync job identified by job id. |
| `SourceControlSyncJob_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, sourceControlName, subscriptionId` | Retrieve a list of source control sync jobs. |
| `SourceControlSyncJob_Create` | `INSERT` | `automationAccountName, resourceGroupName, sourceControlName, sourceControlSyncJobId, subscriptionId, data__properties` | Creates the sync job for a source control. |

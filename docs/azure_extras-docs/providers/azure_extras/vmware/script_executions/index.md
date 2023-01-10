---
title: script_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - script_executions
  - vmware
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
<tr><td><b>Name</b></td><td><code>script_executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.vmware.script_executions</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ScriptExecutions_Get` | `SELECT` | `privateCloudName, resourceGroupName, scriptExecutionName, subscriptionId` |  |
| `ScriptExecutions_List` | `SELECT` | `privateCloudName, resourceGroupName, subscriptionId` |  |
| `ScriptExecutions_CreateOrUpdate` | `INSERT` | `privateCloudName, resourceGroupName, scriptExecutionName, subscriptionId` |  |
| `ScriptExecutions_Delete` | `DELETE` | `privateCloudName, resourceGroupName, scriptExecutionName, subscriptionId` |  |
| `ScriptExecutions_GetExecutionLogs` | `EXEC` | `privateCloudName, resourceGroupName, scriptExecutionName, subscriptionId` | Return the logs for a script execution resource |

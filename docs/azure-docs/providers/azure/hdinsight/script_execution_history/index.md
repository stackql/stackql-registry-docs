---
title: script_execution_history
hide_title: false
hide_table_of_contents: false
keywords:
  - script_execution_history
  - hdinsight
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
<tr><td><b>Name</b></td><td><code>script_execution_history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hdinsight.script_execution_history</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the script action. |
| `endTime` | `string` | The end time of script action execution. |
| `roles` | `array` | The list of roles where script will be executed. |
| `parameters` | `string` | The parameters for the script |
| `startTime` | `string` | The start time of script action execution. |
| `applicationName` | `string` | The application name of the script action, if any. |
| `debugInformation` | `string` | The script action execution debug information. |
| `executionSummary` | `array` | The summary of script action execution result. |
| `scriptExecutionId` | `integer` | The execution id of the script action. |
| `status` | `string` | The current execution status of the script action. |
| `operation` | `string` | The reason why the script action was executed. |
| `uri` | `string` | The URI to the script. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ScriptExecutionHistory_ListByCluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Lists all scripts' execution history for the specified cluster. |
| `ScriptExecutionHistory_Promote` | `EXEC` | `clusterName, resourceGroupName, scriptExecutionId, subscriptionId` | Promotes the specified ad-hoc script execution to a persisted script. |

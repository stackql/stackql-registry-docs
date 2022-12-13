---
title: script_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - script_actions
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
<tr><td><b>Name</b></td><td><code>script_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hdinsight.script_actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the script action. |
| `applicationName` | `string` | The application name of the script action, if any. |
| `endTime` | `string` | The end time of script action execution. |
| `roles` | `array` | The list of roles where script will be executed. |
| `scriptExecutionId` | `integer` | The execution id of the script action. |
| `uri` | `string` | The URI to the script. |
| `startTime` | `string` | The start time of script action execution. |
| `status` | `string` | The current execution status of the script action. |
| `debugInformation` | `string` | The script action execution debug information. |
| `operation` | `string` | The reason why the script action was executed. |
| `parameters` | `string` | The parameters for the script |
| `executionSummary` | `array` | The summary of script action execution result. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ScriptActions_ListByCluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Lists all the persisted script actions for the specified cluster. |
| `ScriptActions_Delete` | `DELETE` | `clusterName, resourceGroupName, scriptName, subscriptionId` | Deletes a specified persisted script action of the cluster. |
| `ScriptActions_GetExecutionAsyncOperationStatus` | `EXEC` | `clusterName, operationId, resourceGroupName, subscriptionId` | Gets the async operation status of execution operation. |
| `ScriptActions_GetExecutionDetail` | `EXEC` | `clusterName, resourceGroupName, scriptExecutionId, subscriptionId` | Gets the script execution detail for the given script execution ID. |

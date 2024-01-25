---
title: workflow_run_actions_expression_traces
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_run_actions_expression_traces
  - app_service
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
<tr><td><b>Name</b></td><td><code>workflow_run_actions_expression_traces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.workflow_run_actions_expression_traces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `inputs` | `array` |  |
| `nextLink` | `string` | The link used to get the next page of recommendations. |
| `value` | `` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `actionName, name, resourceGroupName, runName, subscriptionId, workflowName` |

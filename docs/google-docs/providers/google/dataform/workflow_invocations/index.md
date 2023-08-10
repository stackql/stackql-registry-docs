---
title: workflow_invocations
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_invocations
  - dataform
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_invocations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataform.workflow_invocations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The workflow invocation's name. |
| `state` | `string` | Output only. This workflow invocation's current state. |
| `workflowConfig` | `string` | Immutable. The name of the workflow config to invoke. Must be in the format `projects/*/locations/*/repositories/*/workflowConfigs/*`. |
| `compilationResult` | `string` | Immutable. The name of the compilation result to use for this invocation. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`. |
| `invocationConfig` | `object` | Includes various configuration options for a workflow invocation. If both `included_targets` and `included_tags` are unset, all actions will be included. |
| `invocationTiming` | `object` | Represents a time interval, encoded as a Timestamp start (inclusive) and a Timestamp end (exclusive). The start must be less than or equal to the end. When the start equals the end, the interval is empty (matches no time). When both start and end are unspecified, the interval matches any time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, repositoriesId, workflowInvocationsId` | Fetches a single WorkflowInvocation. |
| `list` | `SELECT` | `locationsId, projectsId, repositoriesId` | Lists WorkflowInvocations in a given Repository. |
| `create` | `INSERT` | `locationsId, projectsId, repositoriesId` | Creates a new WorkflowInvocation in a given Repository. |
| `delete` | `DELETE` | `locationsId, projectsId, repositoriesId, workflowInvocationsId` | Deletes a single WorkflowInvocation. |
| `_list` | `EXEC` | `locationsId, projectsId, repositoriesId` | Lists WorkflowInvocations in a given Repository. |
| `cancel` | `EXEC` | `locationsId, projectsId, repositoriesId, workflowInvocationsId` | Requests cancellation of a running WorkflowInvocation. |
| `query` | `EXEC` | `locationsId, projectsId, repositoriesId, workflowInvocationsId` | Returns WorkflowInvocationActions in a given WorkflowInvocation. |

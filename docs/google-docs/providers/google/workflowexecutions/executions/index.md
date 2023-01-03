---
title: executions
hide_title: false
hide_table_of_contents: false
keywords:
  - executions
  - workflowexecutions
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workflowexecutions.executions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the execution. Format: projects/{project}/locations/{location}/workflows/{workflow}/executions/{execution} |
| `result` | `string` | Output only. Output of the execution represented as a JSON string. The value can only be present if the execution's state is `SUCCEEDED`. |
| `error` | `object` | Error describes why the execution was abnormally terminated. |
| `endTime` | `string` | Output only. Marks the end of execution, successful or not. |
| `workflowRevisionId` | `string` | Output only. Revision of the workflow this execution is using. |
| `state` | `string` | Output only. Current state of the execution. |
| `callLogLevel` | `string` | The call logging level associated to this execution. |
| `startTime` | `string` | Output only. Marks the beginning of execution. |
| `argument` | `string` | Input parameters of the execution represented as a JSON string. The size limit is 32KB. *Note*: If you are using the REST API directly to run your workflow, you must escape any JSON string value of `argument`. Example: `'{"argument":"{\"firstName\":\"FIRST\",\"lastName\":\"LAST\"}"}'` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_workflows_executions_get` | `SELECT` | `executionsId, locationsId, projectsId, workflowsId` | Returns an execution of the given name. |
| `projects_locations_workflows_executions_list` | `SELECT` | `locationsId, projectsId, workflowsId` | Returns a list of executions which belong to the workflow with the given name. The method returns executions of all workflow revisions. Returned executions are ordered by their start time (newest first). |
| `projects_locations_workflows_executions_create` | `INSERT` | `locationsId, projectsId, workflowsId` | Creates a new execution using the latest revision of the given workflow. |
| `projects_locations_workflows_executions_cancel` | `EXEC` | `executionsId, locationsId, projectsId, workflowsId` | Cancels an execution of the given name. |

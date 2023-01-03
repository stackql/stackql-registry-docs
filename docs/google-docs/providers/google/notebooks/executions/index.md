---
title: executions
hide_title: false
hide_table_of_contents: false
keywords:
  - executions
  - notebooks
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
<tr><td><b>Id</b></td><td><code>google.notebooks.executions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the execute. Format: `projects/{project_id}/locations/{location}/executions/{execution_id}` |
| `description` | `string` | A brief description of this execution. |
| `displayName` | `string` | Output only. Name used for UI purposes. Name can only contain alphanumeric characters and underscores '_'. |
| `executionTemplate` | `object` | The description a notebook execution workload. |
| `jobUri` | `string` | Output only. The URI of the external job used to execute the notebook. |
| `createTime` | `string` | Output only. Time the Execution was instantiated. |
| `updateTime` | `string` | Output only. Time the Execution was last updated. |
| `state` | `string` | Output only. State of the underlying AI Platform job. |
| `outputNotebookFile` | `string` | Output notebook file generated by this execution |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_executions_get` | `SELECT` | `executionsId, locationsId, projectsId` | Gets details of executions |
| `projects_locations_executions_list` | `SELECT` | `locationsId, projectsId` | Lists executions in a given project and location |
| `projects_locations_executions_create` | `INSERT` | `locationsId, projectsId` | Creates a new Execution in a given project and location. |
| `projects_locations_executions_delete` | `DELETE` | `executionsId, locationsId, projectsId` | Deletes execution |
---
title: workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - workflows
  - workflows
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
<tr><td><b>Name</b></td><td><code>workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workflows.workflows</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `unreachable` | `array` | Unreachable resources. |
| `workflows` | `array` | The workflows that match the request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, workflowsId` | Gets details of a single workflow. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists workflows in a given project and location. The default order is not specified. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new workflow. If a workflow with the specified name already exists in the specified project and location, the long running operation returns a ALREADY_EXISTS error. |
| `delete` | `DELETE` | `locationsId, projectsId, workflowsId` | Deletes a workflow with the specified name. This method also cancels and deletes all running executions of the workflow. |
| `patch` | `EXEC` | `locationsId, projectsId, workflowsId` | Updates an existing workflow. Running this method has no impact on already running executions of the workflow. A new revision of the workflow might be created as a result of a successful update operation. In that case, the new revision is used in new workflow executions. |

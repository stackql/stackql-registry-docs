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
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `unreachable` | `array` | Locations which could not be reached. |
| `workflowInvocations` | `array` | List of workflow invocations. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, repositoriesId, workflowInvocationsId` | Fetches a single WorkflowInvocation. |
| `list` | `SELECT` | `locationsId, projectsId, repositoriesId` | Lists WorkflowInvocations in a given Repository. |
| `create` | `INSERT` | `locationsId, projectsId, repositoriesId` | Creates a new WorkflowInvocation in a given Repository. |
| `delete` | `DELETE` | `locationsId, projectsId, repositoriesId, workflowInvocationsId` | Deletes a single WorkflowInvocation. |
| `cancel` | `EXEC` | `locationsId, projectsId, repositoriesId, workflowInvocationsId` | Requests cancellation of a running WorkflowInvocation. |
| `query` | `EXEC` | `locationsId, projectsId, repositoriesId, workflowInvocationsId` | Returns WorkflowInvocationActions in a given WorkflowInvocation. |

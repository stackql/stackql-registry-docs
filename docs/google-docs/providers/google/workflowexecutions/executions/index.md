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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `executions` | `array` | The executions which match the request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `executionsId, locationsId, projectsId, workflowsId` | Returns an execution of the given name. |
| `list` | `SELECT` | `locationsId, projectsId, workflowsId` | Returns a list of executions which belong to the workflow with the given name. The method returns executions of all workflow revisions. Returned executions are ordered by their start time (newest first). |
| `create` | `INSERT` | `locationsId, projectsId, workflowsId` | Creates a new execution using the latest revision of the given workflow. |
| `cancel` | `EXEC` | `executionsId, locationsId, projectsId, workflowsId` | Cancels an execution of the given name. |

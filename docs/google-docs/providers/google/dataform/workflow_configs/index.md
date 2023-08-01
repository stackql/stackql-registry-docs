---
title: workflow_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_configs
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
<tr><td><b>Name</b></td><td><code>workflow_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataform.workflow_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `unreachable` | `array` | Locations which could not be reached. |
| `workflowConfigs` | `array` | List of workflow configs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, repositoriesId, workflowConfigsId` | Fetches a single WorkflowConfig. |
| `list` | `SELECT` | `locationsId, projectsId, repositoriesId` | Lists WorkflowConfigs in a given Repository. |
| `create` | `INSERT` | `locationsId, projectsId, repositoriesId` | Creates a new WorkflowConfig in a given Repository. |
| `delete` | `DELETE` | `locationsId, projectsId, repositoriesId, workflowConfigsId` | Deletes a single WorkflowConfig. |
| `patch` | `EXEC` | `locationsId, projectsId, repositoriesId, workflowConfigsId` | Updates a single WorkflowConfig. |

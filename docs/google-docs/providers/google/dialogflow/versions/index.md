---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - dialogflow
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
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `versions` | `array` | A list of versions. There will be a maximum number of items returned based on the page_size field in the request. The list may in some cases be empty or contain fewer entries than page_size even if this isn't the last page. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_flows_versions_get` | `SELECT` | `agentsId, flowsId, locationsId, projectsId, versionsId` | Retrieves the specified Version. |
| `projects_locations_agents_flows_versions_list` | `SELECT` | `agentsId, flowsId, locationsId, projectsId` | Returns the list of all versions in the specified Flow. |
| `projects_locations_agents_flows_versions_create` | `INSERT` | `agentsId, flowsId, locationsId, projectsId` | Creates a Version in the specified Flow. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: CreateVersionOperationMetadata - `response`: Version |
| `projects_locations_agents_flows_versions_delete` | `DELETE` | `agentsId, flowsId, locationsId, projectsId, versionsId` | Deletes the specified Version. |
| `projects_locations_agents_flows_versions_compare_versions` | `EXEC` | `agentsId, flowsId, locationsId, projectsId, versionsId` | Compares the specified base version with target version. |
| `projects_locations_agents_flows_versions_load` | `EXEC` | `agentsId, flowsId, locationsId, projectsId, versionsId` | Loads resources in the specified version to the draft flow. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) |
| `projects_locations_agents_flows_versions_patch` | `EXEC` | `agentsId, flowsId, locationsId, projectsId, versionsId` | Updates the specified Version. |

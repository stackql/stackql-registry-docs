---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - dialogflow
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
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the environment. Format: `projects//locations//agents//environments/`. |
| `description` | `string` | The human-readable description of the environment. The maximum length is 500 characters. If exceeded, the request is rejected. |
| `testCasesConfig` | `object` | The configuration for continuous tests. |
| `updateTime` | `string` | Output only. Update time of this environment. |
| `versionConfigs` | `array` | Required. A list of configurations for flow versions. You should include version configs for all flows that are reachable from `Start Flow` in the agent. Otherwise, an error will be returned. |
| `webhookConfig` | `object` | Configuration for webhooks. |
| `displayName` | `string` | Required. The human-readable name of the environment (unique in an agent). Limit of 64 characters. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_environments_get` | `SELECT` | `agentsId, environmentsId, locationsId, projectsId` | Retrieves the specified Environment. |
| `projects_locations_agents_environments_list` | `SELECT` | `agentsId, locationsId, projectsId` | Returns the list of all environments in the specified Agent. |
| `projects_locations_agents_environments_create` | `INSERT` | `agentsId, locationsId, projectsId` | Creates an Environment in the specified Agent. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: Environment |
| `projects_locations_agents_environments_delete` | `DELETE` | `agentsId, environmentsId, locationsId, projectsId` | Deletes the specified Environment. |
| `projects_locations_agents_environments_deployFlow` | `EXEC` | `agentsId, environmentsId, locationsId, projectsId` | Deploys a flow to the specified Environment. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: DeployFlowMetadata - `response`: DeployFlowResponse |
| `projects_locations_agents_environments_lookupEnvironmentHistory` | `EXEC` | `agentsId, environmentsId, locationsId, projectsId` | Looks up the history of the specified Environment. |
| `projects_locations_agents_environments_patch` | `EXEC` | `agentsId, environmentsId, locationsId, projectsId` | Updates the specified Environment. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: Environment |
| `projects_locations_agents_environments_runContinuousTest` | `EXEC` | `agentsId, environmentsId, locationsId, projectsId` | Kicks off a continuous test under the specified Environment. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: RunContinuousTestMetadata - `response`: RunContinuousTestResponse |

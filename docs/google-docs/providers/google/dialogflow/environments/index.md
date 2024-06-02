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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="dialogflow.environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the environment. Format: `projects//locations//agents//environments/`. |
| <CopyableCode code="description" /> | `string` | The human-readable description of the environment. The maximum length is 500 characters. If exceeded, the request is rejected. |
| <CopyableCode code="displayName" /> | `string` | Required. The human-readable name of the environment (unique in an agent). Limit of 64 characters. |
| <CopyableCode code="testCasesConfig" /> | `object` | The configuration for continuous tests. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time of this environment. |
| <CopyableCode code="versionConfigs" /> | `array` | A list of configurations for flow versions. You should include version configs for all flows that are reachable from `Start Flow` in the agent. Otherwise, an error will be returned. |
| <CopyableCode code="webhookConfig" /> | `object` | Configuration for webhooks. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_environments_get" /> | `SELECT` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId" /> | Retrieves the specified Environment. |
| <CopyableCode code="projects_locations_agents_environments_list" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Returns the list of all environments in the specified Agent. |
| <CopyableCode code="projects_locations_agents_environments_create" /> | `INSERT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Creates an Environment in the specified Agent. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: Environment |
| <CopyableCode code="projects_locations_agents_environments_delete" /> | `DELETE` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId" /> | Deletes the specified Environment. |
| <CopyableCode code="_projects_locations_agents_environments_list" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Returns the list of all environments in the specified Agent. |
| <CopyableCode code="projects_locations_agents_environments_deploy_flow" /> | `EXEC` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId" /> | Deploys a flow to the specified Environment. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: DeployFlowMetadata - `response`: DeployFlowResponse |
| <CopyableCode code="projects_locations_agents_environments_lookup_environment_history" /> | `EXEC` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId" /> | Looks up the history of the specified Environment. |
| <CopyableCode code="projects_locations_agents_environments_patch" /> | `EXEC` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId" /> | Updates the specified Environment. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: Environment |
| <CopyableCode code="projects_locations_agents_environments_run_continuous_test" /> | `EXEC` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId" /> | Kicks off a continuous test under the specified Environment. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: RunContinuousTestMetadata - `response`: RunContinuousTestResponse |

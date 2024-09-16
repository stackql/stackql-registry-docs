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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.environments" /></td></tr>
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
| <CopyableCode code="projects_locations_agents_environments_patch" /> | `UPDATE` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId" /> | Updates the specified Environment. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: Environment |
| <CopyableCode code="projects_locations_agents_environments_deploy_flow" /> | `EXEC` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId" /> | Deploys a flow to the specified Environment. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: DeployFlowMetadata - `response`: DeployFlowResponse |
| <CopyableCode code="projects_locations_agents_environments_lookup_environment_history" /> | `EXEC` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId" /> | Looks up the history of the specified Environment. |
| <CopyableCode code="projects_locations_agents_environments_run_continuous_test" /> | `EXEC` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId" /> | Kicks off a continuous test under the specified Environment. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: RunContinuousTestMetadata - `response`: RunContinuousTestResponse |

## `SELECT` examples

Returns the list of all environments in the specified Agent.

```sql
SELECT
name,
description,
displayName,
testCasesConfig,
updateTime,
versionConfigs,
webhookConfig
FROM google.dialogflow.environments
WHERE agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environments</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.dialogflow.environments (
agentsId,
locationsId,
projectsId,
name,
displayName,
description,
versionConfigs,
testCasesConfig,
webhookConfig
)
SELECT 
'{{ agentsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ versionConfigs }}',
'{{ testCasesConfig }}',
'{{ webhookConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: description
      value: '{{ description }}'
    - name: versionConfigs
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: testCasesConfig
      value:
        - name: testCases
          value:
            - name: type
              value: '{{ type }}'
        - name: enableContinuousRun
          value: '{{ enableContinuousRun }}'
        - name: enablePredeploymentRun
          value: '{{ enablePredeploymentRun }}'
    - name: webhookConfig
      value:
        - name: webhookOverrides
          value:
            - name: $ref
              value: '{{ $ref }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>environments</code> resource.

```sql
/*+ update */
UPDATE google.dialogflow.environments
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
versionConfigs = '{{ versionConfigs }}',
testCasesConfig = '{{ testCasesConfig }}',
webhookConfig = '{{ webhookConfig }}'
WHERE 
agentsId = '{{ agentsId }}'
AND environmentsId = '{{ environmentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>environments</code> resource.

```sql
/*+ delete */
DELETE FROM google.dialogflow.environments
WHERE agentsId = '{{ agentsId }}'
AND environmentsId = '{{ environmentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

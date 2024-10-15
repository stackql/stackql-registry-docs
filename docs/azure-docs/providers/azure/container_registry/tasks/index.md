---
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.tasks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tasks', value: 'view', },
        { label: 'tasks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="agent_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_pool_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed identity for the resource. |
| <CopyableCode code="is_system_task" /> | `text` | field from the `properties` object |
| <CopyableCode code="log_template" /> | `text` | field from the `properties` object |
| <CopyableCode code="platform" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="step" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="taskName" /> | `text` | field from the `properties` object |
| <CopyableCode code="timeout" /> | `text` | field from the `properties` object |
| <CopyableCode code="trigger" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="identity" /> | `object` | Managed identity for the resource. |
| <CopyableCode code="properties" /> | `object` | The properties of a task. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, taskName" /> | Get the properties of a specified task. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all the tasks for a specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, taskName" /> | Creates a task for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, taskName" /> | Deletes a specified task. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, taskName" /> | Updates a task with the specified parameters. |

## `SELECT` examples

Lists all the tasks for a specified container registry.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tasks', value: 'view', },
        { label: 'tasks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
agent_configuration,
agent_pool_name,
creation_date,
credentials,
identity,
is_system_task,
log_template,
platform,
provisioning_state,
registryName,
resourceGroupName,
status,
step,
subscriptionId,
system_data,
taskName,
timeout,
trigger,
type
FROM azure.container_registry.vw_tasks
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
properties,
systemData,
type
FROM azure.container_registry.tasks
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tasks</code> resource.

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
INSERT INTO azure.container_registry.tasks (
registryName,
resourceGroupName,
subscriptionId,
taskName,
identity,
properties
)
SELECT 
'{{ registryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ taskName }}',
'{{ identity }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: creationDate
          value: string
        - name: status
          value: string
        - name: platform
          value:
            - name: os
              value: string
            - name: architecture
              value: string
            - name: variant
              value: string
        - name: agentConfiguration
          value:
            - name: cpu
              value: integer
        - name: agentPoolName
          value: string
        - name: timeout
          value: integer
        - name: step
          value:
            - name: type
              value: string
            - name: baseImageDependencies
              value:
                - - name: type
                    value: string
                  - name: registry
                    value: string
                  - name: repository
                    value: string
                  - name: tag
                    value: string
                  - name: digest
                    value: string
            - name: contextPath
              value: string
            - name: contextAccessToken
              value: string
        - name: trigger
          value:
            - name: timerTriggers
              value:
                - - name: schedule
                    value: string
                  - name: status
                    value: string
                  - name: name
                    value: string
            - name: sourceTriggers
              value:
                - - name: sourceRepository
                    value:
                      - name: sourceControlType
                        value: string
                      - name: repositoryUrl
                        value: string
                      - name: branch
                        value: string
                      - name: sourceControlAuthProperties
                        value:
                          - name: tokenType
                            value: string
                          - name: token
                            value: string
                          - name: refreshToken
                            value: string
                          - name: scope
                            value: string
                          - name: expiresIn
                            value: integer
                  - name: sourceTriggerEvents
                    value:
                      - string
                  - name: status
                    value: string
                  - name: name
                    value: string
            - name: baseImageTrigger
              value:
                - name: baseImageTriggerType
                  value: string
                - name: updateTriggerEndpoint
                  value: string
                - name: updateTriggerPayloadType
                  value: string
                - name: status
                  value: string
                - name: name
                  value: string
        - name: credentials
          value:
            - name: sourceRegistry
              value:
                - name: loginMode
                  value: string
            - name: customRegistries
              value: object
        - name: logTemplate
          value: string
        - name: isSystemTask
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tasks</code> resource.

```sql
/*+ update */
UPDATE azure.container_registry.tasks
SET 
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND taskName = '{{ taskName }}';
```

## `DELETE` example

Deletes the specified <code>tasks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_registry.tasks
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND taskName = '{{ taskName }}';
```

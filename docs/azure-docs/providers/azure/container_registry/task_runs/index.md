---
title: task_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - task_runs
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

Creates, updates, deletes, gets or lists a <code>task_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.task_runs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_task_runs', value: 'view', },
        { label: 'task_runs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="force_update_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed identity for the resource. |
| <CopyableCode code="location" /> | `text` | The location of the resource |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_request" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_result" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="taskRunName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed identity for the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource |
| <CopyableCode code="properties" /> | `object` | The properties of task run. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, taskRunName" /> | Gets the detailed information for a given task run. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all the task runs for a specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, taskRunName" /> | Creates a task run for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, taskRunName" /> | Deletes a specified task run resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, taskRunName" /> | Updates a task run with the specified parameters. |

## `SELECT` examples

Lists all the task runs for a specified container registry.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_task_runs', value: 'view', },
        { label: 'task_runs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
force_update_tag,
identity,
location,
provisioning_state,
registryName,
resourceGroupName,
run_request,
run_result,
subscriptionId,
taskRunName
FROM azure.container_registry.vw_task_runs
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties
FROM azure.container_registry.task_runs
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>task_runs</code> resource.

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
INSERT INTO azure.container_registry.task_runs (
registryName,
resourceGroupName,
subscriptionId,
taskRunName,
identity,
properties,
location
)
SELECT 
'{{ registryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ taskRunName }}',
'{{ identity }}',
'{{ properties }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
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
        - name: runRequest
          value:
            - name: type
              value: string
            - name: isArchiveEnabled
              value: boolean
            - name: agentPoolName
              value: string
            - name: logTemplate
              value: string
        - name: runResult
          value:
            - name: properties
              value:
                - name: runId
                  value: string
                - name: status
                  value: string
                - name: lastUpdatedTime
                  value: string
                - name: runType
                  value: string
                - name: agentPoolName
                  value: string
                - name: createTime
                  value: string
                - name: startTime
                  value: string
                - name: finishTime
                  value: string
                - name: outputImages
                  value:
                    - - name: registry
                        value: string
                      - name: repository
                        value: string
                      - name: tag
                        value: string
                      - name: digest
                        value: string
                - name: task
                  value: string
                - name: imageUpdateTrigger
                  value:
                    - name: id
                      value: string
                    - name: timestamp
                      value: string
                    - name: images
                      value:
                        - - name: registry
                            value: string
                          - name: repository
                            value: string
                          - name: tag
                            value: string
                          - name: digest
                            value: string
                - name: sourceTrigger
                  value:
                    - name: id
                      value: string
                    - name: eventType
                      value: string
                    - name: commitId
                      value: string
                    - name: pullRequestId
                      value: string
                    - name: repositoryUrl
                      value: string
                    - name: branchName
                      value: string
                    - name: providerType
                      value: string
                - name: timerTrigger
                  value:
                    - name: timerTriggerName
                      value: string
                    - name: scheduleOccurrence
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
                - name: sourceRegistryAuth
                  value: string
                - name: customRegistries
                  value:
                    - string
                - name: runErrorMessage
                  value: string
                - name: updateTriggerToken
                  value: string
                - name: logArtifact
                  value:
                    - name: registry
                      value: string
                    - name: repository
                      value: string
                    - name: tag
                      value: string
                    - name: digest
                      value: string
                - name: provisioningState
                  value: string
                - name: isArchiveEnabled
                  value: boolean
        - name: forceUpdateTag
          value: string
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>task_runs</code> resource.

```sql
/*+ update */
UPDATE azure.container_registry.task_runs
SET 
identity = '{{ identity }}',
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND taskRunName = '{{ taskRunName }}';
```

## `DELETE` example

Deletes the specified <code>task_runs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_registry.task_runs
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND taskRunName = '{{ taskRunName }}';
```

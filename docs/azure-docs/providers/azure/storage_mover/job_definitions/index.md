---
title: job_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_definitions
  - storage_mover
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

Creates, updates, deletes, gets or lists a <code>job_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_mover.job_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_definitions', value: 'view', },
        { label: 'job_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="copy_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobDefinitionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="latest_job_run_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="latest_job_run_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="latest_job_run_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_subpath" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageMoverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_subpath" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Job definition properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Gets a Job Definition resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Lists all Job Definitions in a Project. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId, data__properties" /> | Creates or updates a Job Definition resource, which contains configuration for a single unit of managed data transfer. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Deletes a Job Definition resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Updates properties for a Job Definition resource. Properties not specified in the request body will be unchanged. |
| <CopyableCode code="start_job" /> | `EXEC` | <CopyableCode code="jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Creates a new Job Run resource for the specified Job Definition and passes it to the Agent for execution. |
| <CopyableCode code="stop_job" /> | `EXEC` | <CopyableCode code="jobDefinitionName, projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Requests the Agent of any active instance of this Job Definition to stop. |

## `SELECT` examples

Lists all Job Definitions in a Project.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_definitions', value: 'view', },
        { label: 'job_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
agent_name,
agent_resource_id,
copy_mode,
jobDefinitionName,
latest_job_run_name,
latest_job_run_resource_id,
latest_job_run_status,
projectName,
provisioning_state,
resourceGroupName,
source_name,
source_resource_id,
source_subpath,
storageMoverName,
subscriptionId,
system_data,
target_name,
target_resource_id,
target_subpath
FROM azure.storage_mover.vw_job_definitions
WHERE projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.storage_mover.job_definitions
WHERE projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>job_definitions</code> resource.

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
INSERT INTO azure.storage_mover.job_definitions (
jobDefinitionName,
projectName,
resourceGroupName,
storageMoverName,
subscriptionId,
data__properties,
properties,
systemData
)
SELECT 
'{{ jobDefinitionName }}',
'{{ projectName }}',
'{{ resourceGroupName }}',
'{{ storageMoverName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ systemData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: description
          value: string
        - name: copyMode
          value: string
        - name: sourceName
          value: string
        - name: sourceResourceId
          value: string
        - name: sourceSubpath
          value: string
        - name: targetName
          value: string
        - name: targetResourceId
          value: string
        - name: targetSubpath
          value: string
        - name: latestJobRunName
          value: string
        - name: latestJobRunResourceId
          value: string
        - name: latestJobRunStatus
          value: string
        - name: agentName
          value: string
        - name: agentResourceId
          value: string
        - name: provisioningState
          value: []
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>job_definitions</code> resource.

```sql
/*+ update */
UPDATE azure.storage_mover.job_definitions
SET 
properties = '{{ properties }}'
WHERE 
jobDefinitionName = '{{ jobDefinitionName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>job_definitions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage_mover.job_definitions
WHERE jobDefinitionName = '{{ jobDefinitionName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

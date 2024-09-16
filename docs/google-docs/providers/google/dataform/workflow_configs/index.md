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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>workflow_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataform.workflow_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The workflow config's name. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp of when the WorkflowConfig was created. |
| <CopyableCode code="cronSchedule" /> | `string` | Optional. Optional schedule (in cron format) for automatic execution of this workflow config. |
| <CopyableCode code="invocationConfig" /> | `object` | Includes various configuration options for a workflow invocation. If both `included_targets` and `included_tags` are unset, all actions will be included. |
| <CopyableCode code="recentScheduledExecutionRecords" /> | `array` | Output only. Records of the 10 most recent scheduled execution attempts, ordered in in descending order of `execution_time`. Updated whenever automatic creation of a workflow invocation is triggered by cron_schedule. |
| <CopyableCode code="releaseConfig" /> | `string` | Required. The name of the release config whose release_compilation_result should be executed. Must be in the format `projects/*/locations/*/repositories/*/releaseConfigs/*`. |
| <CopyableCode code="timeZone" /> | `string` | Optional. Specifies the time zone to be used when interpreting cron_schedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp of when the WorkflowConfig was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId, workflowConfigsId" /> | Fetches a single WorkflowConfig. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Lists WorkflowConfigs in a given Repository. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Creates a new WorkflowConfig in a given Repository. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, repositoriesId, workflowConfigsId" /> | Deletes a single WorkflowConfig. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, repositoriesId, workflowConfigsId" /> | Updates a single WorkflowConfig. |

## `SELECT` examples

Lists WorkflowConfigs in a given Repository.

```sql
SELECT
name,
createTime,
cronSchedule,
invocationConfig,
recentScheduledExecutionRecords,
releaseConfig,
timeZone,
updateTime
FROM google.dataform.workflow_configs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workflow_configs</code> resource.

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
INSERT INTO google.dataform.workflow_configs (
locationsId,
projectsId,
repositoriesId,
name,
releaseConfig,
invocationConfig,
cronSchedule,
timeZone
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ repositoriesId }}',
'{{ name }}',
'{{ releaseConfig }}',
'{{ invocationConfig }}',
'{{ cronSchedule }}',
'{{ timeZone }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: releaseConfig
      value: '{{ releaseConfig }}'
    - name: invocationConfig
      value:
        - name: includedTargets
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: includedTags
          value:
            - name: type
              value: '{{ type }}'
        - name: transitiveDependenciesIncluded
          value: '{{ transitiveDependenciesIncluded }}'
        - name: transitiveDependentsIncluded
          value: '{{ transitiveDependentsIncluded }}'
        - name: fullyRefreshIncrementalTablesEnabled
          value: '{{ fullyRefreshIncrementalTablesEnabled }}'
        - name: serviceAccount
          value: '{{ serviceAccount }}'
    - name: cronSchedule
      value: '{{ cronSchedule }}'
    - name: timeZone
      value: '{{ timeZone }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workflow_configs</code> resource.

```sql
/*+ update */
UPDATE google.dataform.workflow_configs
SET 
name = '{{ name }}',
releaseConfig = '{{ releaseConfig }}',
invocationConfig = '{{ invocationConfig }}',
cronSchedule = '{{ cronSchedule }}',
timeZone = '{{ timeZone }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'
AND workflowConfigsId = '{{ workflowConfigsId }}';
```

## `DELETE` example

Deletes the specified <code>workflow_configs</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataform.workflow_configs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'
AND workflowConfigsId = '{{ workflowConfigsId }}';
```

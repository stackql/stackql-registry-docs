---
title: import_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - import_jobs
  - migrationcenter
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

Creates, updates, deletes, gets or lists a <code>import_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>import_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.migrationcenter.import_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The full name of the import job. |
| <CopyableCode code="assetSource" /> | `string` | Required. Reference to a source. |
| <CopyableCode code="completeTime" /> | `string` | Output only. The timestamp when the import job was completed. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the import job was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User-friendly display name. Maximum length is 256 characters. |
| <CopyableCode code="executionReport" /> | `object` | A resource that reports result of the import job execution. |
| <CopyableCode code="labels" /> | `object` | Labels as key value pairs. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the import job. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the import job was last updated. |
| <CopyableCode code="validationReport" /> | `object` | A resource that aggregates errors across import job files. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="importJobsId, locationsId, projectsId" /> | Gets the details of an import job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all import jobs. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an import job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="importJobsId, locationsId, projectsId" /> | Deletes an import job. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="importJobsId, locationsId, projectsId" /> | Updates an import job. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="importJobsId, locationsId, projectsId" /> | Runs an import job. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="importJobsId, locationsId, projectsId" /> | Validates an import job. |

## `SELECT` examples

Lists all import jobs.

```sql
SELECT
name,
assetSource,
completeTime,
createTime,
displayName,
executionReport,
labels,
state,
updateTime,
validationReport
FROM google.migrationcenter.import_jobs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>import_jobs</code> resource.

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
INSERT INTO google.migrationcenter.import_jobs (
locationsId,
projectsId,
name,
displayName,
createTime,
updateTime,
completeTime,
state,
labels,
assetSource,
validationReport,
executionReport
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ completeTime }}',
'{{ state }}',
'{{ labels }}',
'{{ assetSource }}',
'{{ validationReport }}',
'{{ executionReport }}'
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
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: completeTime
      value: '{{ completeTime }}'
    - name: state
      value: '{{ state }}'
    - name: labels
      value: '{{ labels }}'
    - name: assetSource
      value: '{{ assetSource }}'
    - name: validationReport
      value: '{{ validationReport }}'
    - name: executionReport
      value: '{{ executionReport }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>import_jobs</code> resource.

```sql
/*+ update */
UPDATE google.migrationcenter.import_jobs
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
completeTime = '{{ completeTime }}',
state = '{{ state }}',
labels = '{{ labels }}',
assetSource = '{{ assetSource }}',
validationReport = '{{ validationReport }}',
executionReport = '{{ executionReport }}'
WHERE 
importJobsId = '{{ importJobsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>import_jobs</code> resource.

```sql
/*+ delete */
DELETE FROM google.migrationcenter.import_jobs
WHERE importJobsId = '{{ importJobsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

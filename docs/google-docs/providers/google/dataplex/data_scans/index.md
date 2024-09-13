---
title: data_scans
hide_title: false
hide_table_of_contents: false
keywords:
  - data_scans
  - dataplex
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

Creates, updates, deletes, gets or lists a <code>data_scans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_scans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.data_scans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the scan, of the form: projects/{project}/locations/{location_id}/dataScans/{datascan_id}, where project refers to a project_id or project_number and location_id refers to a GCP region. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the scan. Must be between 1-1024 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the scan was created. |
| <CopyableCode code="data" /> | `object` | The data source for DataScan. |
| <CopyableCode code="dataProfileResult" /> | `object` | DataProfileResult defines the output of DataProfileScan. Each field of the table will have field type specific profile result. |
| <CopyableCode code="dataProfileSpec" /> | `object` | DataProfileScan related setting. |
| <CopyableCode code="dataQualityResult" /> | `object` | The output of a DataQualityScan. |
| <CopyableCode code="dataQualitySpec" /> | `object` | DataQualityScan related setting. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. Must be between 1-256 characters. |
| <CopyableCode code="executionSpec" /> | `object` | DataScan execution settings. |
| <CopyableCode code="executionStatus" /> | `object` | Status of the data scan execution. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the scan. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the DataScan. |
| <CopyableCode code="type" /> | `string` | Output only. The type of DataScan. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the scan. This ID will be different if the scan is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the scan was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_data_scans_get" /> | `SELECT` | <CopyableCode code="dataScansId, locationsId, projectsId" /> | Gets a DataScan resource. |
| <CopyableCode code="projects_locations_data_scans_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists DataScans. |
| <CopyableCode code="projects_locations_data_scans_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a DataScan resource. |
| <CopyableCode code="projects_locations_data_scans_delete" /> | `DELETE` | <CopyableCode code="dataScansId, locationsId, projectsId" /> | Deletes a DataScan resource. |
| <CopyableCode code="projects_locations_data_scans_patch" /> | `UPDATE` | <CopyableCode code="dataScansId, locationsId, projectsId" /> | Updates a DataScan resource. |
| <CopyableCode code="projects_locations_data_scans_generate_data_quality_rules" /> | `EXEC` | <CopyableCode code="dataScansId, locationsId, projectsId" /> | Generates recommended data quality rules based on the results of a data profiling scan.Use the recommendations to build rules for a data quality scan. |
| <CopyableCode code="projects_locations_data_scans_run" /> | `EXEC` | <CopyableCode code="dataScansId, locationsId, projectsId" /> | Runs an on-demand execution of a DataScan |

## `SELECT` examples

Lists DataScans.

```sql
SELECT
name,
description,
createTime,
data,
dataProfileResult,
dataProfileSpec,
dataQualityResult,
dataQualitySpec,
displayName,
executionSpec,
executionStatus,
labels,
state,
type,
uid,
updateTime
FROM google.dataplex.data_scans
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_scans</code> resource.

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
INSERT INTO google.dataplex.data_scans (
locationsId,
projectsId,
name,
uid,
description,
displayName,
labels,
state,
createTime,
updateTime,
data,
executionSpec,
executionStatus,
type,
dataQualitySpec,
dataProfileSpec,
dataQualityResult,
dataProfileResult
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ uid }}',
'{{ description }}',
'{{ displayName }}',
'{{ labels }}',
'{{ state }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ data }}',
'{{ executionSpec }}',
'{{ executionStatus }}',
'{{ type }}',
'{{ dataQualitySpec }}',
'{{ dataProfileSpec }}',
'{{ dataQualityResult }}',
'{{ dataProfileResult }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: uid
        value: '{{ uid }}'
      - name: description
        value: '{{ description }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: labels
        value: '{{ labels }}'
      - name: state
        value: '{{ state }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: data
        value: '{{ data }}'
      - name: executionSpec
        value: '{{ executionSpec }}'
      - name: executionStatus
        value: '{{ executionStatus }}'
      - name: type
        value: '{{ type }}'
      - name: dataQualitySpec
        value: '{{ dataQualitySpec }}'
      - name: dataProfileSpec
        value: '{{ dataProfileSpec }}'
      - name: dataQualityResult
        value: '{{ dataQualityResult }}'
      - name: dataProfileResult
        value: '{{ dataProfileResult }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>data_scans</code> resource.

```sql
/*+ update */
UPDATE google.dataplex.data_scans
SET 
name = '{{ name }}',
uid = '{{ uid }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
labels = '{{ labels }}',
state = '{{ state }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
data = '{{ data }}',
executionSpec = '{{ executionSpec }}',
executionStatus = '{{ executionStatus }}',
type = '{{ type }}',
dataQualitySpec = '{{ dataQualitySpec }}',
dataProfileSpec = '{{ dataProfileSpec }}',
dataQualityResult = '{{ dataQualityResult }}',
dataProfileResult = '{{ dataProfileResult }}'
WHERE 
dataScansId = '{{ dataScansId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>data_scans</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataplex.data_scans
WHERE dataScansId = '{{ dataScansId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

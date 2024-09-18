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
description,
displayName,
labels,
data,
executionSpec,
dataQualitySpec,
dataProfileSpec
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ description }}',
'{{ displayName }}',
'{{ labels }}',
'{{ data }}',
'{{ executionSpec }}',
'{{ dataQualitySpec }}',
'{{ dataProfileSpec }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
uid: string
description: string
displayName: string
labels: object
state: string
createTime: string
updateTime: string
data:
  entity: string
  resource: string
executionSpec:
  trigger:
    onDemand: {}
    schedule:
      cron: string
  field: string
executionStatus:
  latestJobStartTime: string
  latestJobEndTime: string
  latestJobCreateTime: string
type: string
dataQualitySpec:
  rules:
    - rangeExpectation:
        minValue: string
        maxValue: string
        strictMinEnabled: boolean
        strictMaxEnabled: boolean
      nonNullExpectation: {}
      setExpectation:
        values:
          - type: string
      regexExpectation:
        regex: string
      uniquenessExpectation: {}
      statisticRangeExpectation:
        statistic: string
        minValue: string
        maxValue: string
        strictMinEnabled: boolean
        strictMaxEnabled: boolean
      rowConditionExpectation:
        sqlExpression: string
      tableConditionExpectation:
        sqlExpression: string
      sqlAssertion:
        sqlStatement: string
      column: string
      ignoreNull: boolean
      dimension: string
      threshold: number
      name: string
      description: string
      suspended: boolean
  samplingPercent: number
  rowFilter: string
  postScanActions:
    bigqueryExport:
      resultsTable: string
    notificationReport:
      recipients:
        emails:
          - type: string
      scoreThresholdTrigger:
        scoreThreshold: number
      jobFailureTrigger: {}
      jobEndTrigger: {}
dataProfileSpec:
  samplingPercent: number
  rowFilter: string
  postScanActions:
    bigqueryExport:
      resultsTable: string
  includeFields:
    fieldNames:
      - type: string
dataQualityResult:
  passed: boolean
  score: number
  dimensions:
    - dimension:
        name: string
      passed: boolean
      score: number
  columns:
    - column: string
      score: number
  rules:
    - rule:
        column: string
        ignoreNull: boolean
        dimension: string
        threshold: number
        name: string
        description: string
        suspended: boolean
      passed: boolean
      evaluatedCount: string
      passedCount: string
      nullCount: string
      passRatio: number
      failingRowsQuery: string
      assertionRowCount: string
  rowCount: string
  scannedData:
    incrementalField:
      field: string
      start: string
      end: string
  postScanActionsResult:
    bigqueryExportResult:
      state: string
      message: string
dataProfileResult:
  rowCount: string
  profile:
    fields:
      - name: string
        type: string
        mode: string
        profile:
          nullRatio: number
          distinctRatio: number
          topNValues:
            - value: string
              count: string
              ratio: number
          stringProfile:
            minLength: string
            maxLength: string
            averageLength: number
          integerProfile:
            average: number
            standardDeviation: number
            min: string
            quartiles:
              - type: string
                format: string
            max: string
          doubleProfile:
            average: number
            standardDeviation: number
            min: number
            quartiles:
              - type: string
                format: string
            max: number
  postScanActionsResult:
    bigqueryExportResult:
      state: string
      message: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>data_scans</code> resource.

```sql
/*+ update */
UPDATE google.dataplex.data_scans
SET 
description = '{{ description }}',
displayName = '{{ displayName }}',
labels = '{{ labels }}',
data = '{{ data }}',
executionSpec = '{{ executionSpec }}',
dataQualitySpec = '{{ dataQualitySpec }}',
dataProfileSpec = '{{ dataProfileSpec }}'
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

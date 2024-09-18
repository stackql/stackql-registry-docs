---
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
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

Creates, updates, deletes, gets or lists a <code>reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.migrationcenter.reports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of resource. |
| <CopyableCode code="description" /> | `string` | Free-text description. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation timestamp. |
| <CopyableCode code="displayName" /> | `string` | User-friendly display name. Maximum length is 63 characters. |
| <CopyableCode code="state" /> | `string` | Report creation state. |
| <CopyableCode code="summary" /> | `object` | Describes the Summary view of a Report, which contains aggregated values for all the groups and preference sets included in this Report. |
| <CopyableCode code="type" /> | `string` | Report type. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update timestamp. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, reportConfigsId, reportsId" /> | Gets details of a single Report. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, reportConfigsId" /> | Lists Reports in a given ReportConfig. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, reportConfigsId" /> | Creates a report. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, reportConfigsId, reportsId" /> | Deletes a Report. |

## `SELECT` examples

Lists Reports in a given ReportConfig.

```sql
SELECT
name,
description,
createTime,
displayName,
state,
summary,
type,
updateTime
FROM google.migrationcenter.reports
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND reportConfigsId = '{{ reportConfigsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>reports</code> resource.

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
INSERT INTO google.migrationcenter.reports (
locationsId,
projectsId,
reportConfigsId,
displayName,
description,
type,
state
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ reportConfigsId }}',
'{{ displayName }}',
'{{ description }}',
'{{ type }}',
'{{ state }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
createTime: string
updateTime: string
displayName: string
description: string
type: string
state: string
summary:
  allAssetsStats:
    totalMemoryBytes: string
    totalStorageBytes: string
    totalCores: string
    totalAssets: string
    memoryUtilizationChart:
      used: string
      free: string
    operatingSystem:
      dataPoints:
        - label: string
          value: number
    coreCountHistogram:
      buckets:
        - lowerBound: string
          upperBound: string
          count: string
  groupFindings:
    - displayName: string
      description: string
      overlappingAssetCount: string
      preferenceSetFindings:
        - displayName: string
          description: string
          machinePreferences:
            targetProduct: string
            regionPreferences:
              preferredRegions:
                - type: string
            commitmentPlan: string
            sizingOptimizationStrategy: string
            computeEnginePreferences:
              persistentDiskType: string
              machinePreferences:
                allowedMachineSeries:
                  - code: string
              licenseType: string
            vmwareEnginePreferences:
              cpuOvercommitRatio: number
              memoryOvercommitRatio: number
              storageDeduplicationCompressionRatio: number
              commitmentPlan: string
            soleTenancyPreferences:
              cpuOvercommitRatio: number
              hostMaintenancePolicy: string
              commitmentPlan: string
              nodeTypes:
                - nodeName: string
          monthlyCostTotal:
            currencyCode: string
            units: string
            nanos: integer
          computeEngineFinding:
            allocatedRegions:
              - type: string
            allocatedAssetCount: string
            machineSeriesAllocations:
              - machineSeries:
                  code: string
                allocatedAssetCount: string
            allocatedDiskTypes:
              - type: string
                enumDescriptions: string
                enum: string
          vmwareEngineFinding:
            allocatedRegions:
              - type: string
            allocatedAssetCount: string
            nodeAllocations:
              - vmwareNode:
                  code: string
                nodeCount: string
                allocatedAssetCount: string
          soleTenantFinding:
            allocatedRegions:
              - type: string
            allocatedAssetCount: string
            nodeAllocations:
              - node:
                  nodeName: string
                nodeCount: string
                allocatedAssetCount: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>reports</code> resource.

```sql
/*+ delete */
DELETE FROM google.migrationcenter.reports
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND reportConfigsId = '{{ reportConfigsId }}'
AND reportsId = '{{ reportsId }}';
```

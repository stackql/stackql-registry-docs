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
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: displayName
      value: string
    - name: description
      value: string
    - name: type
      value: string
    - name: state
      value: string
    - name: summary
      value:
        - name: allAssetsStats
          value:
            - name: totalMemoryBytes
              value: string
            - name: totalStorageBytes
              value: string
            - name: totalCores
              value: string
            - name: totalAssets
              value: string
            - name: memoryUtilizationChart
              value:
                - name: used
                  value: string
                - name: free
                  value: string
            - name: operatingSystem
              value:
                - name: dataPoints
                  value:
                    - - name: label
                        value: string
                      - name: value
                        value: number
            - name: coreCountHistogram
              value:
                - name: buckets
                  value:
                    - - name: lowerBound
                        value: string
                      - name: upperBound
                        value: string
                      - name: count
                        value: string
        - name: groupFindings
          value:
            - - name: displayName
                value: string
              - name: description
                value: string
              - name: overlappingAssetCount
                value: string
              - name: preferenceSetFindings
                value:
                  - - name: displayName
                      value: string
                    - name: description
                      value: string
                    - name: machinePreferences
                      value:
                        - name: targetProduct
                          value: string
                        - name: regionPreferences
                          value:
                            - name: preferredRegions
                              value:
                                - string
                        - name: commitmentPlan
                          value: string
                        - name: sizingOptimizationStrategy
                          value: string
                        - name: computeEnginePreferences
                          value:
                            - name: persistentDiskType
                              value: string
                            - name: machinePreferences
                              value:
                                - name: allowedMachineSeries
                                  value:
                                    - - name: code
                                        value: string
                            - name: licenseType
                              value: string
                        - name: vmwareEnginePreferences
                          value:
                            - name: cpuOvercommitRatio
                              value: number
                            - name: memoryOvercommitRatio
                              value: number
                            - name: storageDeduplicationCompressionRatio
                              value: number
                            - name: commitmentPlan
                              value: string
                        - name: soleTenancyPreferences
                          value:
                            - name: cpuOvercommitRatio
                              value: number
                            - name: hostMaintenancePolicy
                              value: string
                            - name: commitmentPlan
                              value: string
                            - name: nodeTypes
                              value:
                                - - name: nodeName
                                    value: string
                    - name: monthlyCostTotal
                      value:
                        - name: currencyCode
                          value: string
                        - name: units
                          value: string
                        - name: nanos
                          value: integer
                    - name: computeEngineFinding
                      value:
                        - name: allocatedRegions
                          value:
                            - string
                        - name: allocatedAssetCount
                          value: string
                        - name: machineSeriesAllocations
                          value:
                            - - name: machineSeries
                                value:
                                  - name: code
                                    value: string
                              - name: allocatedAssetCount
                                value: string
                        - name: allocatedDiskTypes
                          value:
                            - string
                    - name: vmwareEngineFinding
                      value:
                        - name: allocatedRegions
                          value:
                            - string
                        - name: allocatedAssetCount
                          value: string
                        - name: nodeAllocations
                          value:
                            - - name: vmwareNode
                                value:
                                  - name: code
                                    value: string
                              - name: nodeCount
                                value: string
                              - name: allocatedAssetCount
                                value: string
                    - name: soleTenantFinding
                      value:
                        - name: allocatedRegions
                          value:
                            - string
                        - name: allocatedAssetCount
                          value: string
                        - name: nodeAllocations
                          value:
                            - - name: node
                                value:
                                  - name: nodeName
                                    value: string
                              - name: nodeCount
                                value: string
                              - name: allocatedAssetCount
                                value: string

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

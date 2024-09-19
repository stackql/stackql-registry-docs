---
title: collectd_time_series
hide_title: false
hide_table_of_contents: false
keywords:
  - collectd_time_series
  - monitoring
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

Creates, updates, deletes, gets or lists a <code>collectd_time_series</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collectd_time_series</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.monitoring.collectd_time_series" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_collectd_time_series_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Cloud Monitoring Agent only: Creates a new time series.This method is only for use by the Cloud Monitoring Agent. Use projects.timeSeries.create instead. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>collectd_time_series</code> resource.

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
INSERT INTO google.monitoring.collectd_time_series (
projectsId,
resource,
collectdVersion,
collectdPayloads
)
SELECT 
'{{ projectsId }}',
'{{ resource }}',
'{{ collectdVersion }}',
'{{ collectdPayloads }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: resource
      value:
        - name: type
          value: string
        - name: labels
          value: object
    - name: collectdVersion
      value: string
    - name: collectdPayloads
      value:
        - - name: values
            value:
              - - name: dataSourceName
                  value: string
                - name: dataSourceType
                  value: string
                - name: value
                  value:
                    - name: boolValue
                      value: boolean
                    - name: int64Value
                      value: string
                    - name: doubleValue
                      value: number
                    - name: stringValue
                      value: string
                    - name: distributionValue
                      value:
                        - name: count
                          value: string
                        - name: mean
                          value: number
                        - name: sumOfSquaredDeviation
                          value: number
                        - name: range
                          value:
                            - name: min
                              value: number
                            - name: max
                              value: number
                        - name: bucketOptions
                          value:
                            - name: linearBuckets
                              value:
                                - name: numFiniteBuckets
                                  value: integer
                                - name: width
                                  value: number
                                - name: offset
                                  value: number
                            - name: exponentialBuckets
                              value:
                                - name: numFiniteBuckets
                                  value: integer
                                - name: growthFactor
                                  value: number
                                - name: scale
                                  value: number
                            - name: explicitBuckets
                              value:
                                - name: bounds
                                  value:
                                    - number
                        - name: bucketCounts
                          value:
                            - string
                        - name: exemplars
                          value:
                            - - name: value
                                value: number
                              - name: timestamp
                                value: string
                              - name: attachments
                                value:
                                  - object
          - name: startTime
            value: string
          - name: endTime
            value: string
          - name: plugin
            value: string
          - name: pluginInstance
            value: string
          - name: type
            value: string
          - name: typeInstance
            value: string
          - name: metadata
            value: object

```
</TabItem>
</Tabs>

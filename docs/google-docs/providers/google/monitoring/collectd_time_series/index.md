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
resource:
  type: string
  labels: object
collectdVersion: string
collectdPayloads:
  - values:
      - dataSourceName: string
        dataSourceType: string
        value:
          boolValue: boolean
          int64Value: string
          doubleValue: number
          stringValue: string
          distributionValue:
            count: string
            mean: number
            sumOfSquaredDeviation: number
            range:
              min: number
              max: number
            bucketOptions:
              linearBuckets:
                numFiniteBuckets: integer
                width: number
                offset: number
              exponentialBuckets:
                numFiniteBuckets: integer
                growthFactor: number
                scale: number
              explicitBuckets:
                bounds:
                  - type: string
                    format: string
            bucketCounts:
              - type: string
                format: string
            exemplars:
              - value: number
                timestamp: string
                attachments:
                  - type: string
                    additionalProperties: any
    startTime: string
    endTime: string
    plugin: string
    pluginInstance: string
    type: string
    typeInstance: string
    metadata: object

```
</TabItem>
</Tabs>

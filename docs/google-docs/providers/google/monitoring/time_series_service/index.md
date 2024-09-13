---
title: time_series_service
hide_title: false
hide_table_of_contents: false
keywords:
  - time_series_service
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

Creates, updates, deletes, gets or lists a <code>time_series_service</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>time_series_service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.monitoring.time_series_service" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_time_series_create_service" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates or adds data to one or more service time series. A service time series is a time series for a metric from a Google Cloud service. The response is empty if all time series in the request were written. If any time series could not be written, a corresponding failure message is included in the error response. This endpoint rejects writes to user-defined metrics. This method is only for use by Google Cloud services. Use projects.timeSeries.create instead. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>time_series_service</code> resource.

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
INSERT INTO google.monitoring.time_series_service (
projectsId,
timeSeries
)
SELECT 
'{{ projectsId }}',
'{{ timeSeries }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: timeSeries
        value: '{{ timeSeries }}'

```
</TabItem>
</Tabs>

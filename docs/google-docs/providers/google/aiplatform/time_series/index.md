---
title: time_series
hide_title: false
hide_table_of_contents: false
keywords:
  - time_series
  - aiplatform
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

Creates, updates, deletes, gets or lists a <code>time_series</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>time_series</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.time_series" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the TensorboardTimeSeries. |
| <CopyableCode code="description" /> | `string` | Description of this TensorboardTimeSeries. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this TensorboardTimeSeries was created. |
| <CopyableCode code="displayName" /> | `string` | Required. User provided name of this TensorboardTimeSeries. This value should be unique among all TensorboardTimeSeries resources belonging to the same TensorboardRun resource (parent resource). |
| <CopyableCode code="etag" /> | `string` | Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="metadata" /> | `object` | Describes metadata for a TensorboardTimeSeries. |
| <CopyableCode code="pluginData" /> | `string` | Data of the current plugin, with the size limited to 65KB. |
| <CopyableCode code="pluginName" /> | `string` | Immutable. Name of the plugin this time series pertain to. Such as Scalar, Tensor, Blob |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this TensorboardTimeSeries was last updated. |
| <CopyableCode code="valueType" /> | `string` | Required. Immutable. Type of TensorboardTimeSeries value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="experimentsId, locationsId, projectsId, runsId, tensorboardsId, timeSeriesId" /> | Gets a TensorboardTimeSeries. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="experimentsId, locationsId, projectsId, runsId, tensorboardsId" /> | Lists TensorboardTimeSeries in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="experimentsId, locationsId, projectsId, runsId, tensorboardsId" /> | Creates a TensorboardTimeSeries. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="experimentsId, locationsId, projectsId, runsId, tensorboardsId, timeSeriesId" /> | Deletes a TensorboardTimeSeries. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="experimentsId, locationsId, projectsId, runsId, tensorboardsId, timeSeriesId" /> | Updates a TensorboardTimeSeries. |
| <CopyableCode code="export_tensorboard_time_series" /> | `EXEC` | <CopyableCode code="experimentsId, locationsId, projectsId, runsId, tensorboardsId, timeSeriesId" /> | Exports a TensorboardTimeSeries' data. Data is returned in paginated responses. |
| <CopyableCode code="read" /> | `EXEC` | <CopyableCode code="experimentsId, locationsId, projectsId, runsId, tensorboardsId, timeSeriesId" /> | Reads a TensorboardTimeSeries' data. By default, if the number of data points stored is less than 1000, all data is returned. Otherwise, 1000 data points is randomly selected from this time series and returned. This value can be changed by changing max_data_points, which can't be greater than 10k. |
| <CopyableCode code="read_blob_data" /> | `EXEC` | <CopyableCode code="experimentsId, locationsId, projectsId, runsId, tensorboardsId, timeSeriesId" /> | Gets bytes of TensorboardBlobs. This is to allow reading blob data stored in consumer project's Cloud Storage bucket without users having to obtain Cloud Storage access permission. |

## `SELECT` examples

Lists TensorboardTimeSeries in a Location.

```sql
SELECT
name,
description,
createTime,
displayName,
etag,
metadata,
pluginData,
pluginName,
updateTime,
valueType
FROM google.aiplatform.time_series
WHERE experimentsId = '{{ experimentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND runsId = '{{ runsId }}'
AND tensorboardsId = '{{ tensorboardsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>time_series</code> resource.

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
INSERT INTO google.aiplatform.time_series (
experimentsId,
locationsId,
projectsId,
runsId,
tensorboardsId,
description,
pluginName,
pluginData,
valueType,
etag,
displayName
)
SELECT 
'{{ experimentsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ runsId }}',
'{{ tensorboardsId }}',
'{{ description }}',
'{{ pluginName }}',
'{{ pluginData }}',
'{{ valueType }}',
'{{ etag }}',
'{{ displayName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: description
      value: '{{ description }}'
    - name: pluginName
      value: '{{ pluginName }}'
    - name: pluginData
      value: '{{ pluginData }}'
    - name: valueType
      value: '{{ valueType }}'
    - name: etag
      value: '{{ etag }}'
    - name: displayName
      value: '{{ displayName }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>time_series</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.time_series
SET 
description = '{{ description }}',
pluginName = '{{ pluginName }}',
pluginData = '{{ pluginData }}',
valueType = '{{ valueType }}',
etag = '{{ etag }}',
displayName = '{{ displayName }}'
WHERE 
experimentsId = '{{ experimentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND runsId = '{{ runsId }}'
AND tensorboardsId = '{{ tensorboardsId }}'
AND timeSeriesId = '{{ timeSeriesId }}';
```

## `DELETE` example

Deletes the specified <code>time_series</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.time_series
WHERE experimentsId = '{{ experimentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND runsId = '{{ runsId }}'
AND tensorboardsId = '{{ tensorboardsId }}'
AND timeSeriesId = '{{ timeSeriesId }}';
```

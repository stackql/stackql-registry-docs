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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>time_series</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.time_series</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the TensorboardTimeSeries. |
| `description` | `string` | Description of this TensorboardTimeSeries. |
| `pluginName` | `string` | Immutable. Name of the plugin this time series pertain to. Such as Scalar, Tensor, Blob |
| `etag` | `string` | Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| `displayName` | `string` | Required. User provided name of this TensorboardTimeSeries. This value should be unique among all TensorboardTimeSeries resources belonging to the same TensorboardRun resource (parent resource). |
| `metadata` | `object` | Describes metadata for a TensorboardTimeSeries. |
| `pluginData` | `string` | Data of the current plugin, with the size limited to 65KB. |
| `updateTime` | `string` | Output only. Timestamp when this TensorboardTimeSeries was last updated. |
| `valueType` | `string` | Required. Immutable. Type of TensorboardTimeSeries value. |
| `createTime` | `string` | Output only. Timestamp when this TensorboardTimeSeries was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `experimentsId, locationsId, projectsId, runsId, tensorboardsId, timeSeriesId` | Gets a TensorboardTimeSeries. |
| `list` | `SELECT` | `experimentsId, locationsId, projectsId, runsId, tensorboardsId` | Lists TensorboardTimeSeries in a Location. |
| `create` | `INSERT` | `experimentsId, locationsId, projectsId, runsId, tensorboardsId` | Creates a TensorboardTimeSeries. |
| `delete` | `DELETE` | `experimentsId, locationsId, projectsId, runsId, tensorboardsId, timeSeriesId` | Deletes a TensorboardTimeSeries. |
| `_list` | `EXEC` | `experimentsId, locationsId, projectsId, runsId, tensorboardsId` | Lists TensorboardTimeSeries in a Location. |
| `batch_create` | `EXEC` | `experimentsId, locationsId, projectsId, runsId, tensorboardsId` | Batch create TensorboardTimeSeries that belong to a TensorboardExperiment. |
| `batch_read` | `EXEC` | `experimentsId, locationsId, projectsId, runsId, tensorboardsId` | Reads multiple TensorboardTimeSeries' data. The data point number limit is 1000 for scalars, 100 for tensors and blob references. If the number of data points stored is less than the limit, all data is returned. Otherwise, the number limit of data points is randomly selected from this time series and returned. |
| `export_tensorboard_time_series` | `EXEC` | `experimentsId, locationsId, projectsId, runsId, tensorboardsId, timeSeriesId` | Exports a TensorboardTimeSeries' data. Data is returned in paginated responses. |
| `patch` | `EXEC` | `experimentsId, locationsId, projectsId, runsId, tensorboardsId, timeSeriesId` | Updates a TensorboardTimeSeries. |
| `read` | `EXEC` | `experimentsId, locationsId, projectsId, runsId, tensorboardsId, timeSeriesId` | Reads a TensorboardTimeSeries' data. By default, if the number of data points stored is less than 1000, all data is returned. Otherwise, 1000 data points is randomly selected from this time series and returned. This value can be changed by changing max_data_points, which can't be greater than 10k. |
| `read_blob_data` | `EXEC` | `experimentsId, locationsId, projectsId, runsId, tensorboardsId, timeSeriesId` | Gets bytes of TensorboardBlobs. This is to allow reading blob data stored in consumer project's Cloud Storage bucket without users having to obtain Cloud Storage access permission. |

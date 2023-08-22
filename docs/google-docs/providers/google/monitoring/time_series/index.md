---
title: time_series
hide_title: false
hide_table_of_contents: false
keywords:
  - time_series
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>time_series</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.monitoring.time_series</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unit` | `string` | The units in which the metric value is reported. It is only applicable if the value_type is INT64, DOUBLE, or DISTRIBUTION. The unit defines the representation of the stored metric values. |
| `valueType` | `string` | The value type of the time series. When listing time series, this value type might be different from the value type of the associated metric if this time series is an alignment or reduction of other time series.When creating a time series, this field is optional. If present, it must be the same as the type of the data in the points field. |
| `metadata` | `object` | Auxiliary metadata for a MonitoredResource object. MonitoredResource objects contain the minimum set of information to uniquely identify a monitored resource instance. There is some other useful auxiliary metadata. Monitoring and Logging use an ingestion pipeline to extract metadata for cloud resources of all types, and store the metadata in this message. |
| `metric` | `object` | A specific metric, identified by specifying values for all of the labels of a MetricDescriptor. |
| `metricKind` | `string` | The metric kind of the time series. When listing time series, this metric kind might be different from the metric kind of the associated metric if this time series is an alignment or reduction of other time series.When creating a time series, this field is optional. If present, it must be the same as the metric kind of the associated metric. If the associated metric's descriptor must be auto-created, then this field specifies the metric kind of the new descriptor and must be either GAUGE (the default) or CUMULATIVE. |
| `points` | `array` | The data points of this time series. When listing time series, points are returned in reverse time order.When creating a time series, this field must contain exactly one point and the point's type must be the same as the value type of the associated metric. If the associated metric's descriptor must be auto-created, then the value type of the descriptor is determined by the point's type, which must be BOOL, INT64, DOUBLE, or DISTRIBUTION. |
| `resource` | `object` | An object representing a resource that can be used for monitoring, logging, billing, or other purposes. Examples include virtual machine instances, databases, and storage devices such as disks. The type field identifies a MonitoredResourceDescriptor object that describes the resource's schema. Information in the labels field identifies the actual resource and its attributes according to the schema. For example, a particular Compute Engine VM instance could be represented by the following object, because the MonitoredResourceDescriptor for "gce_instance" has labels "project_id", "instance_id" and "zone": &#123; "type": "gce_instance", "labels": &#123; "project_id": "my-project", "instance_id": "12345678901234", "zone": "us-central1-a" &#125;&#125;  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_time_series_list` | `SELECT` | `foldersId` | Lists time series that match a filter. |
| `organizations_time_series_list` | `SELECT` | `organizationsId` | Lists time series that match a filter. |
| `projects_time_series_list` | `SELECT` | `projectsId` | Lists time series that match a filter. |
| `projects_time_series_create` | `INSERT` | `projectsId` | Creates or adds data to one or more time series. The response is empty if all time series in the request were written. If any time series could not be written, a corresponding failure message is included in the error response. |
| `_folders_time_series_list` | `EXEC` | `foldersId` | Lists time series that match a filter. |
| `_organizations_time_series_list` | `EXEC` | `organizationsId` | Lists time series that match a filter. |
| `_projects_time_series_list` | `EXEC` | `projectsId` | Lists time series that match a filter. |
| `projects_time_series_query` | `EXEC` | `projectsId` | Queries time series using Monitoring Query Language. |

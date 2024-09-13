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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>time_series</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>time_series</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.monitoring.time_series" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | Input only. A detailed description of the time series that will be associated with the google.api.MetricDescriptor for the metric. Once set, this field cannot be changed through CreateTimeSeries. |
| <CopyableCode code="metadata" /> | `object` | Auxiliary metadata for a MonitoredResource object. MonitoredResource objects contain the minimum set of information to uniquely identify a monitored resource instance. There is some other useful auxiliary metadata. Monitoring and Logging use an ingestion pipeline to extract metadata for cloud resources of all types, and store the metadata in this message. |
| <CopyableCode code="metric" /> | `object` | A specific metric, identified by specifying values for all of the labels of a MetricDescriptor. |
| <CopyableCode code="metricKind" /> | `string` | The metric kind of the time series. When listing time series, this metric kind might be different from the metric kind of the associated metric if this time series is an alignment or reduction of other time series.When creating a time series, this field is optional. If present, it must be the same as the metric kind of the associated metric. If the associated metric's descriptor must be auto-created, then this field specifies the metric kind of the new descriptor and must be either GAUGE (the default) or CUMULATIVE. |
| <CopyableCode code="points" /> | `array` | The data points of this time series. When listing time series, points are returned in reverse time order.When creating a time series, this field must contain exactly one point and the point's type must be the same as the value type of the associated metric. If the associated metric's descriptor must be auto-created, then the value type of the descriptor is determined by the point's type, which must be BOOL, INT64, DOUBLE, or DISTRIBUTION. |
| <CopyableCode code="resource" /> | `object` | An object representing a resource that can be used for monitoring, logging, billing, or other purposes. Examples include virtual machine instances, databases, and storage devices such as disks. The type field identifies a MonitoredResourceDescriptor object that describes the resource's schema. Information in the labels field identifies the actual resource and its attributes according to the schema. For example, a particular Compute Engine VM instance could be represented by the following object, because the MonitoredResourceDescriptor for "gce_instance" has labels "project_id", "instance_id" and "zone": { "type": "gce_instance", "labels": { "project_id": "my-project", "instance_id": "12345678901234", "zone": "us-central1-a" }}  |
| <CopyableCode code="unit" /> | `string` | The units in which the metric value is reported. It is only applicable if the value_type is INT64, DOUBLE, or DISTRIBUTION. The unit defines the representation of the stored metric values. This field can only be changed through CreateTimeSeries when it is empty. |
| <CopyableCode code="valueType" /> | `string` | The value type of the time series. When listing time series, this value type might be different from the value type of the associated metric if this time series is an alignment or reduction of other time series.When creating a time series, this field is optional. If present, it must be the same as the type of the data in the points field. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_time_series_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Lists time series that match a filter. |
| <CopyableCode code="organizations_time_series_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists time series that match a filter. |
| <CopyableCode code="projects_time_series_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists time series that match a filter. |
| <CopyableCode code="projects_time_series_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates or adds data to one or more time series. The response is empty if all time series in the request were written. If any time series could not be written, a corresponding failure message is included in the error response. This method does not support resource locations constraint of an organization policy (https://cloud.google.com/resource-manager/docs/organization-policy/defining-locations#setting_the_organization_policy). |
| <CopyableCode code="projects_time_series_query" /> | `EXEC` | <CopyableCode code="projectsId" /> | Queries time series by using Monitoring Query Language (MQL). We recommend using PromQL instead of MQL. For more information about the status of MQL, see the MQL deprecation notice (https://cloud.google.com/stackdriver/docs/deprecations/mql). |

## `SELECT` examples

Lists time series that match a filter.

```sql
SELECT
description,
metadata,
metric,
metricKind,
points,
resource,
unit,
valueType
FROM google.monitoring.time_series
WHERE foldersId = '{{ foldersId }}'; 
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
INSERT INTO google.monitoring.time_series (
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

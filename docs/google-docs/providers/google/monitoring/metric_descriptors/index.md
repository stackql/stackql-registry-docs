---
title: metric_descriptors
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_descriptors
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
<tr><td><b>Name</b></td><td><code>metric_descriptors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.monitoring.metric_descriptors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as page_token in the next call to this method. |
| `metricDescriptors` | `array` | The metric descriptors that are available to the project and that match the value of filter, if present. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_metric_descriptors_get` | `SELECT` | `metricDescriptorsId, projectsId` | Gets a single metric descriptor. |
| `projects_metric_descriptors_list` | `SELECT` | `projectsId` | Lists metric descriptors that match a filter. |
| `projects_metric_descriptors_create` | `INSERT` | `projectsId` | Creates a new metric descriptor. The creation is executed asynchronously. User-created metric descriptors define custom metrics (https://cloud.google.com/monitoring/custom-metrics). The metric descriptor is updated if it already exists, except that metric labels are never removed. |
| `projects_metric_descriptors_delete` | `DELETE` | `metricDescriptorsId, projectsId` | Deletes a metric descriptor. Only user-created custom metrics (https://cloud.google.com/monitoring/custom-metrics) can be deleted. |

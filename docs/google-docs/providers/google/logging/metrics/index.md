---
title: metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics
  - logging
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
<tr><td><b>Name</b></td><td><code>metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.logging.metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `metrics` | `array` | A list of logs-based metrics. |
| `nextPageToken` | `string` | If there might be more results than appear in this response, then nextPageToken is included. To get the next set of results, call this method again using the value of nextPageToken as pageToken. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_metrics_list` | `SELECT` | `projectsId` | Lists logs-based metrics. |
| `projects_metrics_create` | `INSERT` | `projectsId` | Creates a logs-based metric. |
| `projects_metrics_delete` | `DELETE` | `metricsId, projectsId` | Deletes a logs-based metric. |
| `projects_metrics_get` | `EXEC` | `metricsId, projectsId` | Gets a logs-based metric. |
| `projects_metrics_update` | `EXEC` | `metricsId, projectsId` | Creates or updates a logs-based metric. |

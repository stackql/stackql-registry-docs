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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `nextPageToken` | `string` | If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as page_token in the next call to this method. |
| `timeSeries` | `array` | One or more time series that match the filter included in the request. |
| `unit` | `string` | The unit in which all time_series point values are reported. unit follows the UCUM format for units as seen in https://unitsofmeasure.org/ucum.html. If different time_series have different units (for example, because they come from different metric types, or a unit is absent), then unit will be "{not_a_unit}". |
| `executionErrors` | `array` | Query execution errors that may have caused the time series data returned to be incomplete. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_timeSeries_list` | `SELECT` | `foldersId` | Lists time series that match a filter. |
| `organizations_timeSeries_list` | `SELECT` | `organizationsId` | Lists time series that match a filter. |
| `projects_timeSeries_list` | `SELECT` | `projectsId` | Lists time series that match a filter. |
| `projects_timeSeries_create` | `INSERT` | `projectsId` | Creates or adds data to one or more time series. The response is empty if all time series in the request were written. If any time series could not be written, a corresponding failure message is included in the error response. |
| `projects_timeSeries_query` | `EXEC` | `projectsId` | Queries time series using Monitoring Query Language. |

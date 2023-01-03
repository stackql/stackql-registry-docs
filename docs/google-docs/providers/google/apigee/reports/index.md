---
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
  - apigee
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
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.reports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Unique identifier for the report T his is a legacy field used to encode custom report unique id |
| `toTime` | `string` | Legacy field: not used. Contains the end time for the report |
| `fromTime` | `string` | Legacy field: not used. Contains the from time for the report |
| `organization` | `string` | Output only. Organization name |
| `dimensions` | `array` | This contains the list of dimensions for the report |
| `tags` | `array` | Legacy field: not used. This field contains a list of tags associated with custom report |
| `lastModifiedAt` | `string` | Output only. Modified time of this entity as milliseconds since epoch. json key: lastModifiedAt |
| `sortOrder` | `string` | Legacy field: not used much. Contains the sort order for the sort columns |
| `offset` | `string` | Legacy field: not used. This field contains the offset for the data |
| `displayName` | `string` | This is the display name for the report |
| `chartType` | `string` | This field contains the chart type for the report |
| `lastViewedAt` | `string` | Output only. Last viewed time of this entity as milliseconds since epoch |
| `createdAt` | `string` | Output only. Unix time when the app was created json key: createdAt |
| `metrics` | `array` | Required. This contains the list of metrics |
| `topk` | `string` | Legacy field: not used. This field contains the top k parameter value for restricting the result |
| `comments` | `array` | Legacy field: not used. This field contains a list of comments associated with custom report |
| `sortByCols` | `array` | Legacy field: not used much. Contains the list of sort by columns |
| `timeUnit` | `string` | This field contains the time unit of aggregation for the report |
| `environment` | `string` | Output only. Environment name |
| `properties` | `array` | This field contains report properties such as ui metadata etc. |
| `filter` | `string` | This field contains the filter expression |
| `limit` | `string` | Legacy field: not used This field contains the limit for the result retrieved |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_reports_get` | `SELECT` | `organizationsId, reportsId` | Retrieve a custom report definition. |
| `organizations_reports_list` | `SELECT` | `organizationsId` | Return a list of Custom Reports |
| `organizations_reports_create` | `INSERT` | `organizationsId` | Creates a Custom Report for an Organization. A Custom Report provides Apigee Customers to create custom dashboards in addition to the standard dashboards which are provided. The Custom Report in its simplest form contains specifications about metrics, dimensions and filters. It is important to note that the custom report by itself does not provide an executable entity. The Edge UI converts the custom report definition into an analytics query and displays the result in a chart. |
| `organizations_reports_delete` | `DELETE` | `organizationsId, reportsId` | Deletes an existing custom report definition |
| `organizations_reports_update` | `EXEC` | `organizationsId, reportsId` | Update an existing custom report definition |

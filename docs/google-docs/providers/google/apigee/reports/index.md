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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigee.reports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Unique identifier for the report T his is a legacy field used to encode custom report unique id |
| <CopyableCode code="chartType" /> | `string` | This field contains the chart type for the report |
| <CopyableCode code="comments" /> | `array` | Legacy field: not used. This field contains a list of comments associated with custom report |
| <CopyableCode code="createdAt" /> | `string` | Output only. Unix time when the app was created json key: createdAt |
| <CopyableCode code="dimensions" /> | `array` | This contains the list of dimensions for the report |
| <CopyableCode code="displayName" /> | `string` | This is the display name for the report |
| <CopyableCode code="environment" /> | `string` | Output only. Environment name |
| <CopyableCode code="filter" /> | `string` | This field contains the filter expression |
| <CopyableCode code="fromTime" /> | `string` | Legacy field: not used. Contains the from time for the report |
| <CopyableCode code="lastModifiedAt" /> | `string` | Output only. Modified time of this entity as milliseconds since epoch. json key: lastModifiedAt |
| <CopyableCode code="lastViewedAt" /> | `string` | Output only. Last viewed time of this entity as milliseconds since epoch |
| <CopyableCode code="limit" /> | `string` | Legacy field: not used This field contains the limit for the result retrieved |
| <CopyableCode code="metrics" /> | `array` | Required. This contains the list of metrics |
| <CopyableCode code="offset" /> | `string` | Legacy field: not used. This field contains the offset for the data |
| <CopyableCode code="organization" /> | `string` | Output only. Organization name |
| <CopyableCode code="properties" /> | `array` | This field contains report properties such as ui metadata etc. |
| <CopyableCode code="sortByCols" /> | `array` | Legacy field: not used much. Contains the list of sort by columns |
| <CopyableCode code="sortOrder" /> | `string` | Legacy field: not used much. Contains the sort order for the sort columns |
| <CopyableCode code="tags" /> | `array` | Legacy field: not used. This field contains a list of tags associated with custom report |
| <CopyableCode code="timeUnit" /> | `string` | This field contains the time unit of aggregation for the report |
| <CopyableCode code="toTime" /> | `string` | Legacy field: not used. Contains the end time for the report |
| <CopyableCode code="topk" /> | `string` | Legacy field: not used. This field contains the top k parameter value for restricting the result |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_reports_get" /> | `SELECT` | <CopyableCode code="organizationsId, reportsId" /> | Retrieve a custom report definition. |
| <CopyableCode code="organizations_reports_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Return a list of Custom Reports |
| <CopyableCode code="organizations_reports_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a Custom Report for an Organization. A Custom Report provides Apigee Customers to create custom dashboards in addition to the standard dashboards which are provided. The Custom Report in its simplest form contains specifications about metrics, dimensions and filters. It is important to note that the custom report by itself does not provide an executable entity. The Edge UI converts the custom report definition into an analytics query and displays the result in a chart. |
| <CopyableCode code="organizations_reports_delete" /> | `DELETE` | <CopyableCode code="organizationsId, reportsId" /> | Deletes an existing custom report definition |
| <CopyableCode code="organizations_reports_update" /> | `EXEC` | <CopyableCode code="organizationsId, reportsId" /> | Update an existing custom report definition |

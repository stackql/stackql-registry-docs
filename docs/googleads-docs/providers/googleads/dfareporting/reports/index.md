---
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
  - dfareporting
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.reports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID identifying this report resource. |
| `name` | `string` | The name of the report. |
| `format` | `string` | The output format of the report. If not specified, default format is "CSV". Note that the actual format in the completed report file might differ if for instance the report's size exceeds the format's capabilities. "CSV" will then be the fallback format. |
| `pathAttributionCriteria` | `object` | The report criteria for a report of type "PATH_ATTRIBUTION". |
| `pathToConversionCriteria` | `object` | The report criteria for a report of type "PATH_TO_CONVERSION". |
| `criteria` | `object` | The report criteria for a report of type "STANDARD". |
| `fileName` | `string` | The filename used when generating report files for this report. |
| `crossDimensionReachCriteria` | `object` | The report criteria for a report of type "CROSS_DIMENSION_REACH". |
| `type` | `string` | The type of the report. |
| `schedule` | `object` | The report's schedule. Can only be set if the report's 'dateRange' is a relative date range and the relative date range is not "TODAY". |
| `kind` | `string` | The kind of resource this is, in this case dfareporting#report. |
| `reachCriteria` | `object` | The report criteria for a report of type "REACH". |
| `ownerProfileId` | `string` | The user profile id of the owner of this report. |
| `floodlightCriteria` | `object` | The report criteria for a report of type "FLOODLIGHT". |
| `lastModifiedTime` | `string` | The timestamp (in milliseconds since epoch) of when this report was last modified. |
| `subAccountId` | `string` | The subaccount ID to which this report belongs if applicable. |
| `pathCriteria` | `object` | The report criteria for a report of type "PATH". |
| `etag` | `string` | The eTag of this response for caching purposes. |
| `accountId` | `string` | The account ID to which this report belongs. |
| `delivery` | `object` | The report's email delivery settings. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `profileId, reportId` | Retrieves a report by its ID. |
| `list` | `SELECT` | `profileId` | Retrieves list of reports. |
| `insert` | `INSERT` | `profileId` | Creates a report. |
| `delete` | `DELETE` | `profileId, reportId` | Deletes a report by its ID. |
| `patch` | `EXEC` | `profileId, reportId` | Updates an existing report. This method supports patch semantics. |
| `run` | `EXEC` | `profileId, reportId` | Runs a report. |
| `update` | `EXEC` | `profileId, reportId` | Updates a report. |

---
title: unsampled_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - unsampled_reports
  - analytics
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>unsampled_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.unsampled_reports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unsampled report ID. |
| `title` | `string` | Title of the unsampled report. |
| `created` | `string` | Time this unsampled report was created. |
| `downloadType` | `string` | The type of download you need to use for the report data file. Possible values include `GOOGLE_DRIVE` and `GOOGLE_CLOUD_STORAGE`. If the value is `GOOGLE_DRIVE`, see the `driveDownloadDetails` field. If the value is `GOOGLE_CLOUD_STORAGE`, see the `cloudStorageDownloadDetails` field. |
| `filters` | `string` | The filters for the unsampled report. |
| `accountId` | `string` | Account ID to which this unsampled report belongs. |
| `webPropertyId` | `string` | Web property ID to which this unsampled report belongs. The web property ID is of the form UA-XXXXX-YY. |
| `updated` | `string` | Time this unsampled report was last modified. |
| `status` | `string` | Status of this unsampled report. Possible values are PENDING, COMPLETED, or FAILED. |
| `cloudStorageDownloadDetails` | `object` | Download details for a file stored in Google Cloud Storage. |
| `metrics` | `string` | The metrics for the unsampled report. |
| `kind` | `string` | Resource type for an Analytics unsampled report. |
| `start-date` | `string` | The start date for the unsampled report. |
| `dimensions` | `string` | The dimensions for the unsampled report. |
| `selfLink` | `string` | Link for this unsampled report. |
| `segment` | `string` | The segment for the unsampled report. |
| `driveDownloadDetails` | `object` | Download details for a file stored in Google Drive. |
| `end-date` | `string` | The end date for the unsampled report. |
| `profileId` | `string` | View (Profile) ID to which this unsampled report belongs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `management_unsampledReports_get` | `SELECT` | `accountId, profileId, unsampledReportId, webPropertyId` | Returns a single unsampled report. |
| `management_unsampledReports_list` | `SELECT` | `accountId, profileId, webPropertyId` | Lists unsampled reports to which the user has access. |
| `management_unsampledReports_delete` | `DELETE` | `accountId, profileId, unsampledReportId, webPropertyId` | Deletes an unsampled report. |
| `management_unsampledReports_insert` | `EXEC` | `accountId, profileId, webPropertyId` | Create a new unsampled report. |

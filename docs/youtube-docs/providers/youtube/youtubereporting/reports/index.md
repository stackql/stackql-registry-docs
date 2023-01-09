---
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
  - youtubereporting
  - youtube    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/youtube/stackql-youtube-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtubereporting.reports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The server-generated ID of the report. |
| `downloadUrl` | `string` | The URL from which the report can be downloaded (max. 1000 characters). |
| `endTime` | `string` | The end of the time period that the report instance covers. The value is exclusive. |
| `jobExpireTime` | `string` | The date/time when the job this report belongs to will expire/expired. |
| `jobId` | `string` | The ID of the job that created this report. |
| `startTime` | `string` | The start of the time period that the report instance covers. The value is inclusive. |
| `createTime` | `string` | The date/time when this report was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `jobs_reports_get` | `SELECT` | `jobId, reportId` | Gets the metadata of a specific report. |
| `jobs_reports_list` | `SELECT` | `jobId` | Lists reports created by a specific job. Returns NOT_FOUND if the job does not exist. |

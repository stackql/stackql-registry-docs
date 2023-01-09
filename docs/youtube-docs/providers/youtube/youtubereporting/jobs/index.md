---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>youtube.youtubereporting.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The server-generated ID of the job (max. 40 characters). |
| `name` | `string` | The name of the job (max. 100 characters). |
| `reportTypeId` | `string` | The type of reports this job creates. Corresponds to the ID of a ReportType. |
| `systemManaged` | `boolean` | True if this a system-managed job that cannot be modified by the user; otherwise false. |
| `createTime` | `string` | The creation date/time of the job. |
| `expireTime` | `string` | The date/time when this job will expire/expired. After a job expired, no new reports are generated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobId` | Gets a job. |
| `list` | `SELECT` |  | Lists jobs. |
| `create` | `INSERT` |  | Creates a job and returns it. |
| `delete` | `DELETE` | `jobId` | Deletes a job. |

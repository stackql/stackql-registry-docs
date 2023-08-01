---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - archive
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.archive.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique identifier of the ingestion job. |
| `name` | `string` | The name of the ingestion job. |
| `endTime` | `string` | The ending timestamp of the ingestion job. |
| `totalObjectsIngested` | `integer` | The total number of objects ingested by the ingestion job. |
| `startTime` | `string` | The starting timestamp of the ingestion job. |
| `createdAt` | `string` | The creation timestamp in UTC of the ingestion job. |
| `status` | `string` | The status of the ingestion job, either `Pending`,`Scanning`,`Ingesting`,`Failed`, or `Succeeded`. |
| `totalBytesIngested` | `integer` | The total bytes ingested by the ingestion job. |
| `createdBy` | `string` | The identifier of the user who created the ingestion job. |
| `totalObjectsScanned` | `integer` | The total number of objects scanned by the ingestion job. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `listArchiveJobsBySourceId` | `SELECT` | `sourceId, region` | Get a list of all the ingestion jobs created on an Archive Source. The response is paginated with a default limit of 10 jobs per page. |
| `createArchiveJob` | `INSERT` | `sourceId, data__endTime, data__name, data__startTime, region` | Create an ingestion job to pull data from your S3 bucket. |
| `deleteArchiveJob` | `DELETE` | `id, sourceId, region` | Delete an ingestion job with the given identifier from the organization. The delete operation is only possible for jobs with a Succeeded or Failed status. |

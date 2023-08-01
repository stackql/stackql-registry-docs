---
title: batches
hide_title: false
hide_table_of_contents: false
keywords:
  - batches
  - dataproc
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
<tr><td><b>Name</b></td><td><code>batches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataproc.batches</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `batches` | `array` | Output only. The batches from the specified collection. |
| `nextPageToken` | `string` | A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_batches_list` | `SELECT` | `locationsId, projectsId` | Lists batch workloads. |
| `projects_locations_batches_create` | `INSERT` | `locationsId, projectsId` | Creates a batch workload that executes asynchronously. |
| `projects_locations_batches_delete` | `DELETE` | `batchesId, locationsId, projectsId` | Deletes the batch workload resource. If the batch is not in a CANCELLED, SUCCEEDED or FAILED State, the delete operation fails and the response returns FAILED_PRECONDITION. |
| `projects_locations_batches_get` | `EXEC` | `batchesId, locationsId, projectsId` | Gets the batch workload resource representation. |

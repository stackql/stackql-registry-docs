---
title: transfer_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - transfer_jobs
  - storagetransfer
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
<tr><td><b>Name</b></td><td><code>transfer_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.storagetransfer.transfer_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The list next page token. |
| `transferJobs` | `array` | A list of transfer jobs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `projectId, transferJobsId` | Gets a transfer job. |
| `list` | `SELECT` | `filter` | Lists transfer jobs. |
| `create` | `INSERT` |  | Creates a transfer job that runs periodically. |
| `delete` | `DELETE` | `projectId, transferJobsId` | Deletes a transfer job. Deleting a transfer job sets its status to DELETED. |
| `patch` | `EXEC` | `transferJobsId` | Updates a transfer job. Updating a job's transfer spec does not affect transfer operations that are running already. **Note:** The job's status field can be modified using this RPC (for example, to set a job's status to DELETED, DISABLED, or ENABLED). |
| `run` | `EXEC` | `transferJobsId` | Starts a new operation for the specified transfer job. A `TransferJob` has a maximum of one active `TransferOperation`. If this method is called while a `TransferOperation` is active, an error is returned. |

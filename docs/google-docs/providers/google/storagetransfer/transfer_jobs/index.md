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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>transfer_job</code> resource or lists <code>transfer_jobs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transfer_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storagetransfer.transfer_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A unique name (within the transfer project) assigned when the job is created. If this field is empty in a CreateTransferJobRequest, Storage Transfer Service assigns a unique name. Otherwise, the specified name is used as the unique name for this job. If the specified name is in use by a job, the creation request fails with an ALREADY_EXISTS error. This name must start with `"transferJobs/"` prefix and end with a letter or a number, and should be no more than 128 characters. For transfers involving PosixFilesystem, this name must start with `transferJobs/OPI` specifically. For all other transfer types, this name must not start with `transferJobs/OPI`. Non-PosixFilesystem example: `"transferJobs/^(?!OPI)[A-Za-z0-9-._~]*[A-Za-z0-9]$"` PosixFilesystem example: `"transferJobs/OPI^[A-Za-z0-9-._~]*[A-Za-z0-9]$"` Applications must not rely on the enforcement of naming requirements involving OPI. Invalid job names fail with an INVALID_ARGUMENT error. |
| <CopyableCode code="description" /> | `string` | A description provided by the user for the job. Its max length is 1024 bytes when Unicode-encoded. |
| <CopyableCode code="creationTime" /> | `string` | Output only. The time that the transfer job was created. |
| <CopyableCode code="deletionTime" /> | `string` | Output only. The time that the transfer job was deleted. |
| <CopyableCode code="eventStream" /> | `object` | Specifies the Event-driven transfer options. Event-driven transfers listen to an event stream to transfer updated files. |
| <CopyableCode code="lastModificationTime" /> | `string` | Output only. The time that the transfer job was last modified. |
| <CopyableCode code="latestOperationName" /> | `string` | The name of the most recently started TransferOperation of this JobConfig. Present if a TransferOperation has been created for this JobConfig. |
| <CopyableCode code="loggingConfig" /> | `object` | Specifies the logging behavior for transfer operations. Logs can be sent to Cloud Logging for all transfer types. See [Read transfer logs](https://cloud.google.com/storage-transfer/docs/read-transfer-logs) for details. |
| <CopyableCode code="notificationConfig" /> | `object` | Specification to configure notifications published to Pub/Sub. Notifications are published to the customer-provided topic using the following `PubsubMessage.attributes`: * `"eventType"`: one of the EventType values * `"payloadFormat"`: one of the PayloadFormat values * `"projectId"`: the project_id of the `TransferOperation` * `"transferJobName"`: the transfer_job_name of the `TransferOperation` * `"transferOperationName"`: the name of the `TransferOperation` The `PubsubMessage.data` contains a TransferOperation resource formatted according to the specified `PayloadFormat`. |
| <CopyableCode code="projectId" /> | `string` | The ID of the Google Cloud project that owns the job. |
| <CopyableCode code="replicationSpec" /> | `object` | Specifies the configuration for running a replication job. |
| <CopyableCode code="schedule" /> | `object` | Transfers can be scheduled to recur or to run just once. |
| <CopyableCode code="status" /> | `string` | Status of the job. This value MUST be specified for `CreateTransferJobRequests`. **Note:** The effect of the new job status takes place during a subsequent job run. For example, if you change the job status from ENABLED to DISABLED, and an operation spawned by the transfer is running, the status change would not affect the current operation. |
| <CopyableCode code="transferSpec" /> | `object` | Configuration for running a transfer. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="projectId, transferJobsId" /> | Gets a transfer job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="filter" /> | Lists transfer jobs. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="" /> | Creates a transfer job that runs periodically. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="projectId, transferJobsId" /> | Deletes a transfer job. Deleting a transfer job sets its status to DELETED. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="transferJobsId" /> | Updates a transfer job. Updating a job's transfer spec does not affect transfer operations that are running already. **Note:** The job's status field can be modified using this RPC (for example, to set a job's status to DELETED, DISABLED, or ENABLED). |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="transferJobsId" /> | Starts a new operation for the specified transfer job. A `TransferJob` has a maximum of one active `TransferOperation`. If this method is called while a `TransferOperation` is active, an error is returned. |

## `SELECT` examples

Lists transfer jobs.

```sql
SELECT
name,
description,
creationTime,
deletionTime,
eventStream,
lastModificationTime,
latestOperationName,
loggingConfig,
notificationConfig,
projectId,
replicationSpec,
schedule,
status,
transferSpec
FROM google.storagetransfer.transfer_jobs
WHERE filter = '{{ filter }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>transfer_jobs</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.storagetransfer.transfer_jobs (
,
name,
description,
projectId,
transferSpec,
replicationSpec,
notificationConfig,
loggingConfig,
schedule,
eventStream,
status,
creationTime,
lastModificationTime,
deletionTime,
latestOperationName
)
SELECT 
'{{  }}',
'{{ name }}',
'{{ description }}',
'{{ projectId }}',
'{{ transferSpec }}',
'{{ replicationSpec }}',
'{{ notificationConfig }}',
'{{ loggingConfig }}',
'{{ schedule }}',
'{{ eventStream }}',
'{{ status }}',
'{{ creationTime }}',
'{{ lastModificationTime }}',
'{{ deletionTime }}',
'{{ latestOperationName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: projectId
        value: '{{ projectId }}'
      - name: transferSpec
        value: '{{ transferSpec }}'
      - name: replicationSpec
        value: '{{ replicationSpec }}'
      - name: notificationConfig
        value: '{{ notificationConfig }}'
      - name: loggingConfig
        value: '{{ loggingConfig }}'
      - name: schedule
        value: '{{ schedule }}'
      - name: eventStream
        value: '{{ eventStream }}'
      - name: status
        value: '{{ status }}'
      - name: creationTime
        value: '{{ creationTime }}'
      - name: lastModificationTime
        value: '{{ lastModificationTime }}'
      - name: deletionTime
        value: '{{ deletionTime }}'
      - name: latestOperationName
        value: '{{ latestOperationName }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a transfer_job only if the necessary resources are available.

```sql
UPDATE google.storagetransfer.transfer_jobs
SET 
projectId = '{{ projectId }}',
transferJob = '{{ transferJob }}',
updateTransferJobFieldMask = '{{ updateTransferJobFieldMask }}'
WHERE 
transferJobsId = '{{ transferJobsId }}';
```

## `DELETE` example

Deletes the specified transfer_job resource.

```sql
DELETE FROM google.storagetransfer.transfer_jobs
WHERE projectId = '{{ projectId }}'
AND transferJobsId = '{{ transferJobsId }}';
```

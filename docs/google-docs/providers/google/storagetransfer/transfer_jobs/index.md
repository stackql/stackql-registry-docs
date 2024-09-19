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

Creates, updates, deletes, gets or lists a <code>transfer_jobs</code> resource.

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
latestOperationName
)
SELECT 
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
'{{ latestOperationName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: description
      value: string
    - name: projectId
      value: string
    - name: transferSpec
      value:
        - name: gcsDataSink
          value:
            - name: bucketName
              value: string
            - name: path
              value: string
            - name: managedFolderTransferEnabled
              value: boolean
        - name: posixDataSink
          value:
            - name: rootDirectory
              value: string
        - name: awsS3DataSource
          value:
            - name: bucketName
              value: string
            - name: awsAccessKey
              value:
                - name: accessKeyId
                  value: string
                - name: secretAccessKey
                  value: string
            - name: path
              value: string
            - name: roleArn
              value: string
            - name: cloudfrontDomain
              value: string
            - name: credentialsSecret
              value: string
            - name: managedPrivateNetwork
              value: boolean
        - name: httpDataSource
          value:
            - name: listUrl
              value: string
        - name: azureBlobStorageDataSource
          value:
            - name: storageAccount
              value: string
            - name: azureCredentials
              value:
                - name: sasToken
                  value: string
            - name: container
              value: string
            - name: path
              value: string
            - name: credentialsSecret
              value: string
        - name: awsS3CompatibleDataSource
          value:
            - name: bucketName
              value: string
            - name: path
              value: string
            - name: endpoint
              value: string
            - name: region
              value: string
            - name: s3Metadata
              value:
                - name: authMethod
                  value: string
                - name: requestModel
                  value: string
                - name: protocol
                  value: string
                - name: listApi
                  value: string
        - name: hdfsDataSource
          value:
            - name: path
              value: string
        - name: objectConditions
          value:
            - name: minTimeElapsedSinceLastModification
              value: string
            - name: maxTimeElapsedSinceLastModification
              value: string
            - name: includePrefixes
              value:
                - string
            - name: excludePrefixes
              value:
                - string
            - name: lastModifiedSince
              value: string
            - name: lastModifiedBefore
              value: string
        - name: transferOptions
          value:
            - name: overwriteObjectsAlreadyExistingInSink
              value: boolean
            - name: deleteObjectsUniqueInSink
              value: boolean
            - name: deleteObjectsFromSourceAfterTransfer
              value: boolean
            - name: overwriteWhen
              value: string
            - name: metadataOptions
              value:
                - name: symlink
                  value: string
                - name: mode
                  value: string
                - name: gid
                  value: string
                - name: uid
                  value: string
                - name: acl
                  value: string
                - name: storageClass
                  value: string
                - name: temporaryHold
                  value: string
                - name: kmsKey
                  value: string
                - name: timeCreated
                  value: string
        - name: transferManifest
          value:
            - name: location
              value: string
        - name: sourceAgentPoolName
          value: string
        - name: sinkAgentPoolName
          value: string
    - name: replicationSpec
      value: []
    - name: notificationConfig
      value:
        - name: pubsubTopic
          value: string
        - name: eventTypes
          value:
            - string
        - name: payloadFormat
          value: string
    - name: loggingConfig
      value:
        - name: logActions
          value:
            - string
        - name: logActionStates
          value:
            - string
        - name: enableOnpremGcsTransferLogs
          value: boolean
    - name: schedule
      value:
        - name: scheduleStartDate
          value:
            - name: year
              value: integer
            - name: month
              value: integer
            - name: day
              value: integer
        - name: startTimeOfDay
          value:
            - name: hours
              value: integer
            - name: minutes
              value: integer
            - name: seconds
              value: integer
            - name: nanos
              value: integer
        - name: repeatInterval
          value: string
    - name: eventStream
      value:
        - name: name
          value: string
        - name: eventStreamStartTime
          value: string
        - name: eventStreamExpirationTime
          value: string
    - name: status
      value: string
    - name: creationTime
      value: string
    - name: lastModificationTime
      value: string
    - name: deletionTime
      value: string
    - name: latestOperationName
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>transfer_jobs</code> resource.

```sql
/*+ update */
UPDATE google.storagetransfer.transfer_jobs
SET 
projectId = '{{ projectId }}',
transferJob = '{{ transferJob }}',
updateTransferJobFieldMask = '{{ updateTransferJobFieldMask }}'
WHERE 
transferJobsId = '{{ transferJobsId }}';
```

## `DELETE` example

Deletes the specified <code>transfer_jobs</code> resource.

```sql
/*+ delete */
DELETE FROM google.storagetransfer.transfer_jobs
WHERE projectId = '{{ projectId }}'
AND transferJobsId = '{{ transferJobsId }}';
```

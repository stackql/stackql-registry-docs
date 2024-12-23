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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>batches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>batches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataproc.batches" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the batch. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the batch was created. |
| <CopyableCode code="creator" /> | `string` | Output only. The email address of the user who created the batch. |
| <CopyableCode code="environmentConfig" /> | `object` | Environment configuration for a workload. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels to associate with this batch. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a batch. |
| <CopyableCode code="operation" /> | `string` | Output only. The resource name of the operation associated with this batch. |
| <CopyableCode code="pysparkBatch" /> | `object` | A configuration for running an Apache PySpark (https://spark.apache.org/docs/latest/api/python/getting_started/quickstart.html) batch workload. |
| <CopyableCode code="runtimeConfig" /> | `object` | Runtime configuration for a workload. |
| <CopyableCode code="runtimeInfo" /> | `object` | Runtime information about workload execution. |
| <CopyableCode code="sparkBatch" /> | `object` | A configuration for running an Apache Spark (https://spark.apache.org/) batch workload. |
| <CopyableCode code="sparkRBatch" /> | `object` | A configuration for running an Apache SparkR (https://spark.apache.org/docs/latest/sparkr.html) batch workload. |
| <CopyableCode code="sparkSqlBatch" /> | `object` | A configuration for running Apache Spark SQL (https://spark.apache.org/sql/) queries as a batch workload. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the batch. |
| <CopyableCode code="stateHistory" /> | `array` | Output only. Historical state information for the batch. |
| <CopyableCode code="stateMessage" /> | `string` | Output only. Batch state details, such as a failure description if the state is FAILED. |
| <CopyableCode code="stateTime" /> | `string` | Output only. The time when the batch entered a current state. |
| <CopyableCode code="uuid" /> | `string` | Output only. A batch UUID (Unique Universal Identifier). The service generates this value when it creates the batch. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_batches_get" /> | `SELECT` | <CopyableCode code="batchesId, locationsId, projectsId" /> | Gets the batch workload resource representation. |
| <CopyableCode code="projects_locations_batches_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists batch workloads. |
| <CopyableCode code="projects_locations_batches_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a batch workload that executes asynchronously. |
| <CopyableCode code="projects_locations_batches_delete" /> | `DELETE` | <CopyableCode code="batchesId, locationsId, projectsId" /> | Deletes the batch workload resource. If the batch is not in a CANCELLED, SUCCEEDED or FAILED State, the delete operation fails and the response returns FAILED_PRECONDITION. |
| <CopyableCode code="projects_locations_batches_analyze" /> | `EXEC` | <CopyableCode code="batchesId, locationsId, projectsId" /> | Analyze a Batch for possible recommendations and insights. |

## `SELECT` examples

Lists batch workloads.

```sql
SELECT
name,
createTime,
creator,
environmentConfig,
labels,
operation,
pysparkBatch,
runtimeConfig,
runtimeInfo,
sparkBatch,
sparkRBatch,
sparkSqlBatch,
state,
stateHistory,
stateMessage,
stateTime,
uuid
FROM google.dataproc.batches
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>batches</code> resource.

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
INSERT INTO google.dataproc.batches (
locationsId,
projectsId,
pysparkBatch,
sparkBatch,
sparkRBatch,
sparkSqlBatch,
labels,
runtimeConfig,
environmentConfig
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ pysparkBatch }}',
'{{ sparkBatch }}',
'{{ sparkRBatch }}',
'{{ sparkSqlBatch }}',
'{{ labels }}',
'{{ runtimeConfig }}',
'{{ environmentConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: uuid
      value: string
    - name: createTime
      value: string
    - name: pysparkBatch
      value:
        - name: mainPythonFileUri
          value: string
        - name: args
          value:
            - string
        - name: pythonFileUris
          value:
            - string
        - name: jarFileUris
          value:
            - string
        - name: fileUris
          value:
            - string
        - name: archiveUris
          value:
            - string
    - name: sparkBatch
      value:
        - name: mainJarFileUri
          value: string
        - name: mainClass
          value: string
        - name: args
          value:
            - string
        - name: jarFileUris
          value:
            - string
        - name: fileUris
          value:
            - string
        - name: archiveUris
          value:
            - string
    - name: sparkRBatch
      value:
        - name: mainRFileUri
          value: string
        - name: args
          value:
            - string
        - name: fileUris
          value:
            - string
        - name: archiveUris
          value:
            - string
    - name: sparkSqlBatch
      value:
        - name: queryFileUri
          value: string
        - name: queryVariables
          value: object
        - name: jarFileUris
          value:
            - string
    - name: runtimeInfo
      value:
        - name: endpoints
          value: object
        - name: outputUri
          value: string
        - name: diagnosticOutputUri
          value: string
        - name: approximateUsage
          value:
            - name: milliDcuSeconds
              value: string
            - name: shuffleStorageGbSeconds
              value: string
            - name: milliAcceleratorSeconds
              value: string
            - name: acceleratorType
              value: string
        - name: currentUsage
          value:
            - name: milliDcu
              value: string
            - name: shuffleStorageGb
              value: string
            - name: milliDcuPremium
              value: string
            - name: shuffleStorageGbPremium
              value: string
            - name: milliAccelerator
              value: string
            - name: acceleratorType
              value: string
            - name: snapshotTime
              value: string
    - name: state
      value: string
    - name: stateMessage
      value: string
    - name: stateTime
      value: string
    - name: creator
      value: string
    - name: labels
      value: object
    - name: runtimeConfig
      value:
        - name: version
          value: string
        - name: containerImage
          value: string
        - name: properties
          value: object
        - name: repositoryConfig
          value:
            - name: pypiRepositoryConfig
              value:
                - name: pypiRepository
                  value: string
        - name: autotuningConfig
          value:
            - name: scenarios
              value:
                - string
        - name: cohort
          value: string
    - name: environmentConfig
      value:
        - name: executionConfig
          value:
            - name: serviceAccount
              value: string
            - name: networkUri
              value: string
            - name: subnetworkUri
              value: string
            - name: networkTags
              value:
                - string
            - name: kmsKey
              value: string
            - name: idleTtl
              value: string
            - name: ttl
              value: string
            - name: stagingBucket
              value: string
        - name: peripheralsConfig
          value:
            - name: metastoreService
              value: string
            - name: sparkHistoryServerConfig
              value:
                - name: dataprocCluster
                  value: string
    - name: operation
      value: string
    - name: stateHistory
      value:
        - - name: state
            value: string
          - name: stateMessage
            value: string
          - name: stateStartTime
            value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>batches</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataproc.batches
WHERE batchesId = '{{ batchesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

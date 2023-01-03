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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Output only. The resource name of the batch. |
| `state` | `string` | Output only. The state of the batch. |
| `environmentConfig` | `object` | Environment configuration for a workload. |
| `labels` | `object` | Optional. The labels to associate with this batch. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a batch. |
| `runtimeInfo` | `object` | Runtime information about workload execution. |
| `pysparkBatch` | `object` | A configuration for running an Apache PySpark (https://spark.apache.org/docs/latest/api/python/getting_started/quickstart.html) batch workload. |
| `createTime` | `string` | Output only. The time when the batch was created. |
| `operation` | `string` | Output only. The resource name of the operation associated with this batch. |
| `sparkSqlBatch` | `object` | A configuration for running Apache Spark SQL (https://spark.apache.org/sql/) queries as a batch workload. |
| `stateHistory` | `array` | Output only. Historical state information for the batch. |
| `uuid` | `string` | Output only. A batch UUID (Unique Universal Identifier). The service generates this value when it creates the batch. |
| `sparkBatch` | `object` | A configuration for running an Apache Spark (https://spark.apache.org/) batch workload. |
| `stateTime` | `string` | Output only. The time when the batch entered a current state. |
| `stateMessage` | `string` | Output only. Batch state details, such as a failure description if the state is FAILED. |
| `runtimeConfig` | `object` | Runtime configuration for a workload. |
| `sparkRBatch` | `object` | A configuration for running an Apache SparkR (https://spark.apache.org/docs/latest/sparkr.html) batch workload. |
| `creator` | `string` | Output only. The email address of the user who created the batch. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_batches_get` | `SELECT` | `batchesId, locationsId, projectsId` | Gets the batch workload resource representation. |
| `projects_locations_batches_list` | `SELECT` | `locationsId, projectsId` | Lists batch workloads. |
| `projects_locations_batches_create` | `INSERT` | `locationsId, projectsId` | Creates a batch workload that executes asynchronously. |
| `projects_locations_batches_delete` | `DELETE` | `batchesId, locationsId, projectsId` | Deletes the batch workload resource. If the batch is not in terminal state, the delete fails and the response returns FAILED_PRECONDITION. |

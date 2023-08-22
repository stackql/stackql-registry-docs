---
title: replication_cycles
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_cycles
  - vmmigration
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
<tr><td><b>Name</b></td><td><code>replication_cycles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vmmigration.replication_cycles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The identifier of the ReplicationCycle. |
| `cycleNumber` | `integer` | The cycle's ordinal number. |
| `startTime` | `string` | The time the replication cycle has started. |
| `warnings` | `array` | Output only. Warnings that occurred during the cycle. |
| `totalPauseDuration` | `string` | The accumulated duration the replication cycle was paused. |
| `endTime` | `string` | The time the replication cycle has ended. |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `progressPercent` | `integer` | The current progress in percentage of this cycle. Was replaced by 'steps' field, which breaks down the cycle progression more accurately. |
| `steps` | `array` | The cycle's steps list representing its progress. |
| `state` | `string` | State of the ReplicationCycle. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, migratingVmsId, projectsId, replicationCyclesId, sourcesId` | Gets details of a single ReplicationCycle. |
| `list` | `SELECT` | `locationsId, migratingVmsId, projectsId, sourcesId` | Lists ReplicationCycles in a given MigratingVM. |
| `_list` | `EXEC` | `locationsId, migratingVmsId, projectsId, sourcesId` | Lists ReplicationCycles in a given MigratingVM. |

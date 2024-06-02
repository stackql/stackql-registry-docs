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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_cycles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vmmigration.replication_cycles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The identifier of the ReplicationCycle. |
| <CopyableCode code="cycleNumber" /> | `integer` | The cycle's ordinal number. |
| <CopyableCode code="endTime" /> | `string` | The time the replication cycle has ended. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="progressPercent" /> | `integer` | The current progress in percentage of this cycle. Was replaced by 'steps' field, which breaks down the cycle progression more accurately. |
| <CopyableCode code="startTime" /> | `string` | The time the replication cycle has started. |
| <CopyableCode code="state" /> | `string` | State of the ReplicationCycle. |
| <CopyableCode code="steps" /> | `array` | The cycle's steps list representing its progress. |
| <CopyableCode code="totalPauseDuration" /> | `string` | The accumulated duration the replication cycle was paused. |
| <CopyableCode code="warnings" /> | `array` | Output only. Warnings that occurred during the cycle. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, migratingVmsId, projectsId, replicationCyclesId, sourcesId" /> | Gets details of a single ReplicationCycle. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, migratingVmsId, projectsId, sourcesId" /> | Lists ReplicationCycles in a given MigratingVM. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, migratingVmsId, projectsId, sourcesId" /> | Lists ReplicationCycles in a given MigratingVM. |

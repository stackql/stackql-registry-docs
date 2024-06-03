---
title: cutover_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - cutover_jobs
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
<tr><td><b>Name</b></td><td><code>cutover_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmmigration.cutover_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the cutover job. |
| <CopyableCode code="computeEngineDisksTargetDetails" /> | `object` | ComputeEngineDisksTargetDetails is a collection of created Persistent Disks details. |
| <CopyableCode code="computeEngineTargetDetails" /> | `object` | ComputeEngineTargetDetails is a collection of details for creating a VM in a target Compute Engine project. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the cutover job was created (as an API call, not when it was actually created in the target). |
| <CopyableCode code="endTime" /> | `string` | Output only. The time the cutover job had finished. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="progressPercent" /> | `integer` | Output only. The current progress in percentage of the cutover job. |
| <CopyableCode code="state" /> | `string` | Output only. State of the cutover job. |
| <CopyableCode code="stateMessage" /> | `string` | Output only. A message providing possible extra details about the current state. |
| <CopyableCode code="stateTime" /> | `string` | Output only. The time the state was last updated. |
| <CopyableCode code="steps" /> | `array` | Output only. The cutover steps list representing its progress. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cutoverJobsId, locationsId, migratingVmsId, projectsId, sourcesId" /> | Gets details of a single CutoverJob. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, migratingVmsId, projectsId, sourcesId" /> | Lists the CutoverJobs of a migrating VM. Only 25 most recent CutoverJobs are listed. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, migratingVmsId, projectsId, sourcesId" /> | Initiates a Cutover of a specific migrating VM. The returned LRO is completed when the cutover job resource is created and the job is initiated. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, migratingVmsId, projectsId, sourcesId" /> | Lists the CutoverJobs of a migrating VM. Only 25 most recent CutoverJobs are listed. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="cutoverJobsId, locationsId, migratingVmsId, projectsId, sourcesId" /> | Initiates the cancellation of a running cutover job. |

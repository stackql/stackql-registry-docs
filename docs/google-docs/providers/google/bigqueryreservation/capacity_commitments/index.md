---
title: capacity_commitments
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_commitments
  - bigqueryreservation
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
<tr><td><b>Name</b></td><td><code>capacity_commitments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigqueryreservation.capacity_commitments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the capacity commitment, e.g., `projects/myproject/locations/US/capacityCommitments/123` The commitment_id must only contain lower case alphanumeric characters or dashes. It must start with a letter and must not end with a dash. Its maximum length is 64 characters. |
| `slotCount` | `string` | Number of slots in this commitment. |
| `edition` | `string` | Edition of the capacity commitment. |
| `failureStatus` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `plan` | `string` | Capacity commitment commitment plan. |
| `isFlatRate` | `boolean` | Output only. If true, the commitment is a flat-rate commitment, otherwise, it's an edition commitment. |
| `commitmentEndTime` | `string` | Output only. The end of the current commitment period. It is applicable only for ACTIVE capacity commitments. |
| `state` | `string` | Output only. State of the commitment. |
| `multiRegionAuxiliary` | `boolean` | Applicable only for commitments located within one of the BigQuery multi-regions (US or EU). If set to true, this commitment is placed in the organization's secondary region which is designated for disaster recovery purposes. If false, this commitment is placed in the organization's default region. NOTE: this is a preview feature. Project must be allow-listed in order to set this field. |
| `renewalPlan` | `string` | The plan this capacity commitment is converted to after commitment_end_time passes. Once the plan is changed, committed period is extended according to commitment plan. Only applicable for ANNUAL and TRIAL commitments. |
| `commitmentStartTime` | `string` | Output only. The start of the current commitment period. It is applicable only for ACTIVE capacity commitments. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `capacityCommitmentsId, locationsId, projectsId` | Returns information about the capacity commitment. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all the capacity commitments for the admin project. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new capacity commitment resource. |
| `delete` | `DELETE` | `capacityCommitmentsId, locationsId, projectsId` | Deletes a capacity commitment. Attempting to delete capacity commitment before its commitment_end_time will fail with the error code `google.rpc.Code.FAILED_PRECONDITION`. |
| `merge` | `EXEC` | `locationsId, projectsId` | Merges capacity commitments of the same plan into a single commitment. The resulting capacity commitment has the greater commitment_end_time out of the to-be-merged capacity commitments. Attempting to merge capacity commitments of different plan will fail with the error code `google.rpc.Code.FAILED_PRECONDITION`. |
| `patch` | `EXEC` | `capacityCommitmentsId, locationsId, projectsId` | Updates an existing capacity commitment. Only `plan` and `renewal_plan` fields can be updated. Plan can only be changed to a plan of a longer commitment period. Attempting to change to a plan with shorter commitment period will fail with the error code `google.rpc.Code.FAILED_PRECONDITION`. |
| `split` | `EXEC` | `capacityCommitmentsId, locationsId, projectsId` | Splits capacity commitment to two commitments of the same plan and `commitment_end_time`. A common use case is to enable downgrading commitments. For example, in order to downgrade from 10000 slots to 8000, you might split a 10000 capacity commitment into commitments of 2000 and 8000. Then, you delete the first one after the commitment end time passes. |

---
title: utilization_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - utilization_reports
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
<tr><td><b>Name</b></td><td><code>utilization_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmmigration.utilization_reports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The report unique name. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the report was created (this refers to the time of the request, not the time the report creation completed). |
| <CopyableCode code="displayName" /> | `string` | The report display name, as assigned by the user. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="frameEndTime" /> | `string` | Output only. The point in time when the time frame ends. Notice that the time frame is counted backwards. For instance if the "frame_end_time" value is 2021/01/20 and the time frame is WEEK then the report covers the week between 2021/01/20 and 2021/01/14. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the report. |
| <CopyableCode code="stateTime" /> | `string` | Output only. The time the state was last set. |
| <CopyableCode code="timeFrame" /> | `string` | Time frame of the report. |
| <CopyableCode code="vmCount" /> | `integer` | Output only. Total number of VMs included in the report. |
| <CopyableCode code="vms" /> | `array` | List of utilization information per VM. When sent as part of the request, the "vm_id" field is used in order to specify which VMs to include in the report. In that case all other fields are ignored. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, sourcesId, utilizationReportsId" /> | Gets a single Utilization Report. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Lists Utilization Reports of the given Source. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Creates a new UtilizationReport. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, sourcesId, utilizationReportsId" /> | Deletes a single Utilization Report. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Lists Utilization Reports of the given Source. |

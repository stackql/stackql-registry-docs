---
title: canaryevaluations
hide_title: false
hide_table_of_contents: false
keywords:
  - canaryevaluations
  - apigee
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
<tr><td><b>Name</b></td><td><code>canaryevaluations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.canaryevaluations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the canary evalution. |
| <CopyableCode code="control" /> | `string` | Required. The stable version that is serving requests. |
| <CopyableCode code="createTime" /> | `string` | Output only. Create time of the canary evaluation. |
| <CopyableCode code="endTime" /> | `string` | Required. End time for the evaluation's analysis. |
| <CopyableCode code="metricLabels" /> | `object` | Labels that can be used to filter Apigee metrics. |
| <CopyableCode code="startTime" /> | `string` | Required. Start time for the canary evaluation's analysis. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the canary evaluation. |
| <CopyableCode code="treatment" /> | `string` | Required. The newer version that is serving requests. |
| <CopyableCode code="verdict" /> | `string` | Output only. The resulting verdict of the canary evaluations: NONE, PASS, or FAIL. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_instances_canaryevaluations_get" /> | `SELECT` | <CopyableCode code="canaryevaluationsId, instancesId, organizationsId" /> | Gets a CanaryEvaluation for an organization. |
| <CopyableCode code="organizations_instances_canaryevaluations_create" /> | `INSERT` | <CopyableCode code="instancesId, organizationsId" /> | Creates a new canary evaluation for an organization. |

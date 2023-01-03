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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>canaryevaluations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.canaryevaluations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the canary evalution. |
| `state` | `string` | Output only. The current state of the canary evaluation. |
| `treatment` | `string` | Required. The newer version that is serving requests. |
| `endTime` | `string` | Required. End time for the evaluation's analysis. |
| `metricLabels` | `object` | Labels that can be used to filter Apigee metrics. |
| `control` | `string` | Required. The stable version that is serving requests. |
| `verdict` | `string` | Output only. The resulting verdict of the canary evaluations: NONE, PASS, or FAIL. |
| `createTime` | `string` | Output only. Create time of the canary evaluation. |
| `startTime` | `string` | Required. Start time for the canary evaluation's analysis. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_instances_canaryevaluations_get` | `SELECT` | `canaryevaluationsId, instancesId, organizationsId` | Gets a CanaryEvaluation for an organization. |
| `organizations_instances_canaryevaluations_create` | `INSERT` | `instancesId, organizationsId` | Creates a new canary evaluation for an organization. |

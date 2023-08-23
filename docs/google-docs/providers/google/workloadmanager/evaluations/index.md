---
title: evaluations
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluations
  - workloadmanager
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
<tr><td><b>Name</b></td><td><code>evaluations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workloadmanager.evaluations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | name of resource names have the form 'projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/evaluations/&#123;evaluation_id&#125;' |
| `description` | `string` | Description of the Evaluation |
| `customRulesBucket` | `string` | The Cloud Storage bucket name for custom rules. |
| `labels` | `object` | Labels as key value pairs |
| `updateTime` | `string` | Output only. [Output only] Update time stamp |
| `resourceStatus` | `object` | Message describing resource status |
| `ruleVersions` | `array` | Output only. [Output only] The updated rule ids if exist. |
| `schedule` | `string` | crontab format schedule for scheduled evaluation, currently only support the following schedule: "0 */1 * * *", "0 */6 * * *", "0 */12 * * *", "0 0 */1 * *", "0 0 */7 * *", |
| `resourceFilter` | `object` | Message describing resource filters |
| `createTime` | `string` | Output only. [Output only] Create time stamp |
| `ruleNames` | `array` | the name of the rule |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `evaluationsId, locationsId, projectsId` | Gets details of a single Evaluation. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Evaluations in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Evaluation in a given project and location. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists Evaluations in a given project and location. |

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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>evaluations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="workloadmanager.evaluations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | name of resource names have the form 'projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/evaluations/&#123;evaluation_id&#125;' |
| <CopyableCode code="description" /> | `string` | Description of the Evaluation |
| <CopyableCode code="bigQueryDestination" /> | `object` | Message describing big query destination |
| <CopyableCode code="createTime" /> | `string` | Output only. [Output only] Create time stamp |
| <CopyableCode code="customRulesBucket" /> | `string` | The Cloud Storage bucket name for custom rules. |
| <CopyableCode code="labels" /> | `object` | Labels as key value pairs |
| <CopyableCode code="resourceFilter" /> | `object` | Message describing resource filters |
| <CopyableCode code="resourceStatus" /> | `object` | Message describing resource status |
| <CopyableCode code="ruleNames" /> | `array` | the name of the rule |
| <CopyableCode code="ruleVersions" /> | `array` | Output only. [Output only] The updated rule ids if exist. |
| <CopyableCode code="schedule" /> | `string` | crontab format schedule for scheduled evaluation, currently only support the following schedule: "0 */1 * * *", "0 */6 * * *", "0 */12 * * *", "0 0 */1 * *", "0 0 */7 * *", |
| <CopyableCode code="updateTime" /> | `string` | Output only. [Output only] Update time stamp |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="evaluationsId, locationsId, projectsId" /> | Gets details of a single Evaluation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Evaluations in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Evaluation in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="evaluationsId, locationsId, projectsId" /> | Deletes a single Evaluation. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists Evaluations in a given project and location. |

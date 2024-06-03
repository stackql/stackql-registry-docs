---
title: workflow_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_configs
  - dataform
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
<tr><td><b>Name</b></td><td><code>workflow_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataform.workflow_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The workflow config's name. |
| <CopyableCode code="cronSchedule" /> | `string` | Optional. Optional schedule (in cron format) for automatic execution of this workflow config. |
| <CopyableCode code="invocationConfig" /> | `object` | Includes various configuration options for a workflow invocation. If both `included_targets` and `included_tags` are unset, all actions will be included. |
| <CopyableCode code="recentScheduledExecutionRecords" /> | `array` | Output only. Records of the 10 most recent scheduled execution attempts, ordered in in descending order of `execution_time`. Updated whenever automatic creation of a workflow invocation is triggered by cron_schedule. |
| <CopyableCode code="releaseConfig" /> | `string` | Required. The name of the release config whose release_compilation_result should be executed. Must be in the format `projects/*/locations/*/repositories/*/releaseConfigs/*`. |
| <CopyableCode code="timeZone" /> | `string` | Optional. Specifies the time zone to be used when interpreting cron_schedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId, workflowConfigsId" /> | Fetches a single WorkflowConfig. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Lists WorkflowConfigs in a given Repository. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Creates a new WorkflowConfig in a given Repository. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, repositoriesId, workflowConfigsId" /> | Deletes a single WorkflowConfig. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, repositoriesId, workflowConfigsId" /> | Updates a single WorkflowConfig. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Lists WorkflowConfigs in a given Repository. |

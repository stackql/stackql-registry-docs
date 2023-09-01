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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataform.workflow_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The workflow config's name. |
| `cronSchedule` | `string` | Optional. Optional schedule (in cron format) for automatic execution of this workflow config. |
| `invocationConfig` | `object` | Includes various configuration options for a workflow invocation. If both `included_targets` and `included_tags` are unset, all actions will be included. |
| `recentScheduledExecutionRecords` | `array` | Output only. Records of the 10 most recent scheduled execution attempts, ordered in in descending order of `execution_time`. Updated whenever automatic creation of a workflow invocation is triggered by cron_schedule. |
| `releaseConfig` | `string` | Required. The name of the release config whose release_compilation_result should be executed. Must be in the format `projects/*/locations/*/repositories/*/releaseConfigs/*`. |
| `timeZone` | `string` | Optional. Specifies the time zone to be used when interpreting cron_schedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, repositoriesId, workflowConfigsId` | Fetches a single WorkflowConfig. |
| `list` | `SELECT` | `locationsId, projectsId, repositoriesId` | Lists WorkflowConfigs in a given Repository. |
| `create` | `INSERT` | `locationsId, projectsId, repositoriesId` | Creates a new WorkflowConfig in a given Repository. |
| `delete` | `DELETE` | `locationsId, projectsId, repositoriesId, workflowConfigsId` | Deletes a single WorkflowConfig. |
| `_list` | `EXEC` | `locationsId, projectsId, repositoriesId` | Lists WorkflowConfigs in a given Repository. |
| `patch` | `EXEC` | `locationsId, projectsId, repositoriesId, workflowConfigsId` | Updates a single WorkflowConfig. |

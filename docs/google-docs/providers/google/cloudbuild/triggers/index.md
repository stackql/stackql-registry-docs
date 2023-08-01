---
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
  - cloudbuild
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
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudbuild.triggers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `triggers` | `array` | `BuildTriggers` for the project, sorted by `create_time` descending. |
| `nextPageToken` | `string` | Token to receive the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_triggers_list` | `SELECT` | `locationsId, projectsId` | Lists existing `BuildTrigger`s. This API is experimental. |
| `projects_triggers_list` | `SELECT` | `projectId` | Lists existing `BuildTrigger`s. This API is experimental. |
| `projects_locations_triggers_create` | `INSERT` | `locationsId, projectsId` | Creates a new `BuildTrigger`. This API is experimental. |
| `projects_triggers_create` | `INSERT` | `projectId` | Creates a new `BuildTrigger`. This API is experimental. |
| `projects_locations_triggers_delete` | `DELETE` | `locationsId, projectsId, triggersId` | Deletes a `BuildTrigger` by its project ID and trigger ID. This API is experimental. |
| `projects_triggers_delete` | `DELETE` | `projectId, triggerId` | Deletes a `BuildTrigger` by its project ID and trigger ID. This API is experimental. |
| `projects_locations_triggers_get` | `EXEC` | `locationsId, projectsId, triggersId` | Returns information about a `BuildTrigger`. This API is experimental. |
| `projects_locations_triggers_patch` | `EXEC` | `locationsId, projectsId, triggersId` | Updates a `BuildTrigger` by its project ID and trigger ID. This API is experimental. |
| `projects_locations_triggers_run` | `EXEC` | `locationsId, projectsId, triggersId` | Runs a `BuildTrigger` at a particular source revision. To run a regional or global trigger, use the POST request that includes the location endpoint in the path (ex. v1/projects/&#123;projectId&#125;/locations/&#123;region&#125;/triggers/&#123;triggerId&#125;:run). The POST request that does not include the location endpoint in the path can only be used when running global triggers. |
| `projects_locations_triggers_webhook` | `EXEC` | `locationsId, projectsId, triggersId` | ReceiveTriggerWebhook [Experimental] is called when the API receives a webhook request targeted at a specific trigger. |
| `projects_triggers_get` | `EXEC` | `projectId, triggerId` | Returns information about a `BuildTrigger`. This API is experimental. |
| `projects_triggers_patch` | `EXEC` | `projectId, triggerId` | Updates a `BuildTrigger` by its project ID and trigger ID. This API is experimental. |
| `projects_triggers_run` | `EXEC` | `projectId, triggerId` | Runs a `BuildTrigger` at a particular source revision. To run a regional or global trigger, use the POST request that includes the location endpoint in the path (ex. v1/projects/&#123;projectId&#125;/locations/&#123;region&#125;/triggers/&#123;triggerId&#125;:run). The POST request that does not include the location endpoint in the path can only be used when running global triggers. |
| `projects_triggers_webhook` | `EXEC` | `projectId, trigger` | ReceiveTriggerWebhook [Experimental] is called when the API receives a webhook request targeted at a specific trigger. |

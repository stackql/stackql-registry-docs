---
title: experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - experiments
  - dialogflow
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
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.experiments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the experiment. Format: projects//locations//agents//environments//experiments/.. |
| `description` | `string` | The human-readable description of the experiment. |
| `variantsHistory` | `array` | The history of updates to the experiment variants. |
| `createTime` | `string` | Creation time of this experiment. |
| `experimentLength` | `string` | Maximum number of days to run the experiment/rollout. If auto-rollout is not enabled, default value and maximum will be 30 days. If auto-rollout is enabled, default value and maximum will be 6 days. |
| `definition` | `object` | Definition of the experiment. |
| `lastUpdateTime` | `string` | Last update time of this experiment. |
| `endTime` | `string` | End time of this experiment. |
| `state` | `string` | The current state of the experiment. Transition triggered by Experiments.StartExperiment: DRAFT-&gt;RUNNING. Transition triggered by Experiments.CancelExperiment: DRAFT-&gt;DONE or RUNNING-&gt;DONE. |
| `displayName` | `string` | Required. The human-readable name of the experiment (unique in an environment). Limit of 64 characters. |
| `startTime` | `string` | Start time of this experiment. |
| `rolloutConfig` | `object` | The configuration for auto rollout. |
| `rolloutFailureReason` | `string` | The reason why rollout has failed. Should only be set when state is ROLLOUT_FAILED. |
| `result` | `object` | The inference result which includes an objective metric to optimize and the confidence interval. |
| `rolloutState` | `object` | State of the auto-rollout process. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_environments_experiments_get` | `SELECT` | `agentsId, environmentsId, experimentsId, locationsId, projectsId` | Retrieves the specified Experiment. |
| `projects_locations_agents_environments_experiments_list` | `SELECT` | `agentsId, environmentsId, locationsId, projectsId` | Returns the list of all experiments in the specified Environment. |
| `projects_locations_agents_environments_experiments_create` | `INSERT` | `agentsId, environmentsId, locationsId, projectsId` | Creates an Experiment in the specified Environment. |
| `projects_locations_agents_environments_experiments_delete` | `DELETE` | `agentsId, environmentsId, experimentsId, locationsId, projectsId` | Deletes the specified Experiment. |
| `projects_locations_agents_environments_experiments_patch` | `EXEC` | `agentsId, environmentsId, experimentsId, locationsId, projectsId` | Updates the specified Experiment. |
| `projects_locations_agents_environments_experiments_start` | `EXEC` | `agentsId, environmentsId, experimentsId, locationsId, projectsId` | Starts the specified Experiment. This rpc only changes the state of experiment from PENDING to RUNNING. |
| `projects_locations_agents_environments_experiments_stop` | `EXEC` | `agentsId, environmentsId, experimentsId, locationsId, projectsId` | Stops the specified Experiment. This rpc only changes the state of experiment from RUNNING to DONE. |

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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.experiments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the experiment. Format: projects//locations//agents//environments//experiments/.. |
| <CopyableCode code="description" /> | `string` | The human-readable description of the experiment. |
| <CopyableCode code="createTime" /> | `string` | Creation time of this experiment. |
| <CopyableCode code="definition" /> | `object` | Definition of the experiment. |
| <CopyableCode code="displayName" /> | `string` | Required. The human-readable name of the experiment (unique in an environment). Limit of 64 characters. |
| <CopyableCode code="endTime" /> | `string` | End time of this experiment. |
| <CopyableCode code="experimentLength" /> | `string` | Maximum number of days to run the experiment/rollout. If auto-rollout is not enabled, default value and maximum will be 30 days. If auto-rollout is enabled, default value and maximum will be 6 days. |
| <CopyableCode code="lastUpdateTime" /> | `string` | Last update time of this experiment. |
| <CopyableCode code="result" /> | `object` | The inference result which includes an objective metric to optimize and the confidence interval. |
| <CopyableCode code="rolloutConfig" /> | `object` | The configuration for auto rollout. |
| <CopyableCode code="rolloutFailureReason" /> | `string` | The reason why rollout has failed. Should only be set when state is ROLLOUT_FAILED. |
| <CopyableCode code="rolloutState" /> | `object` | State of the auto-rollout process. |
| <CopyableCode code="startTime" /> | `string` | Start time of this experiment. |
| <CopyableCode code="state" /> | `string` | The current state of the experiment. Transition triggered by Experiments.StartExperiment: DRAFT-&gt;RUNNING. Transition triggered by Experiments.CancelExperiment: DRAFT-&gt;DONE or RUNNING-&gt;DONE. |
| <CopyableCode code="variantsHistory" /> | `array` | The history of updates to the experiment variants. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_environments_experiments_get" /> | `SELECT` | <CopyableCode code="agentsId, environmentsId, experimentsId, locationsId, projectsId" /> | Retrieves the specified Experiment. |
| <CopyableCode code="projects_locations_agents_environments_experiments_list" /> | `SELECT` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId" /> | Returns the list of all experiments in the specified Environment. |
| <CopyableCode code="projects_locations_agents_environments_experiments_create" /> | `INSERT` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId" /> | Creates an Experiment in the specified Environment. |
| <CopyableCode code="projects_locations_agents_environments_experiments_delete" /> | `DELETE` | <CopyableCode code="agentsId, environmentsId, experimentsId, locationsId, projectsId" /> | Deletes the specified Experiment. |
| <CopyableCode code="_projects_locations_agents_environments_experiments_list" /> | `EXEC` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId" /> | Returns the list of all experiments in the specified Environment. |
| <CopyableCode code="projects_locations_agents_environments_experiments_patch" /> | `EXEC` | <CopyableCode code="agentsId, environmentsId, experimentsId, locationsId, projectsId" /> | Updates the specified Experiment. |
| <CopyableCode code="projects_locations_agents_environments_experiments_start" /> | `EXEC` | <CopyableCode code="agentsId, environmentsId, experimentsId, locationsId, projectsId" /> | Starts the specified Experiment. This rpc only changes the state of experiment from PENDING to RUNNING. |
| <CopyableCode code="projects_locations_agents_environments_experiments_stop" /> | `EXEC` | <CopyableCode code="agentsId, environmentsId, experimentsId, locationsId, projectsId" /> | Stops the specified Experiment. This rpc only changes the state of experiment from RUNNING to DONE. |

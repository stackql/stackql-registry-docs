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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.experiments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `experiments` | `array` | The list of experiments. There will be a maximum number of items returned based on the page_size field in the request. The list may in some cases be empty or contain fewer entries than page_size even if this isn't the last page. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
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

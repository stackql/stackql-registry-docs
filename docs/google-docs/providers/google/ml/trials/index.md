---
title: trials
hide_title: false
hide_table_of_contents: false
keywords:
  - trials
  - ml
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
<tr><td><b>Name</b></td><td><code>trials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.ml.trials</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_studies_trials_get` | `SELECT` | `locationsId, projectsId, studiesId, trialsId` | Gets a trial. |
| `projects_locations_studies_trials_list` | `SELECT` | `locationsId, projectsId, studiesId` | Lists the trials associated with a study. |
| `projects_locations_studies_trials_create` | `INSERT` | `locationsId, projectsId, studiesId` | Adds a user provided trial to a study. |
| `projects_locations_studies_trials_delete` | `DELETE` | `locationsId, projectsId, studiesId, trialsId` | Deletes a trial. |
| `projects_locations_studies_trials_check_early_stopping_state` | `EXEC` | `locationsId, projectsId, studiesId, trialsId` | Checks whether a trial should stop or not. Returns a long-running operation. When the operation is successful, it will contain a CheckTrialEarlyStoppingStateResponse. |
| `projects_locations_studies_trials_complete` | `EXEC` | `locationsId, projectsId, studiesId, trialsId` | Marks a trial as complete. |
| `projects_locations_studies_trials_stop` | `EXEC` | `locationsId, projectsId, studiesId, trialsId` | Stops a trial. |
| `projects_locations_studies_trials_suggest` | `EXEC` | `locationsId, projectsId, studiesId` | Adds one or more trials to a study, with parameter values suggested by AI Platform Vizier. Returns a long-running operation associated with the generation of trial suggestions. When this long-running operation succeeds, it will contain a SuggestTrialsResponse. |

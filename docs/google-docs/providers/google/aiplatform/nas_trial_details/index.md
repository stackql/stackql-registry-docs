---
title: nas_trial_details
hide_title: false
hide_table_of_contents: false
keywords:
  - nas_trial_details
  - aiplatform
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
<tr><td><b>Name</b></td><td><code>nas_trial_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.nas_trial_details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the NasTrialDetail. |
| `trainTrial` | `object` | Represents a uCAIP NasJob trial. |
| `parameters` | `string` | The parameters for the NasJob NasTrial. |
| `searchTrial` | `object` | Represents a uCAIP NasJob trial. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, nasJobsId, nasTrialDetailsId, projectsId` | Gets a NasTrialDetail. |
| `list` | `SELECT` | `locationsId, nasJobsId, projectsId` | List top NasTrialDetails of a NasJob. |
| `_list` | `EXEC` | `locationsId, nasJobsId, projectsId` | List top NasTrialDetails of a NasJob. |

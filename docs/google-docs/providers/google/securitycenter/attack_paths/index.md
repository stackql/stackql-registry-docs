---
title: attack_paths
hide_title: false
hide_table_of_contents: false
keywords:
  - attack_paths
  - securitycenter
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
<tr><td><b>Name</b></td><td><code>attack_paths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.attack_paths</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results. |
| `attackPaths` | `array` | The attack paths that the attack path simulation identified. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_simulations_attack_exposure_results_attack_paths_list` | `SELECT` | `attackExposureResultsId, organizationsId, simulationsId` |
| `organizations_simulations_attack_paths_list` | `SELECT` | `organizationsId, simulationsId` |
| `organizations_simulations_valued_resources_attack_paths_list` | `SELECT` | `organizationsId, simulationsId, valuedResourcesId` |

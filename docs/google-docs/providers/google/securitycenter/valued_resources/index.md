---
title: valued_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - valued_resources
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
<tr><td><b>Name</b></td><td><code>valued_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.valued_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `totalSize` | `integer` | The estimated total number of results matching the query. |
| `valuedResources` | `array` | The valued resources that the attack path simulation identified. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_simulations_attack_exposure_results_valued_resources_list` | `SELECT` | `attackExposureResultsId, organizationsId, simulationsId` |
| `organizations_simulations_valued_resources_list` | `SELECT` | `organizationsId, simulationsId` |

---
title: results
hide_title: false
hide_table_of_contents: false
keywords:
  - results
  - policysimulator
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
<tr><td><b>Name</b></td><td><code>results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.policysimulator.results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token that you can use to retrieve the next page of ReplayResult objects. If this field is omitted, there are no subsequent pages. |
| `replayResults` | `array` | The results of running a Replay. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `folders_locations_replays_results_list` | `SELECT` | `foldersId, locationsId, replaysId` |
| `organizations_locations_replays_results_list` | `SELECT` | `locationsId, organizationsId, replaysId` |
| `projects_locations_replays_results_list` | `SELECT` | `locationsId, projectsId, replaysId` |

---
title: workstation_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - workstation_clusters
  - workstations
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
<tr><td><b>Name</b></td><td><code>workstation_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workstations.workstation_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `workstationClusters` | `array` | The requested workstation clusters. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `unreachable` | `array` | Unreachable resources. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, workstationClustersId` | Returns the requested workstation cluster. |
| `list` | `SELECT` | `locationsId, projectsId` | Returns all workstation clusters in the specified location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new workstation cluster. |
| `delete` | `DELETE` | `locationsId, projectsId, workstationClustersId` | Deletes the specified workstation cluster. |
| `patch` | `EXEC` | `locationsId, projectsId, workstationClustersId` | Updates an existing workstation cluster. |

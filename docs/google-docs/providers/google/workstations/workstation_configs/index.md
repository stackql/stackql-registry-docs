---
title: workstation_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - workstation_configs
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
<tr><td><b>Name</b></td><td><code>workstation_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workstations.workstation_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `workstationConfigs` | `array` | The requested configs. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `unreachable` | `array` | Unreachable resources. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` | Returns the requested workstation configuration. |
| `list` | `SELECT` | `locationsId, projectsId, workstationClustersId` | Returns all workstation configurations in the specified cluster. |
| `create` | `INSERT` | `locationsId, projectsId, workstationClustersId` | Creates a new workstation configuration. |
| `delete` | `DELETE` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` | Deletes the specified workstation configuration. |
| `patch` | `EXEC` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` | Updates an existing workstation configuration. |

---
title: workstations
hide_title: false
hide_table_of_contents: false
keywords:
  - workstations
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
<tr><td><b>Name</b></td><td><code>workstations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workstations.workstations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `unreachable` | `array` | Unreachable resources. |
| `workstations` | `array` | The requested workstations. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId` | Returns the requested workstation. |
| `list` | `SELECT` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` | Returns all Workstations using the specified workstation configuration. |
| `create` | `INSERT` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` | Creates a new workstation. |
| `delete` | `DELETE` | `locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId` | Deletes the specified workstation. |
| `generate_access_token` | `EXEC` | `locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId` | Returns a short-lived credential that can be used to send authenticated and authorized traffic to a workstation. |
| `patch` | `EXEC` | `locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId` | Updates an existing workstation. |
| `start` | `EXEC` | `locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId` | Starts running a workstation so that users can connect to it. |
| `stop` | `EXEC` | `locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId` | Stops running a workstation, reducing costs. |

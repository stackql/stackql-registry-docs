---
title: usable
hide_title: false
hide_table_of_contents: false
keywords:
  - usable
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
<tr><td><b>Name</b></td><td><code>usable</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workstations.usable</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `workstations` | `array` | The requested workstations. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `unreachable` | `array` | Unreachable resources. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_workstationClusters_workstationConfigs_workstations_listUsable` | `SELECT` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` |

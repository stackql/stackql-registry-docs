---
title: workstation_configs_usable
hide_title: false
hide_table_of_contents: false
keywords:
  - workstation_configs_usable
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
<tr><td><b>Name</b></td><td><code>workstation_configs_usable</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workstations.workstation_configs_usable</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `unreachable` | `array` | Unreachable resources. |
| `workstationConfigs` | `array` | The requested configs. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_usable` | `SELECT` | `locationsId, projectsId, workstationClustersId` |

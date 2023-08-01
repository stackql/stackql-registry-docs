---
title: service_level_objectives
hide_title: false
hide_table_of_contents: false
keywords:
  - service_level_objectives
  - monitoring
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
<tr><td><b>Name</b></td><td><code>service_level_objectives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.monitoring.service_level_objectives</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `serviceLevelObjectives` | `array` | The ServiceLevelObjectives matching the specified filter. |
| `nextPageToken` | `string` | If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as page_token in the next call to this method. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `services_service_level_objectives_list` | `SELECT` | `parent` | List the ServiceLevelObjectives for the given Service. |
| `services_service_level_objectives_create` | `INSERT` | `parent` | Create a ServiceLevelObjective for the given Service. |
| `services_service_level_objectives_delete` | `DELETE` | `name` | Delete the given ServiceLevelObjective. |
| `services_service_level_objectives_get` | `EXEC` | `name` | Get a ServiceLevelObjective by name. |
| `services_service_level_objectives_patch` | `EXEC` | `name` | Update the given ServiceLevelObjective. |

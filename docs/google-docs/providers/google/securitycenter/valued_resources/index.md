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
| `name` | `string` | Valued resource name, for example, e.g.: `organizations/123/simulations/456/valuedResources/789` |
| `resourceValueConfigsUsed` | `array` | List of resource value configurations' metadata used to determine the value of this resource. Maximum of 100. |
| `displayName` | `string` | Human-readable name of the valued resource. |
| `exposedScore` | `number` | Exposed score for this valued resource. A value of 0 means no exposure was detected exposure. |
| `resource` | `string` | The [full resource name](https://cloud.google.com/apis/design/resource_names#full_resource_name) of the valued resource. |
| `resourceType` | `string` | The [resource type](https://cloud.google.com/asset-inventory/docs/supported-asset-types) of the valued resource. |
| `resourceValue` | `string` | How valuable this resource is. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_simulations_attack_exposure_results_valued_resources_list` | `SELECT` | `attackExposureResultsId, organizationsId, simulationsId` |
| `organizations_simulations_valued_resources_list` | `SELECT` | `organizationsId, simulationsId` |
| `_organizations_simulations_attack_exposure_results_valued_resources_list` | `EXEC` | `attackExposureResultsId, organizationsId, simulationsId` |
| `_organizations_simulations_valued_resources_list` | `EXEC` | `organizationsId, simulationsId` |

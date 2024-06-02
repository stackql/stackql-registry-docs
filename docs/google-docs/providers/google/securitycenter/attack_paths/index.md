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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attack_paths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="securitycenter.attack_paths" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The attack path name, for example, `organizations/12/simulation/34/valuedResources/56/attackPaths/78` |
| <CopyableCode code="edges" /> | `array` | A list of the edges between nodes in this attack path. |
| <CopyableCode code="pathNodes" /> | `array` | A list of nodes that exist in this attack path. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="organizations_simulations_attack_exposure_results_attack_paths_list" /> | `SELECT` | <CopyableCode code="attackExposureResultsId, organizationsId, simulationsId" /> |
| <CopyableCode code="organizations_simulations_attack_paths_list" /> | `SELECT` | <CopyableCode code="organizationsId, simulationsId" /> |
| <CopyableCode code="organizations_simulations_valued_resources_attack_paths_list" /> | `SELECT` | <CopyableCode code="organizationsId, simulationsId, valuedResourcesId" /> |
| <CopyableCode code="_organizations_simulations_attack_exposure_results_attack_paths_list" /> | `EXEC` | <CopyableCode code="attackExposureResultsId, organizationsId, simulationsId" /> |
| <CopyableCode code="_organizations_simulations_attack_paths_list" /> | `EXEC` | <CopyableCode code="organizationsId, simulationsId" /> |
| <CopyableCode code="_organizations_simulations_valued_resources_attack_paths_list" /> | `EXEC` | <CopyableCode code="organizationsId, simulationsId, valuedResourcesId" /> |

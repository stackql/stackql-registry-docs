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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>attack_paths</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attack_paths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.attack_paths" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The attack path name, for example, `organizations/12/simulation/34/valuedResources/56/attackPaths/78` |
| <CopyableCode code="edges" /> | `array` | A list of the edges between nodes in this attack path. |
| <CopyableCode code="pathNodes" /> | `array` | A list of nodes that exist in this attack path. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_simulations_attack_exposure_results_attack_paths_list" /> | `SELECT` | <CopyableCode code="attackExposureResultsId, organizationsId, simulationsId" /> | Lists the attack paths for a set of simulation results or valued resources and filter. |
| <CopyableCode code="organizations_simulations_attack_paths_list" /> | `SELECT` | <CopyableCode code="organizationsId, simulationsId" /> | Lists the attack paths for a set of simulation results or valued resources and filter. |
| <CopyableCode code="organizations_simulations_valued_resources_attack_paths_list" /> | `SELECT` | <CopyableCode code="organizationsId, simulationsId, valuedResourcesId" /> | Lists the attack paths for a set of simulation results or valued resources and filter. |

## `SELECT` examples

Lists the attack paths for a set of simulation results or valued resources and filter.

```sql
SELECT
name,
edges,
pathNodes
FROM google.securitycenter.attack_paths
WHERE organizationsId = '{{ organizationsId }}'
AND simulationsId = '{{ simulationsId }}';
```

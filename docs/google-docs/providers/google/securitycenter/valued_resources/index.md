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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>valued_resource</code> resource or lists <code>valued_resources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>valued_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.valued_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Valued resource name, for example, e.g.: `organizations/123/simulations/456/valuedResources/789` |
| <CopyableCode code="displayName" /> | `string` | Human-readable name of the valued resource. |
| <CopyableCode code="exposedScore" /> | `number` | Exposed score for this valued resource. A value of 0 means no exposure was detected exposure. |
| <CopyableCode code="resource" /> | `string` | The [full resource name](https://cloud.google.com/apis/design/resource_names#full_resource_name) of the valued resource. |
| <CopyableCode code="resourceType" /> | `string` | The [resource type](https://cloud.google.com/asset-inventory/docs/supported-asset-types) of the valued resource. |
| <CopyableCode code="resourceValue" /> | `string` | How valuable this resource is. |
| <CopyableCode code="resourceValueConfigsUsed" /> | `array` | List of resource value configurations' metadata used to determine the value of this resource. Maximum of 100. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_simulations_attack_exposure_results_valued_resources_list" /> | `SELECT` | <CopyableCode code="attackExposureResultsId, organizationsId, simulationsId" /> | Lists the valued resources for a set of simulation results and filter. |
| <CopyableCode code="organizations_simulations_valued_resources_get" /> | `SELECT` | <CopyableCode code="organizationsId, simulationsId, valuedResourcesId" /> | Get the valued resource by name |
| <CopyableCode code="organizations_simulations_valued_resources_list" /> | `SELECT` | <CopyableCode code="organizationsId, simulationsId" /> | Lists the valued resources for a set of simulation results and filter. |
| <CopyableCode code="organizations_valued_resources_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists the valued resources for a set of simulation results and filter. |

## `SELECT` examples

Lists the valued resources for a set of simulation results and filter.

```sql
SELECT
name,
displayName,
exposedScore,
resource,
resourceType,
resourceValue,
resourceValueConfigsUsed
FROM google.securitycenter.valued_resources
WHERE organizationsId = '{{ organizationsId }}'; 
```

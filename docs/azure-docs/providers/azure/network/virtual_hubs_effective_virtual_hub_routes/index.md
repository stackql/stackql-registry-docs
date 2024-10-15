---
title: virtual_hubs_effective_virtual_hub_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hubs_effective_virtual_hub_routes
  - network
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

Creates, updates, deletes, gets or lists a <code>virtual_hubs_effective_virtual_hub_routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_hubs_effective_virtual_hub_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_hubs_effective_virtual_hub_routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="addressPrefixes" /> | `array` | The list of address prefixes. |
| <CopyableCode code="asPath" /> | `string` | The ASPath of this route. |
| <CopyableCode code="nextHopType" /> | `string` | The type of the next hop. |
| <CopyableCode code="nextHops" /> | `array` | The list of next hops. |
| <CopyableCode code="routeOrigin" /> | `string` | The origin of this route. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Gets the effective routes configured for the Virtual Hub resource or the specified resource . |

## `SELECT` examples

Gets the effective routes configured for the Virtual Hub resource or the specified resource .


```sql
SELECT
addressPrefixes,
asPath,
nextHopType,
nextHops,
routeOrigin
FROM azure.network.virtual_hubs_effective_virtual_hub_routes
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
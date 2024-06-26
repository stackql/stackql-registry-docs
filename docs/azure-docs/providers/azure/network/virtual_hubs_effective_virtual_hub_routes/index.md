---
title: virtual_hubs_effective_virtual_hub_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hubs_effective_virtual_hub_routes
  - network
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> |

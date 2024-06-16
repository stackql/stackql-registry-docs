---
title: express_route_cross_connections_routes_table_summary
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_cross_connections_routes_table_summary
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
<tr><td><b>Name</b></td><td><code>express_route_cross_connections_routes_table_summary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_cross_connections_routes_table_summary" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="asn" /> | `integer` | Autonomous system number. |
| <CopyableCode code="neighbor" /> | `string` | IP address of Neighbor router. |
| <CopyableCode code="stateOrPrefixesReceived" /> | `string` | Current state of the BGP session, and the number of prefixes that have been received from a neighbor or peer group. |
| <CopyableCode code="upDown" /> | `string` | The length of time that the BGP session has been in the Established state, or the current status if not in the Established state. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="crossConnectionName, devicePath, peeringName, resourceGroupName, subscriptionId" /> |

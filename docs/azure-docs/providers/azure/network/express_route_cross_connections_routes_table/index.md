---
title: express_route_cross_connections_routes_table
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_cross_connections_routes_table
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
<tr><td><b>Name</b></td><td><code>express_route_cross_connections_routes_table</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_cross_connections_routes_table" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="locPrf" /> | `string` | Local preference value as set with the set local-preference route-map configuration command. |
| <CopyableCode code="network" /> | `string` | IP address of a network entity. |
| <CopyableCode code="nextHop" /> | `string` | NextHop address. |
| <CopyableCode code="path" /> | `string` | Autonomous system paths to the destination network. |
| <CopyableCode code="weight" /> | `integer` | Route Weight. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="crossConnectionName, devicePath, peeringName, resourceGroupName, subscriptionId" /> |

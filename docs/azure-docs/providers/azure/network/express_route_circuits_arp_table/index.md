---
title: express_route_circuits_arp_table
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuits_arp_table
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
<tr><td><b>Name</b></td><td><code>express_route_circuits_arp_table</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_circuits_arp_table" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="age" /> | `integer` | Entry age in minutes. |
| <CopyableCode code="interface" /> | `string` | Interface address. |
| <CopyableCode code="ipAddress" /> | `string` | The IP address. |
| <CopyableCode code="macAddress" /> | `string` | The MAC address. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="circuitName, devicePath, peeringName, resourceGroupName, subscriptionId" /> |

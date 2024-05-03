---
title: express_route_circuits_stats
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuits_stats
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
<tr><td><b>Name</b></td><td><code>express_route_circuits_stats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_circuits_stats" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="primarybytesIn" /> | `integer` | The Primary BytesIn of the peering. |
| <CopyableCode code="primarybytesOut" /> | `integer` | The primary BytesOut of the peering. |
| <CopyableCode code="secondarybytesIn" /> | `integer` | The secondary BytesIn of the peering. |
| <CopyableCode code="secondarybytesOut" /> | `integer` | The secondary BytesOut of the peering. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="circuitName, resourceGroupName, subscriptionId" /> |

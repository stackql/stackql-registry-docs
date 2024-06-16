---
title: virtual_networks_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks_usage
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
<tr><td><b>Name</b></td><td><code>virtual_networks_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_networks_usage" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Subnet identifier. |
| <CopyableCode code="name" /> | `object` | Usage strings container. |
| <CopyableCode code="currentValue" /> | `number` | Indicates number of IPs used from the Subnet. |
| <CopyableCode code="limit" /> | `number` | Indicates the size of the subnet. |
| <CopyableCode code="unit" /> | `string` | Usage units. Returns 'Count'. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName" /> |

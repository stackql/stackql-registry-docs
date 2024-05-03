---
title: data_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - data_networks
  - mobile_network
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
<tr><td><b>Name</b></td><td><code>data_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.data_networks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Data network properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataNetworkName, mobileNetworkName, resourceGroupName, subscriptionId" /> | Gets information about the specified data network. |
| <CopyableCode code="list_by_mobile_network" /> | `SELECT` | <CopyableCode code="mobileNetworkName, resourceGroupName, subscriptionId" /> | Lists all data networks in the mobile network. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataNetworkName, mobileNetworkName, resourceGroupName, subscriptionId" /> | Creates or updates a data network. Must be created in the same location as its parent mobile network. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataNetworkName, mobileNetworkName, resourceGroupName, subscriptionId" /> | Deletes the specified data network. |
| <CopyableCode code="_list_by_mobile_network" /> | `EXEC` | <CopyableCode code="mobileNetworkName, resourceGroupName, subscriptionId" /> | Lists all data networks in the mobile network. |

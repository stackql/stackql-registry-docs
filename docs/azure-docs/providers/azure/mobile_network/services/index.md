---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Service properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="mobileNetworkName, resourceGroupName, serviceName, subscriptionId" /> | Gets information about the specified service. |
| <CopyableCode code="list_by_mobile_network" /> | `SELECT` | <CopyableCode code="mobileNetworkName, resourceGroupName, subscriptionId" /> | Gets all the services in a mobile network. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="mobileNetworkName, resourceGroupName, serviceName, subscriptionId, data__properties" /> | Creates or updates a service. Must be created in the same location as its parent mobile network. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="mobileNetworkName, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified service. |
| <CopyableCode code="_list_by_mobile_network" /> | `EXEC` | <CopyableCode code="mobileNetworkName, resourceGroupName, subscriptionId" /> | Gets all the services in a mobile network. |

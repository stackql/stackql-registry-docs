---
title: associations_interface
hide_title: false
hide_table_of_contents: false
keywords:
  - associations_interface
  - service_networking
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
<tr><td><b>Name</b></td><td><code>associations_interface</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_networking.associations_interface" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Association Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="associationName, resourceGroupName, subscriptionId, trafficControllerName" /> | Get a Association |
| <CopyableCode code="list_by_traffic_controller" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, trafficControllerName" /> | List Association resources by TrafficController |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="associationName, resourceGroupName, subscriptionId, trafficControllerName" /> | Create a Association |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="associationName, resourceGroupName, subscriptionId, trafficControllerName" /> | Delete a Association |
| <CopyableCode code="_list_by_traffic_controller" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, trafficControllerName" /> | List Association resources by TrafficController |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="associationName, resourceGroupName, subscriptionId, trafficControllerName" /> | Update a Association |

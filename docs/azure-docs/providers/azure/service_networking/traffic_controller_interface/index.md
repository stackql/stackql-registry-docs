---
title: traffic_controller_interface
hide_title: false
hide_table_of_contents: false
keywords:
  - traffic_controller_interface
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
<tr><td><b>Name</b></td><td><code>traffic_controller_interface</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_networking.traffic_controller_interface" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Traffic Controller Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, trafficControllerName" /> | Get a TrafficController |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List TrafficController resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List TrafficController resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, trafficControllerName" /> | Create a TrafficController |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, trafficControllerName" /> | Delete a TrafficController |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List TrafficController resources by resource group |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List TrafficController resources by subscription ID |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, trafficControllerName" /> | Update a TrafficController |

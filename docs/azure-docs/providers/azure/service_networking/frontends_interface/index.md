---
title: frontends_interface
hide_title: false
hide_table_of_contents: false
keywords:
  - frontends_interface
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
<tr><td><b>Name</b></td><td><code>frontends_interface</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_networking.frontends_interface" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Frontend Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="frontendName, resourceGroupName, subscriptionId, trafficControllerName" /> | Get a Frontend |
| <CopyableCode code="list_by_traffic_controller" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, trafficControllerName" /> | List Frontend resources by TrafficController |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="frontendName, resourceGroupName, subscriptionId, trafficControllerName" /> | Create a Frontend |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="frontendName, resourceGroupName, subscriptionId, trafficControllerName" /> | Delete a Frontend |
| <CopyableCode code="_list_by_traffic_controller" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, trafficControllerName" /> | List Frontend resources by TrafficController |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="frontendName, resourceGroupName, subscriptionId, trafficControllerName" /> | Update a Frontend |

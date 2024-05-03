---
title: frontend_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - frontend_endpoints
  - front_door
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
<tr><td><b>Name</b></td><td><code>frontend_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.front_door.frontend_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties required to create a frontend endpoint. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="frontDoorName, frontendEndpointName, resourceGroupName, subscriptionId" /> | Gets a Frontend endpoint with the specified name within the specified Front Door. |
| <CopyableCode code="list_by_front_door" /> | `SELECT` | <CopyableCode code="frontDoorName, resourceGroupName, subscriptionId" /> | Lists all of the frontend endpoints within a Front Door. |
| <CopyableCode code="_list_by_front_door" /> | `EXEC` | <CopyableCode code="frontDoorName, resourceGroupName, subscriptionId" /> | Lists all of the frontend endpoints within a Front Door. |
| <CopyableCode code="disable_https" /> | `EXEC` | <CopyableCode code="frontDoorName, frontendEndpointName, resourceGroupName, subscriptionId" /> | Disables a frontendEndpoint for HTTPS traffic |
| <CopyableCode code="enable_https" /> | `EXEC` | <CopyableCode code="frontDoorName, frontendEndpointName, resourceGroupName, subscriptionId, data__certificateSource, data__minimumTlsVersion, data__protocolType" /> | Enables a frontendEndpoint for HTTPS traffic |

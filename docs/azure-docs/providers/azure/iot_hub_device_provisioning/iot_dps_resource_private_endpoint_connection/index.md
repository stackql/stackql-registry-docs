---
title: iot_dps_resource_private_endpoint_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_dps_resource_private_endpoint_connection
  - iot_hub_device_provisioning
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
<tr><td><b>Name</b></td><td><code>iot_dps_resource_private_endpoint_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub_device_provisioning.iot_dps_resource_private_endpoint_connection" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="properties" /> | `object` | The properties of a private endpoint connection |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId" /> | Get private endpoint connection properties |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Create or update the status of a private endpoint connection with the specified name |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId" /> | Delete private endpoint connection with the specified name |

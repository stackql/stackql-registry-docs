---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - iot_hub
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="properties" /> | `object` | The properties of a private endpoint connection |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId" /> | Get private endpoint connection properties |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | List private endpoint connection properties |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId" /> | Delete private endpoint connection with the specified name |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Update the status of a private endpoint connection with the specified name |

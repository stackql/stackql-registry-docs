---
title: private_endpoint_connection_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connection_proxies
  - device_update
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connection_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.device_update.private_endpoint_connection_proxies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="eTag" /> | `string` | ETag from NRP. |
| <CopyableCode code="properties" /> | `object` | Private endpoint connection proxy object property bag. |
| <CopyableCode code="remotePrivateEndpoint" /> | `object` | Remote private endpoint details. |
| <CopyableCode code="status" /> | `string` | Operation status. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, privateEndpointConnectionProxyId, resourceGroupName, subscriptionId" /> | (INTERNAL - DO NOT USE) Get the specified private endpoint connection proxy associated with the device update account. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | (INTERNAL - DO NOT USE) List all private endpoint connection proxies in a device update account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, privateEndpointConnectionProxyId, resourceGroupName, subscriptionId" /> | (INTERNAL - DO NOT USE) Creates or updates the specified private endpoint connection proxy resource associated with the device update account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, privateEndpointConnectionProxyId, resourceGroupName, subscriptionId" /> | (INTERNAL - DO NOT USE) Deletes the specified private endpoint connection proxy associated with the device update account. |
| <CopyableCode code="_list_by_account" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | (INTERNAL - DO NOT USE) List all private endpoint connection proxies in a device update account. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="accountName, privateEndpointConnectionProxyId, resourceGroupName, subscriptionId" /> | (INTERNAL - DO NOT USE) Validates a private endpoint connection proxy object. |

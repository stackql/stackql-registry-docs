---
title: api_gateway_config_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - api_gateway_config_connection
  - api_management
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
<tr><td><b>Name</b></td><td><code>api_gateway_config_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.api_gateway_config_connection" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | ETag of the resource. |
| <CopyableCode code="properties" /> | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configConnectionName, gatewayName, resourceGroupName, subscriptionId" /> | Gets an API Management gateway config connection resource description. |
| <CopyableCode code="list_by_gateway" /> | `SELECT` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | List all API Management gateway config connections within a gateway. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configConnectionName, gatewayName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an API Management gateway config connection. This is long running operation and could take several minutes to complete. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, configConnectionName, gatewayName, resourceGroupName, subscriptionId" /> | Deletes an existing API Management gateway config connection. |

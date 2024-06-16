---
title: gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway
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
<tr><td><b>Name</b></td><td><code>gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.gateway" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the Gateway specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of gateways registered with service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates a Gateway to be used in Api Management instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Deletes specific Gateway. |
| <CopyableCode code="generate_token" /> | `EXEC` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId, data__expiry, data__keyType" /> | Gets the Shared Access Authorization Token for the gateway. |
| <CopyableCode code="invalidate_debug_credentials" /> | `EXEC` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Action is invalidating all debug credentials issued for gateway. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId, data__keyType" /> | Regenerates specified gateway key invalidating any tokens created with it. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Updates the details of the gateway specified by its identifier. |

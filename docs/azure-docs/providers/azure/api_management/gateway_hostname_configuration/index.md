---
title: gateway_hostname_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_hostname_configuration
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
<tr><td><b>Name</b></td><td><code>gateway_hostname_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.gateway_hostname_configuration" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayId, hcId, resourceGroupName, serviceName, subscriptionId" /> | Get details of a hostname configuration |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Lists the collection of hostname configurations for the specified gateway. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="gatewayId, hcId, resourceGroupName, serviceName, subscriptionId" /> | Creates of updates hostname configuration for a Gateway. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, gatewayId, hcId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified hostname configuration from the specified Gateway. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="gatewayId, resourceGroupName, serviceName, subscriptionId" /> | Lists the collection of hostname configurations for the specified gateway. |

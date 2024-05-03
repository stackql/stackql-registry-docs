---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.gateways" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Spring Cloud Gateway properties payload |
| <CopyableCode code="sku" /> | `object` | Sku of Azure Spring Apps |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayName, resourceGroupName, serviceName, subscriptionId" /> | Get the Spring Cloud Gateway and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in a Service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="gatewayName, resourceGroupName, serviceName, subscriptionId" /> | Create the default Spring Cloud Gateway or update the existing Spring Cloud Gateway. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="gatewayName, resourceGroupName, serviceName, subscriptionId" /> | Disable the default Spring Cloud Gateway. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in a Service. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="gatewayName, resourceGroupName, serviceName, subscriptionId" /> | Restart the Spring Cloud Gateway. |
| <CopyableCode code="validate_domain" /> | `EXEC` | <CopyableCode code="gatewayName, resourceGroupName, serviceName, subscriptionId, data__name" /> | Check the domains are valid as well as not in use. |

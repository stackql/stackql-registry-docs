---
title: web_apps_hybrid_connection_slot
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_hybrid_connection_slot
  - app_service
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
<tr><td><b>Name</b></td><td><code>web_apps_hybrid_connection_slot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.web_apps_hybrid_connection_slot" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | HybridConnection resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, namespaceName, relayName, resourceGroupName, slot, subscriptionId" /> | Description for Retrieves a specific Service Bus Hybrid Connection used by this Web App. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, namespaceName, relayName, resourceGroupName, slot, subscriptionId" /> | Description for Creates a new Hybrid Connection using a Service Bus relay. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, namespaceName, relayName, resourceGroupName, slot, subscriptionId" /> | Description for Removes a Hybrid Connection from this site. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="name, namespaceName, relayName, resourceGroupName, slot, subscriptionId" /> | Description for Creates a new Hybrid Connection using a Service Bus relay. |

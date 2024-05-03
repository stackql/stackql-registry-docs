---
title: backend
hide_title: false
hide_table_of_contents: false
keywords:
  - backend
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
<tr><td><b>Name</b></td><td><code>backend</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.backend" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backendId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the backend specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of backends in the specified service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="backendId, resourceGroupName, serviceName, subscriptionId" /> | Creates or Updates a backend. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, backendId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified backend. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of backends in the specified service instance. |
| <CopyableCode code="reconnect" /> | `EXEC` | <CopyableCode code="backendId, resourceGroupName, serviceName, subscriptionId" /> | Notifies the API Management gateway to create a new connection to the backend after the specified timeout. If no timeout was specified, timeout of 2 minutes is used. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, backendId, resourceGroupName, serviceName, subscriptionId" /> | Updates an existing backend. |

---
title: authorization_server
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_server
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
<tr><td><b>Name</b></td><td><code>authorization_server</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.authorization_server" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authsid, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the authorization server specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of authorization servers defined within a service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authsid, resourceGroupName, serviceName, subscriptionId" /> | Creates new authorization server or updates an existing authorization server. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, authsid, resourceGroupName, serviceName, subscriptionId" /> | Deletes specific authorization server instance. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of authorization servers defined within a service instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, authsid, resourceGroupName, serviceName, subscriptionId" /> | Updates the details of the authorization server specified by its identifier. |

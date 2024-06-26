---
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
  - cdn
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
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.routes" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, profileName, resourceGroupName, routeName, subscriptionId" /> | Gets an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint. |
| <CopyableCode code="list_by_endpoint" /> | `SELECT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Lists all of the existing origins within a profile. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="endpointName, profileName, resourceGroupName, routeName, subscriptionId" /> | Creates a new route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointName, profileName, resourceGroupName, routeName, subscriptionId" /> | Deletes an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, routeName, subscriptionId" /> | Updates an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint. |

---
title: access_control_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - access_control_lists
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>access_control_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.access_control_lists" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Access Control List Properties defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessControlListName, resourceGroupName, subscriptionId" /> | Implements Access Control List GET method. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Implements AccessControlLists list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Implements AccessControlLists list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accessControlListName, resourceGroupName, subscriptionId, data__location, data__properties" /> | Implements Access Control List PUT method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accessControlListName, resourceGroupName, subscriptionId" /> | Implements Access Control List DELETE method. |
| <CopyableCode code="resync" /> | `EXEC` | <CopyableCode code="accessControlListName, resourceGroupName, subscriptionId" /> | Implements the operation to the underlying resources. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accessControlListName, resourceGroupName, subscriptionId" /> | API to update certain properties of the Access Control List resource. |
| <CopyableCode code="validate_configuration" /> | `EXEC` | <CopyableCode code="accessControlListName, resourceGroupName, subscriptionId" /> | Implements the operation to the underlying resources. |

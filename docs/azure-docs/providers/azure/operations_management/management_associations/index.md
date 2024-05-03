---
title: management_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - management_associations
  - operations_management
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
<tr><td><b>Name</b></td><td><code>management_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.operations_management.management_associations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | ManagementAssociation properties supported by the OperationsManagement resource provider. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managementAssociationName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId" /> | Retrieves the user ManagementAssociation. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieves the ManagementAssociations list. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managementAssociationName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId" /> | Creates or updates the ManagementAssociation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managementAssociationName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId" /> | Deletes the ManagementAssociation in the subscription. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Retrieves the ManagementAssociations list. |

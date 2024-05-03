---
title: tag
hide_title: false
hide_table_of_contents: false
keywords:
  - tag
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
<tr><td><b>Name</b></td><td><code>tag</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.tag" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, tagId" /> | Gets the details of the tag specified by its identifier. |
| <CopyableCode code="list_by_api" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Lists all Tags associated with the API. |
| <CopyableCode code="list_by_operation" /> | `SELECT` | <CopyableCode code="apiId, operationId, resourceGroupName, serviceName, subscriptionId" /> | Lists all Tags associated with the Operation. |
| <CopyableCode code="list_by_product" /> | `SELECT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId" /> | Lists all Tags associated with the Product. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of tags defined within a service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, tagId" /> | Creates a tag. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, resourceGroupName, serviceName, subscriptionId, tagId" /> | Deletes specific tag of the API Management service instance. |
| <CopyableCode code="_list_by_api" /> | `EXEC` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Lists all Tags associated with the API. |
| <CopyableCode code="_list_by_operation" /> | `EXEC` | <CopyableCode code="apiId, operationId, resourceGroupName, serviceName, subscriptionId" /> | Lists all Tags associated with the Operation. |
| <CopyableCode code="_list_by_product" /> | `EXEC` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId" /> | Lists all Tags associated with the Product. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of tags defined within a service instance. |
| <CopyableCode code="assign_to_api" /> | `EXEC` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Assign tag to the Api. |
| <CopyableCode code="assign_to_operation" /> | `EXEC` | <CopyableCode code="apiId, operationId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Assign tag to the Operation. |
| <CopyableCode code="assign_to_product" /> | `EXEC` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Assign tag to the Product. |
| <CopyableCode code="detach_from_api" /> | `EXEC` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Detach the tag from the Api. |
| <CopyableCode code="detach_from_operation" /> | `EXEC` | <CopyableCode code="apiId, operationId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Detach the tag from the Operation. |
| <CopyableCode code="detach_from_product" /> | `EXEC` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Detach the tag from the Product. |
| <CopyableCode code="get_by_api" /> | `EXEC` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Get tag associated with the API. |
| <CopyableCode code="get_by_operation" /> | `EXEC` | <CopyableCode code="apiId, operationId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Get tag associated with the Operation. |
| <CopyableCode code="get_by_product" /> | `EXEC` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Get tag associated with the Product. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, resourceGroupName, serviceName, subscriptionId, tagId" /> | Updates the details of the tag specified by its identifier. |

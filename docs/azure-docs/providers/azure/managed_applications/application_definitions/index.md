---
title: application_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - application_definitions
  - managed_applications
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
<tr><td><b>Name</b></td><td><code>application_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_applications.application_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="managedBy" /> | `string` | ID of the resource that manages this resource. |
| <CopyableCode code="properties" /> | `object` | The managed application definition properties. |
| <CopyableCode code="sku" /> | `object` | SKU for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationDefinitionName, resourceGroupName, subscriptionId" /> | Gets the managed application definition. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the managed application definitions in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the application definitions within a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationDefinitionName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a managed application definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationDefinitionName, resourceGroupName, subscriptionId" /> | Deletes the managed application definition. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the managed application definitions in a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all the application definitions within a subscription. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="applicationDefinitionName, resourceGroupName, subscriptionId" /> | Updates the managed application definition. |

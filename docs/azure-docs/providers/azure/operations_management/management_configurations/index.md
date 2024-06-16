---
title: management_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - management_configurations
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
<tr><td><b>Name</b></td><td><code>management_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.operations_management.management_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | ManagementConfiguration properties supported by the OperationsManagement resource provider. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managementConfigurationName, resourceGroupName, subscriptionId" /> | Retrieves the user ManagementConfiguration. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieves the ManagementConfigurations list. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managementConfigurationName, resourceGroupName, subscriptionId" /> | Creates or updates the ManagementConfiguration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managementConfigurationName, resourceGroupName, subscriptionId" /> | Deletes the ManagementConfiguration in the subscription. |

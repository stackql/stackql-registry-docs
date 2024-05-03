---
title: data_products
hide_title: false
hide_table_of_contents: false
keywords:
  - data_products
  - network_analytics
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
<tr><td><b>Name</b></td><td><code>data_products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network_analytics.data_products" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The data product properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId" /> | Retrieve data product resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List data products by resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List data products by subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId" /> | Create data product resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId" /> | Delete data product resource. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List data products by resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List data products by subscription. |
| <CopyableCode code="add_user_role" /> | `EXEC` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId, data__dataTypeScope, data__principalId, data__principalType, data__role, data__roleId, data__userName" /> | Assign role to the data product. |
| <CopyableCode code="generate_storage_account_sas_token" /> | `EXEC` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId, data__expiryTimeStamp, data__ipAddress, data__startTimeStamp" /> | Generate sas token for storage account. |
| <CopyableCode code="remove_user_role" /> | `EXEC` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId, data__dataTypeScope, data__principalId, data__principalType, data__role, data__roleAssignmentId, data__roleId, data__userName" /> | Remove role from the data product. |
| <CopyableCode code="rotate_key" /> | `EXEC` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId, data__keyVaultUrl" /> | Initiate key rotation on Data Product. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="dataProductName, resourceGroupName, subscriptionId" /> | Update data product resource. |

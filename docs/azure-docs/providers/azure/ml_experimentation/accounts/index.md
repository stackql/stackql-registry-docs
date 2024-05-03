---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - ml_experimentation
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_experimentation.accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. This cannot be changed after the resource is created. |
| <CopyableCode code="properties" /> | `object` | The properties of a machine learning team account. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified machine learning team account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the available machine learning team accounts under the specified subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the available machine learning team accounts under the specified resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Creates or updates a team account with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Deletes a machine learning team account. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all the available machine learning team accounts under the specified subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the available machine learning team accounts under the specified resource group. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Updates a machine learning team account with the specified parameters. |

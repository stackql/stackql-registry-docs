---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
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
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_experimentation.workspaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. This cannot be changed after the resource is created. |
| <CopyableCode code="properties" /> | `object` | The properties of a machine learning team account workspace. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, workspaceName" /> | Gets the properties of the specified machine learning workspace. |
| <CopyableCode code="list_by_accounts" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists all the available machine learning workspaces under the specified team account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates a machine learning workspace with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a machine learning workspace. |
| <CopyableCode code="_list_by_accounts" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists all the available machine learning workspaces under the specified team account. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, workspaceName" /> | Updates a machine learning workspace with the specified parameters. |

---
title: notebook_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - notebook_workspaces
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>notebook_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.notebook_workspaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `string` | The name of the database account. |
| <CopyableCode code="properties" /> | `object` | Properties of a notebook workspace resource. |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, notebookWorkspaceName, resourceGroupName, subscriptionId" /> | Gets the notebook workspace for a Cosmos DB account. |
| <CopyableCode code="list_by_database_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the notebook workspace resources of an existing Cosmos DB account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, notebookWorkspaceName, resourceGroupName, subscriptionId" /> | Creates the notebook workspace for a Cosmos DB account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, notebookWorkspaceName, resourceGroupName, subscriptionId" /> | Deletes the notebook workspace for a Cosmos DB account. |
| <CopyableCode code="_list_by_database_account" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the notebook workspace resources of an existing Cosmos DB account. |
| <CopyableCode code="regenerate_auth_token" /> | `EXEC` | <CopyableCode code="accountName, notebookWorkspaceName, resourceGroupName, subscriptionId" /> | Regenerates the auth token for the notebook workspace |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="accountName, notebookWorkspaceName, resourceGroupName, subscriptionId" /> | Starts the notebook workspace |

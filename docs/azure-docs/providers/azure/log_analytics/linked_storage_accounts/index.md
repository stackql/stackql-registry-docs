---
title: linked_storage_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - linked_storage_accounts
  - log_analytics
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
<tr><td><b>Name</b></td><td><code>linked_storage_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.linked_storage_accounts" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataSourceType, resourceGroupName, subscriptionId, workspaceName" /> | Gets all linked storage account of a specific data source type associated with the specified workspace. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all linked storage accounts associated with the specified workspace, storage accounts will be sorted by their data source type. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataSourceType, resourceGroupName, subscriptionId, workspaceName, data__properties" /> | Create or Update a link relation between current workspace and a group of storage accounts of a specific data source type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataSourceType, resourceGroupName, subscriptionId, workspaceName" /> | Deletes all linked storage accounts of a specific data source type associated with the specified workspace. |

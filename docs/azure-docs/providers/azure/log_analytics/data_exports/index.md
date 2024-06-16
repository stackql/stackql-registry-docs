---
title: data_exports
hide_title: false
hide_table_of_contents: false
keywords:
  - data_exports
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
<tr><td><b>Name</b></td><td><code>data_exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.data_exports" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataExportName, resourceGroupName, subscriptionId, workspaceName" /> | Gets a data export instance. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists the data export instances within a workspace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataExportName, resourceGroupName, subscriptionId, workspaceName" /> | Create or update a data export. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataExportName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes the specified data export in a given workspace.. |

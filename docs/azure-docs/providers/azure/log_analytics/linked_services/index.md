---
title: linked_services
hide_title: false
hide_table_of_contents: false
keywords:
  - linked_services
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
<tr><td><b>Name</b></td><td><code>linked_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.linked_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Linked service properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="linkedServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Gets a linked service instance. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets the linked services instances in a workspace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="linkedServiceName, resourceGroupName, subscriptionId, workspaceName, data__properties" /> | Create or update a linked service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="linkedServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a linked service instance. |

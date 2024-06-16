---
title: partner_namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_namespaces
  - event_grid
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
<tr><td><b>Name</b></td><td><code>partner_namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.partner_namespaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the partner namespace. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Tags of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="partnerNamespaceName, resourceGroupName, subscriptionId" /> | Get properties of a partner namespace. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the partner namespaces under a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the partner namespaces under an Azure subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="partnerNamespaceName, resourceGroupName, subscriptionId" /> | Asynchronously creates a new partner namespace with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="partnerNamespaceName, resourceGroupName, subscriptionId" /> | Delete existing partner namespace. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="partnerNamespaceName, resourceGroupName, subscriptionId, data__keyName" /> | Regenerate a shared access key for a partner namespace. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="partnerNamespaceName, resourceGroupName, subscriptionId" /> | Asynchronously updates a partner namespace with the specified parameters. |

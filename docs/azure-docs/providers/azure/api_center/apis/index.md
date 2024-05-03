---
title: apis
hide_title: false
hide_table_of_contents: false
keywords:
  - apis
  - api_center
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
<tr><td><b>Name</b></td><td><code>apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_center.apis" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | API properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Returns details of the API. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Returns a collection of APIs. |
| <CopyableCode code="create_or_update" /> | `INSERT` |  | Creates new or updates existing API. |
| <CopyableCode code="delete" /> | `DELETE` |  | Deletes specified API. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceName" /> | Returns a collection of APIs. |
| <CopyableCode code="head" /> | `EXEC` |  | Checks if specified API exists. |

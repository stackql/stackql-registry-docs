---
title: api_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - api_definitions
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
<tr><td><b>Name</b></td><td><code>api_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_center.api_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | API definition properties entity. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Returns details of the API definition. |
| <CopyableCode code="list" /> | `SELECT` |  | Returns a collection of API definitions. |
| <CopyableCode code="create_or_update" /> | `INSERT` |  | Creates new or updates existing API definition. |
| <CopyableCode code="delete" /> | `DELETE` |  | Deletes specified API definition. |
| <CopyableCode code="_list" /> | `EXEC` |  | Returns a collection of API definitions. |
| <CopyableCode code="export_specification" /> | `EXEC` |  | Exports the API specification. |
| <CopyableCode code="head" /> | `EXEC` |  | Checks if specified API definition exists. |
| <CopyableCode code="import_specification" /> | `EXEC` |  | Imports the API specification. |

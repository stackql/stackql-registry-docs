---
title: integration_account_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_maps
  - logic_apps
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
<tr><td><b>Name</b></td><td><code>integration_account_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_account_maps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The integration account map. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, integrationAccountName, mapName, resourceGroupName, subscriptionId" /> | Gets an integration account map. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, integrationAccountName, resourceGroupName, subscriptionId" /> | Gets a list of integration account maps. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, integrationAccountName, mapName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an integration account map. If the map is larger than 4 MB, you need to store the map in an Azure blob and use the blob's Shared Access Signature (SAS) URL as the 'contentLink' property value. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, integrationAccountName, mapName, resourceGroupName, subscriptionId" /> | Deletes an integration account map. |

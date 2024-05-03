---
title: configuration_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_stores
  - app_configuration
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
<tr><td><b>Name</b></td><td><code>configuration_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration.configuration_stores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | An identity that can be associated with a resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a configuration store. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified configuration store. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the configuration stores for a given subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the configuration stores for a given resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId, data__location, data__sku" /> | Creates a configuration store with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId" /> | Deletes a configuration store. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists the configuration stores for a given subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the configuration stores for a given resource group. |
| <CopyableCode code="purge_deleted" /> | `EXEC` | <CopyableCode code="configStoreName, location, subscriptionId" /> | Permanently deletes the specified configuration store. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId" /> | Regenerates an access key for the specified configuration store. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId" /> | Updates a configuration store with the specified parameters. |

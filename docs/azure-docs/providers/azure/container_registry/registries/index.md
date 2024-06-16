---
title: registries
hide_title: false
hide_table_of_contents: false
keywords:
  - registries
  - container_registry
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
<tr><td><b>Name</b></td><td><code>registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.registries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="identity" /> | `object` | Managed identity for the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. This cannot be changed after the resource is created. |
| <CopyableCode code="properties" /> | `object` | The properties of a container registry. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified container registry. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the container registries under the specified subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the container registries under the specified resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, data__sku" /> | Creates a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Deletes a container registry. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Checks whether the container registry name is available for use. The name must contain only alphanumeric characters, be globally unique, and between 5 and 50 characters in length. |
| <CopyableCode code="generate_credentials" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Generate keys for a token of a specified container registry. |
| <CopyableCode code="import_image" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, data__source" /> | Copies an image to this container registry from the specified container registry. |
| <CopyableCode code="regenerate_credential" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, data__name" /> | Regenerates one of the login credentials for the specified container registry. |
| <CopyableCode code="schedule_run" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId, data__type" /> | Schedules a new run based on the request parameters and add it to the run queue. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Updates a container registry with the specified parameters. |

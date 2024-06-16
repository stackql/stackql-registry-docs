---
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
  - api_management
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
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.service" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | ETag of the resource. |
| <CopyableCode code="identity" /> | `object` | Identity properties of the Api Management service resource. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of an API Management service resource description. |
| <CopyableCode code="sku" /> | `object` | API Management service resource SKU properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type for API Management resource is set to Microsoft.ApiManagement. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting where the resource needs to come from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Gets an API Management service resource description. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all API Management services within an Azure subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all API Management services within a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, data__location, data__properties, data__sku" /> | Creates or updates an API Management service. This is long running operation and could take several minutes to complete. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Deletes an existing API Management service. |
| <CopyableCode code="apply_network_configuration_updates" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Updates the Microsoft.ApiManagement resource running in the Virtual network to pick the updated DNS changes. |
| <CopyableCode code="backup" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, data__backupName, data__containerName, data__storageAccount" /> | Creates a backup of the API Management service to the given Azure Storage Account. This is long running operation and could take several minutes to complete. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name" /> | Checks availability and correctness of a name for an API Management service. |
| <CopyableCode code="migrate_to_stv2" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Upgrades an API Management service to the Stv2 platform. For details refer to https://aka.ms/apim-migrate-stv2. This change is not reversible. This is long running operation and could take several minutes to complete. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, data__backupName, data__containerName, data__storageAccount" /> | Restores a backup of an API Management service created using the ApiManagementService_Backup operation on the current service. This is a long running operation and could take several minutes to complete. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Updates an existing API Management service. |

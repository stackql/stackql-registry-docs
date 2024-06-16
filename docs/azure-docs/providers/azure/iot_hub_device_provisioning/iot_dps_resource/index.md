---
title: iot_dps_resource
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_dps_resource
  - iot_hub_device_provisioning
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
<tr><td><b>Name</b></td><td><code>iot_dps_resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub_device_provisioning.iot_dps_resource" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | the service specific properties of a provisioning service, including keys, linked iot hubs, current state, and system generated properties such as hostname and idScope |
| <CopyableCode code="resourcegroup" /> | `string` | The resource group of the resource. |
| <CopyableCode code="sku" /> | `object` | List of possible provisioning service SKUs. |
| <CopyableCode code="subscriptionid" /> | `string` | The subscription id of the resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, provisioningServiceName, resourceGroupName, subscriptionId" /> | Get the metadata of the provisioning service without SAS keys. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Get a list of all provisioning services in the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | List all the provisioning services for a given subscription id. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, provisioningServiceName, resourceGroupName, subscriptionId, data__properties, data__sku" /> | Create or update the metadata of the provisioning service. The usual pattern to modify a property is to retrieve the provisioning service metadata and security metadata, and then combine them with the modified values in a new body to update the provisioning service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, provisioningServiceName, resourceGroupName, subscriptionId" /> | Deletes the Provisioning Service. |
| <CopyableCode code="check_provisioning_service_name_availability" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId, data__name" /> | Check if a provisioning service name is available. This will validate if the name is syntactically valid and if the name is usable |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, provisioningServiceName, resourceGroupName, subscriptionId" /> | Update an existing provisioning service's tags. to update other fields use the CreateOrUpdate method |

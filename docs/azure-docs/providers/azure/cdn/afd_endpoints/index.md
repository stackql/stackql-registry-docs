---
title: afd_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_endpoints
  - cdn
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
<tr><td><b>Name</b></td><td><code>afd_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.afd_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties required to create an endpoint. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Gets an existing AzureFrontDoor endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| <CopyableCode code="list_by_profile" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Lists existing AzureFrontDoor endpoints. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Creates a new AzureFrontDoor endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Deletes an existing AzureFrontDoor endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| <CopyableCode code="purge_content" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId, data__contentPaths" /> | Removes a content from AzureFrontDoor. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Updates an existing AzureFrontDoor endpoint with the specified endpoint name under the specified subscription, resource group and profile. Only tags can be updated after creating an endpoint. To update origins, use the Update Origin operation. To update origin groups, use the Update Origin group operation. To update domains, use the Update Custom Domain operation. |
| <CopyableCode code="validate_custom_domain" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId, data__hostName" /> | Validates the custom domain mapping to ensure it maps to the correct Azure Front Door endpoint in DNS. |

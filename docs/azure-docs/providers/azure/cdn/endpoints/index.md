---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
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
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.endpoints" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Gets an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| <CopyableCode code="list_by_profile" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Lists existing CDN endpoints. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Creates a new CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Deletes an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| <CopyableCode code="load_content" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId, data__contentPaths" /> | Pre-loads a content to CDN. Available for Verizon Profiles. |
| <CopyableCode code="purge_content" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId, data__contentPaths" /> | Removes a content from CDN. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Starts an existing CDN endpoint that is on a stopped state. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Stops an existing running CDN endpoint. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Updates an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. Only tags can be updated after creating an endpoint. To update origins, use the Update Origin operation. To update origin groups, use the Update Origin group operation. To update custom domains, use the Update Custom Domain operation. |
| <CopyableCode code="validate_custom_domain" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId, data__hostName" /> | Validates the custom domain mapping to ensure it maps to the correct CDN endpoint in DNS. |

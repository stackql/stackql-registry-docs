---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - search
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the search service. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, searchServiceName, subscriptionId" /> | Gets the search service with the given name in the given resource group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of all Search services in the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of all Search services in the given subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, searchServiceName, subscriptionId" /> | Creates or updates a search service in the given resource group. If the search service already exists, all properties will be updated with the given values. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, searchServiceName, subscriptionId" /> | Deletes a search service in the given resource group, along with its associated resources. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of all Search services in the given resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets a list of all Search services in the given subscription. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Checks whether or not the given search service name is available for use. Search service names must be globally unique since they are part of the service URI (https://&lt;name&gt;.search.windows.net). |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, searchServiceName, subscriptionId" /> | Updates an existing search service in the given resource group. |

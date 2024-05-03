---
title: integration_service_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_service_environments
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
<tr><td><b>Name</b></td><td><code>integration_service_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_service_environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="identity" /> | `object` | Managed service identity properties. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The integration service environment properties. |
| <CopyableCode code="sku" /> | `object` | The integration service environment sku. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Gets an integration service environment. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroup, subscriptionId" /> | Gets a list of integration service environments by resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Gets a list of integration service environments by subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Creates or updates an integration service environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Deletes an integration service environment. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroup, subscriptionId" /> | Gets a list of integration service environments by resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> | Gets a list of integration service environments by subscription. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Restarts an integration service environment. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Updates an integration service environment. |

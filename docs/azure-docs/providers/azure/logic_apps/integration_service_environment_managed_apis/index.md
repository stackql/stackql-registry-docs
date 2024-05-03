---
title: integration_service_environment_managed_apis
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_service_environment_managed_apis
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
<tr><td><b>Name</b></td><td><code>integration_service_environment_managed_apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_service_environment_managed_apis" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The integration service environment managed api properties. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, apiName, integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Gets the integration service environment managed Api. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Gets the integration service environment managed Apis. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, apiName, integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Deletes the integration service environment managed Api. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Gets the integration service environment managed Apis. |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="api-version, apiName, integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Puts the integration service environment managed Api. |

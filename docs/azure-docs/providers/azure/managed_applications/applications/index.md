---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - managed_applications
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_applications.applications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `string` | The kind of the managed application. Allowed values are MarketPlace and ServiceCatalog. |
| <CopyableCode code="managedBy" /> | `string` | ID of the resource that manages this resource. |
| <CopyableCode code="plan" /> | `object` | Plan for the managed application. |
| <CopyableCode code="properties" /> | `object` | The managed application properties. |
| <CopyableCode code="sku" /> | `object` | SKU for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationName, resourceGroupName, subscriptionId" /> | Gets the managed application. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the applications within a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the applications within a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationName, resourceGroupName, subscriptionId, data__kind, data__properties" /> | Creates or updates a managed application. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationName, resourceGroupName, subscriptionId" /> | Deletes the managed application. |
| <CopyableCode code="delete_by_id" /> | `DELETE` | <CopyableCode code="applicationId" /> | Deletes the managed application. |
| <CopyableCode code="create_or_update_by_id" /> | `EXEC` | <CopyableCode code="applicationId, data__kind, data__properties" /> | Creates or updates a managed application. |
| <CopyableCode code="get_by_id" /> | `EXEC` | <CopyableCode code="applicationId" /> | Gets the managed application. |
| <CopyableCode code="refresh_permissions" /> | `EXEC` | <CopyableCode code="applicationName, resourceGroupName, subscriptionId" /> | Refresh Permissions for application. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="applicationName, resourceGroupName, subscriptionId" /> | Updates an existing managed application. |
| <CopyableCode code="update_by_id" /> | `EXEC` | <CopyableCode code="applicationId" /> | Updates an existing managed application. |

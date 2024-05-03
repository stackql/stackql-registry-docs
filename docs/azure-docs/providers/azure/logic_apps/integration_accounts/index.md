---
title: integration_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_accounts
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
<tr><td><b>Name</b></td><td><code>integration_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The integration account properties. |
| <CopyableCode code="sku" /> | `object` | The integration account sku. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, integrationAccountName, resourceGroupName, subscriptionId" /> | Gets an integration account. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Gets a list of integration accounts by resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Gets a list of integration accounts by subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, integrationAccountName, resourceGroupName, subscriptionId" /> | Creates or updates an integration account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, integrationAccountName, resourceGroupName, subscriptionId" /> | Deletes an integration account. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Gets a list of integration accounts by resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> | Gets a list of integration accounts by subscription. |
| <CopyableCode code="log_tracking_events" /> | `EXEC` | <CopyableCode code="api-version, integrationAccountName, resourceGroupName, subscriptionId, data__events, data__sourceType" /> | Logs the integration account's tracking events. |
| <CopyableCode code="regenerate_access_key" /> | `EXEC` | <CopyableCode code="api-version, integrationAccountName, resourceGroupName, subscriptionId" /> | Regenerates the integration account access key. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, integrationAccountName, resourceGroupName, subscriptionId" /> | Updates an integration account. |

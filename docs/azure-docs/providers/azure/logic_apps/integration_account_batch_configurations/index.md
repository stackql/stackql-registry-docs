---
title: integration_account_batch_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_batch_configurations
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
<tr><td><b>Name</b></td><td><code>integration_account_batch_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_account_batch_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The batch configuration properties definition. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, batchConfigurationName, integrationAccountName, resourceGroupName, subscriptionId" /> | Get a batch configuration for an integration account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, integrationAccountName, resourceGroupName, subscriptionId" /> | List the batch configurations for an integration account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, batchConfigurationName, integrationAccountName, resourceGroupName, subscriptionId, data__properties" /> | Create or update a batch configuration for an integration account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, batchConfigurationName, integrationAccountName, resourceGroupName, subscriptionId" /> | Delete a batch configuration for an integration account. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, integrationAccountName, resourceGroupName, subscriptionId" /> | List the batch configurations for an integration account. |

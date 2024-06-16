---
title: kusto_pool_attached_database_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pool_attached_database_configurations
  - synapse
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
<tr><td><b>Name</b></td><td><code>kusto_pool_attached_database_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.kusto_pool_attached_database_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Class representing the an attached database configuration properties of kind specific. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="attachedDatabaseConfigurationName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Returns an attached database configuration. |
| <CopyableCode code="list_by_kusto_pool" /> | `SELECT` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Returns the list of attached database configurations of the given Kusto Pool. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="attachedDatabaseConfigurationName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates an attached database configuration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="attachedDatabaseConfigurationName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes the attached database configuration with the given name. |

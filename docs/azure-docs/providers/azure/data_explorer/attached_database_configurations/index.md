---
title: attached_database_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - attached_database_configurations
  - data_explorer
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
<tr><td><b>Name</b></td><td><code>attached_database_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.attached_database_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Class representing the an attached database configuration properties of kind specific. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="attachedDatabaseConfigurationName, clusterName, resourceGroupName, subscriptionId" /> | Returns an attached database configuration. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Returns the list of attached database configurations of the given Kusto cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="attachedDatabaseConfigurationName, clusterName, resourceGroupName, subscriptionId" /> | Creates or updates an attached database configuration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="attachedDatabaseConfigurationName, clusterName, resourceGroupName, subscriptionId" /> | Deletes the attached database configuration with the given name. |
| <CopyableCode code="_list_by_cluster" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Returns the list of attached database configurations of the given Kusto cluster. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__name, data__type" /> | Checks that the attached database configuration resource name is valid and is not already in use. |

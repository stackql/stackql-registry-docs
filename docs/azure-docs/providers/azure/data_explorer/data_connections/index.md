---
title: data_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - data_connections
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
<tr><td><b>Name</b></td><td><code>data_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.data_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of the endpoint for the data connection |
| <CopyableCode code="location" /> | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, dataConnectionName, databaseName, resourceGroupName, subscriptionId" /> | Returns a data connection. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Returns the list of data connections of the given Kusto database. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, dataConnectionName, databaseName, resourceGroupName, subscriptionId, data__kind" /> | Creates or updates a data connection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, dataConnectionName, databaseName, resourceGroupName, subscriptionId" /> | Deletes the data connection with the given name. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__name, data__type" /> | Checks that the data connection name is valid and is not already in use. |
| <CopyableCode code="data_connection_validation" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Checks that the data connection parameters are valid. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterName, dataConnectionName, databaseName, resourceGroupName, subscriptionId, data__kind" /> | Updates a data connection. |

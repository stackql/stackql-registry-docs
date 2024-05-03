---
title: scripts
hide_title: false
hide_table_of_contents: false
keywords:
  - scripts
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
<tr><td><b>Name</b></td><td><code>scripts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.scripts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A class representing database script property. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, scriptName, subscriptionId" /> | Gets a Kusto cluster database script. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Returns the list of database scripts for given database. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, scriptName, subscriptionId" /> | Creates a Kusto database script. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, databaseName, resourceGroupName, scriptName, subscriptionId" /> | Deletes a Kusto database script. |
| <CopyableCode code="_list_by_database" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Returns the list of database scripts for given database. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__name, data__type" /> | Checks that the script name is valid and is not already in use. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, scriptName, subscriptionId" /> | Updates a database script. |

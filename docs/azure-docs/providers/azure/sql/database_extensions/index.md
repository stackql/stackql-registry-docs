---
title: database_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - database_extensions
  - sql
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
<tr><td><b>Name</b></td><td><code>database_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.database_extensions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | List database extension. This will return an empty list as it is not supported. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, extensionName, resourceGroupName, serverName, subscriptionId" /> | Perform a database extension operation, like polybase import |
| <CopyableCode code="_list_by_database" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | List database extension. This will return an empty list as it is not supported. |
| <CopyableCode code="exec_get" /> | `EXEC` | <CopyableCode code="databaseName, extensionName, resourceGroupName, serverName, subscriptionId" /> | Gets a database extension. This will return resource not found as it is not supported. |

---
title: database_recommended_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - database_recommended_actions
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
<tr><td><b>Name</b></td><td><code>database_recommended_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.database_recommended_actions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Resource kind. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties for a Database, Server or Elastic Pool Recommended Action. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="advisorName, databaseName, recommendedActionName, resourceGroupName, serverName, subscriptionId" /> | Gets a database recommended action. |
| <CopyableCode code="list_by_database_advisor" /> | `SELECT` | <CopyableCode code="advisorName, databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets list of Database Recommended Actions. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="advisorName, databaseName, recommendedActionName, resourceGroupName, serverName, subscriptionId" /> | Updates a database recommended action. |

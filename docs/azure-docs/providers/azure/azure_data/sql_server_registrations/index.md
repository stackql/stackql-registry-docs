---
title: sql_server_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_server_registrations
  - azure_data
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
<tr><td><b>Name</b></td><td><code>sql_server_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_data.sql_server_registrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The SQL server Registration properties. |
| <CopyableCode code="systemData" /> | `object` | Read only system data |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlServerRegistrationName, subscriptionId" /> | Gets a SQL Server registration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all SQL Server registrations in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all SQL Server registrations in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlServerRegistrationName, subscriptionId, data__location" /> | Creates or updates a SQL Server registration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sqlServerRegistrationName, subscriptionId" /> | Deletes a SQL Server registration. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlServerRegistrationName, subscriptionId" /> | Updates SQL Server Registration tags. |

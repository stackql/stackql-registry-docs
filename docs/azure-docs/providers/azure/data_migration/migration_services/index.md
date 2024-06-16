---
title: migration_services
hide_title: false
hide_table_of_contents: false
keywords:
  - migration_services
  - data_migration
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
<tr><td><b>Name</b></td><td><code>migration_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.migration_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The Migration Service properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="migrationServiceName, resourceGroupName, subscriptionId" /> | Retrieve the Database Migration Service |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieve all migration services in the resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieve all migration services in the subscriptions. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="migrationServiceName, resourceGroupName, subscriptionId" /> | Create or Update Database Migration Service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="migrationServiceName, resourceGroupName, subscriptionId" /> | Delete Database Migration Service. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="migrationServiceName, resourceGroupName, subscriptionId" /> | Update Database Migration Service. |

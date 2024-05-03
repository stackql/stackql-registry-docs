---
title: postgres_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_instances
  - azure_arc_data
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
<tr><td><b>Name</b></td><td><code>postgres_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.postgres_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Postgres Instance properties. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU for Azure Database for PostgresSQL - Azure Arc |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, postgresInstanceName, resourceGroupName, subscriptionId" /> | Retrieves a postgres Instance resource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Get a postgres Instances list by Resource group name. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, postgresInstanceName, resourceGroupName, subscriptionId, data__properties" /> | Creates or replaces a postgres Instance resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, postgresInstanceName, resourceGroupName, subscriptionId" /> | Deletes a postgres Instance resource |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> |  |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Get a postgres Instances list by Resource group name. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, postgresInstanceName, resourceGroupName, subscriptionId" /> | Updates a postgres Instance resource |

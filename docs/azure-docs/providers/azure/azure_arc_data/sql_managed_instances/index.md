---
title: sql_managed_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_managed_instances
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
<tr><td><b>Name</b></td><td><code>sql_managed_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.sql_managed_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of sqlManagedInstance. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU for Azure Managed Instance - Azure Arc |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, sqlManagedInstanceName, subscriptionId" /> | Retrieves a SQL Managed Instance resource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Gets all sqlManagedInstances in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, resourceGroupName, sqlManagedInstanceName, subscriptionId, data__properties" /> | Creates or replaces a SQL Managed Instance resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, resourceGroupName, sqlManagedInstanceName, subscriptionId" /> | Deletes a SQL Managed Instance resource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, sqlManagedInstanceName, subscriptionId" /> | Updates a SQL Managed Instance resource |

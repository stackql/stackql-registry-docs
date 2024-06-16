---
title: sql_server_availability_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_server_availability_groups
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
<tr><td><b>Name</b></td><td><code>sql_server_availability_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.sql_server_availability_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of Arc Sql Server availability group resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="availabilityGroupName, resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Retrieves an Arc Sql Server availability group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlServerInstanceName, subscriptionId" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="availabilityGroupName, resourceGroupName, sqlServerInstanceName, subscriptionId, data__properties" /> | Creates or replaces an Arc Sql Server Availability Group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="availabilityGroupName, resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Deletes an Arc Sql Server availability group resource. |
| <CopyableCode code="detail_view" /> | `EXEC` | <CopyableCode code="availabilityGroupName, resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Retrieves detailed properties of the Availability Group. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="availabilityGroupName, resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Request manual failover of the availability group to this server. |
| <CopyableCode code="force_failover_allow_data_loss" /> | `EXEC` | <CopyableCode code="availabilityGroupName, resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Request forced failover of the availability group to this server. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="availabilityGroupName, resourceGroupName, sqlServerInstanceName, subscriptionId" /> | Updates an existing Availability Group. |

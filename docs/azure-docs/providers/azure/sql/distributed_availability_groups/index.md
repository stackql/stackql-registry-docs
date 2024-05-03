---
title: distributed_availability_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - distributed_availability_groups
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
<tr><td><b>Name</b></td><td><code>distributed_availability_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.distributed_availability_groups" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="distributedAvailabilityGroupName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a distributed availability group info. |
| <CopyableCode code="list_by_instance" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a list of a distributed availability groups in instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="distributedAvailabilityGroupName, managedInstanceName, resourceGroupName, subscriptionId" /> | Creates a distributed availability group between Sql On-Prem and Sql Managed Instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="distributedAvailabilityGroupName, managedInstanceName, resourceGroupName, subscriptionId" /> | Drops a distributed availability group between Sql On-Prem and Sql Managed Instance. |
| <CopyableCode code="_list_by_instance" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a list of a distributed availability groups in instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="distributedAvailabilityGroupName, managedInstanceName, resourceGroupName, subscriptionId" /> | Updates a distributed availability group replication mode. |

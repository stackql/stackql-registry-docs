---
title: instance_failover_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_failover_groups
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
<tr><td><b>Name</b></td><td><code>instance_failover_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.instance_failover_groups" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="failoverGroupName, locationName, resourceGroupName, subscriptionId" /> | Gets a failover group. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="locationName, resourceGroupName, subscriptionId" /> | Lists the failover groups in a location. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="failoverGroupName, locationName, resourceGroupName, subscriptionId" /> | Creates or updates a failover group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="failoverGroupName, locationName, resourceGroupName, subscriptionId" /> | Deletes a failover group. |
| <CopyableCode code="_list_by_location" /> | `EXEC` | <CopyableCode code="locationName, resourceGroupName, subscriptionId" /> | Lists the failover groups in a location. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="failoverGroupName, locationName, resourceGroupName, subscriptionId" /> | Fails over from the current primary managed instance to this managed instance. |
| <CopyableCode code="force_failover_allow_data_loss" /> | `EXEC` | <CopyableCode code="failoverGroupName, locationName, resourceGroupName, subscriptionId" /> | Fails over from the current primary managed instance to this managed instance. This operation might result in data loss. |

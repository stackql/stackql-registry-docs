---
title: failover_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - failover_groups
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
<tr><td><b>Name</b></td><td><code>failover_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.failover_groups" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, failoverGroupName, resourceGroupName, sqlManagedInstanceName, subscriptionId" /> | Retrieves a failover group resource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, sqlManagedInstanceName, subscriptionId" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, failoverGroupName, resourceGroupName, sqlManagedInstanceName, subscriptionId, data__properties" /> | Creates or replaces a failover group resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, failoverGroupName, resourceGroupName, sqlManagedInstanceName, subscriptionId" /> | Deletes a failover group resource |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, sqlManagedInstanceName, subscriptionId" /> |  |

---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
  - container_storage
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
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_storage.volumes" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="poolName, resourceGroupName, subscriptionId, volumeName" /> | Get a Volume |
| <CopyableCode code="list_by_pool" /> | `SELECT` | <CopyableCode code="poolName, resourceGroupName, subscriptionId" /> | List Volume resources by Pool |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="poolName, resourceGroupName, subscriptionId, volumeName" /> | Create a Volume |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="poolName, resourceGroupName, subscriptionId, volumeName" /> | Compliant create or update template/** |
| <CopyableCode code="_list_by_pool" /> | `EXEC` | <CopyableCode code="poolName, resourceGroupName, subscriptionId" /> | List Volume resources by Pool |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="poolName, resourceGroupName, subscriptionId, volumeName" /> | Update a Volume |

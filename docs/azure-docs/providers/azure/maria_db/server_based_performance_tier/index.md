---
title: server_based_performance_tier
hide_title: false
hide_table_of_contents: false
keywords:
  - server_based_performance_tier
  - maria_db
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
<tr><td><b>Name</b></td><td><code>server_based_performance_tier</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maria_db.server_based_performance_tier" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the performance tier. |
| <CopyableCode code="maxBackupRetentionDays" /> | `integer` | Maximum Backup retention in days for the performance tier edition |
| <CopyableCode code="maxLargeStorageMB" /> | `integer` | Max storage allowed for a server. |
| <CopyableCode code="maxStorageMB" /> | `integer` | Max storage allowed for a server. |
| <CopyableCode code="minBackupRetentionDays" /> | `integer` | Minimum Backup retention in days for the performance tier edition |
| <CopyableCode code="minLargeStorageMB" /> | `integer` | Max storage allowed for a server. |
| <CopyableCode code="minStorageMB" /> | `integer` | Max storage allowed for a server. |
| <CopyableCode code="serviceLevelObjectives" /> | `array` | Service level objectives associated with the performance tier |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> |

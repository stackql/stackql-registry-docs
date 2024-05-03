---
title: flexible_server_ltr_backup
hide_title: false
hide_table_of_contents: false
keywords:
  - flexible_server_ltr_backup
  - postgresql
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
<tr><td><b>Name</b></td><td><code>flexible_server_ltr_backup</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql.flexible_server_ltr_backup" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="start_ltr_backup" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, data__targetDetails" /> | Start the Long Term Retention Backup operation |
| <CopyableCode code="trigger_ltr_pre_backup" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | PreBackup operation performs all the checks that are needed for the subsequent long term retention backup operation to succeed. |

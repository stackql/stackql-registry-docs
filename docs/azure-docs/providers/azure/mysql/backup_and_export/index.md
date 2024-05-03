---
title: backup_and_export
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_and_export
  - mysql
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
<tr><td><b>Name</b></td><td><code>backup_and_export</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.backup_and_export" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, data__backupSettings, data__targetDetails" /> | Exports the backup of the given server by creating a backup if not existing. |
| <CopyableCode code="validate_backup" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Validates if backup can be performed for given server. |

---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.backups" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupName, resourceGroupName, serverName, subscriptionId" /> | List all the backups for a given server. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | List all the backups for a given server. |
| <CopyableCode code="_list_by_server" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | List all the backups for a given server. |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="backupName, resourceGroupName, serverName, subscriptionId" /> | Create backup for a given server with specified backup name. |

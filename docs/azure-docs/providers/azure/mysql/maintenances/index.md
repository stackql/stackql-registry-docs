---
title: maintenances
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenances
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
<tr><td><b>Name</b></td><td><code>maintenances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.maintenances" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | List maintenances. |
| <CopyableCode code="read" /> | `EXEC` | <CopyableCode code="maintenanceName, resourceGroupName, serverName, subscriptionId" /> | Read maintenance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="maintenanceName, resourceGroupName, serverName, subscriptionId" /> | Update maintenances. |

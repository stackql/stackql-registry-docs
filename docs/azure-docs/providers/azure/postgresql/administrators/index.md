---
title: administrators
hide_title: false
hide_table_of_contents: false
keywords:
  - administrators
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
<tr><td><b>Name</b></td><td><code>administrators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql.administrators" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="objectId, resourceGroupName, serverName, subscriptionId" /> | Gets information about a server. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | List all the AAD administrators for a given server. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="objectId, resourceGroupName, serverName, subscriptionId" /> | Creates a new server. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="objectId, resourceGroupName, serverName, subscriptionId" /> | Deletes an Active Directory Administrator associated with the server. |

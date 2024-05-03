---
title: server_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - server_keys
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
<tr><td><b>Name</b></td><td><code>server_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties for a server key execution. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keyName, resourceGroupName, serverName, subscriptionId" /> | Gets a server key. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of server keys. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="keyName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates a server key. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="keyName, resourceGroupName, serverName, subscriptionId" /> | Deletes the server key with the given name. |
| <CopyableCode code="_list_by_server" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of server keys. |

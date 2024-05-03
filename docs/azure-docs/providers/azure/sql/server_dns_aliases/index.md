---
title: server_dns_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - server_dns_aliases
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
<tr><td><b>Name</b></td><td><code>server_dns_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_dns_aliases" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsAliasName, resourceGroupName, serverName, subscriptionId" /> | Gets a server DNS alias. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of server DNS aliases for a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dnsAliasName, resourceGroupName, serverName, subscriptionId" /> | Creates a server DNS alias. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dnsAliasName, resourceGroupName, serverName, subscriptionId" /> | Deletes the server DNS alias with the given name. |
| <CopyableCode code="_list_by_server" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of server DNS aliases for a server. |
| <CopyableCode code="acquire" /> | `EXEC` | <CopyableCode code="dnsAliasName, resourceGroupName, serverName, subscriptionId, data__oldServerDnsAliasId" /> | Acquires server DNS alias from another server. |

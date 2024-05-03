---
title: managed_server_dns_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_server_dns_aliases
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
<tr><td><b>Name</b></td><td><code>managed_server_dns_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_server_dns_aliases" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsAliasName, managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a server DNS alias. |
| <CopyableCode code="list_by_managed_instance" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a list of managed server DNS aliases for a managed server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dnsAliasName, managedInstanceName, resourceGroupName, subscriptionId" /> | Creates a managed server DNS alias. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dnsAliasName, managedInstanceName, resourceGroupName, subscriptionId" /> | Deletes the managed server DNS alias with the given name. |
| <CopyableCode code="_list_by_managed_instance" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a list of managed server DNS aliases for a managed server. |
| <CopyableCode code="acquire" /> | `EXEC` | <CopyableCode code="dnsAliasName, managedInstanceName, resourceGroupName, subscriptionId, data__oldManagedServerDnsAliasResourceId" /> | Acquires managed server DNS alias from another managed server. |

---
title: server_azure_ad_only_authentications
hide_title: false
hide_table_of_contents: false
keywords:
  - server_azure_ad_only_authentications
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
<tr><td><b>Name</b></td><td><code>server_azure_ad_only_authentications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_azure_ad_only_authentications" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authenticationName, resourceGroupName, serverName, subscriptionId" /> | Gets a specific Azure Active Directory only authentication property. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of server Azure Active Directory only authentications. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authenticationName, resourceGroupName, serverName, subscriptionId" /> | Sets Server Active Directory only authentication property or updates an existing server Active Directory only authentication property. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authenticationName, resourceGroupName, serverName, subscriptionId" /> | Deletes an existing server Active Directory only authentication property. |
| <CopyableCode code="_list_by_server" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of server Azure Active Directory only authentications. |

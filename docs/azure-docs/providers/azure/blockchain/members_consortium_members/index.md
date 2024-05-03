---
title: members_consortium_members
hide_title: false
hide_table_of_contents: false
keywords:
  - members_consortium_members
  - blockchain
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
<tr><td><b>Name</b></td><td><code>members_consortium_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.blockchain.members_consortium_members" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Gets the consortium member name. |
| <CopyableCode code="dateModified" /> | `string` | Gets the consortium member modified date. |
| <CopyableCode code="displayName" /> | `string` | Gets the consortium member display name. |
| <CopyableCode code="joinDate" /> | `string` | Gets the consortium member join date. |
| <CopyableCode code="role" /> | `string` | Gets the consortium member role. |
| <CopyableCode code="status" /> | `string` | Gets the consortium member status. |
| <CopyableCode code="subscriptionId" /> | `string` | Gets the consortium member subscription id. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="blockchainMemberName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="blockchainMemberName, resourceGroupName, subscriptionId" /> |

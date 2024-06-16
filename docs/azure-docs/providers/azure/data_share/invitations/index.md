---
title: invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - invitations
  - data_share
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
<tr><td><b>Name</b></td><td><code>invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.invitations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `string` | Name of the azure resource |
| <CopyableCode code="properties" /> | `object` | Invitation property bag. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the azure resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, invitationName, resourceGroupName, shareName, subscriptionId" /> | Get an invitation in a share |
| <CopyableCode code="list_by_share" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, shareName, subscriptionId" /> | List invitations in a share |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, api-version, invitationName, resourceGroupName, shareName, subscriptionId" /> | Create an invitation  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, invitationName, resourceGroupName, shareName, subscriptionId" /> | Delete an invitation in a share |

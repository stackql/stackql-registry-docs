---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
  - event_grid
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
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.channels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the Channel. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="channelName, partnerNamespaceName, resourceGroupName, subscriptionId" /> | Get properties of a channel. |
| <CopyableCode code="list_by_partner_namespace" /> | `SELECT` | <CopyableCode code="partnerNamespaceName, resourceGroupName, subscriptionId" /> | List all the channels in a partner namespace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="channelName, partnerNamespaceName, resourceGroupName, subscriptionId" /> | Synchronously creates or updates a new channel with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="channelName, partnerNamespaceName, resourceGroupName, subscriptionId" /> | Delete an existing channel. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="channelName, partnerNamespaceName, resourceGroupName, subscriptionId" /> | Synchronously updates a channel with the specified parameters. |

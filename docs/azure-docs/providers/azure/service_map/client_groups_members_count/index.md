---
title: client_groups_members_count
hide_title: false
hide_table_of_contents: false
keywords:
  - client_groups_members_count
  - service_map
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
<tr><td><b>Name</b></td><td><code>client_groups_members_count</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_map.client_groups_members_count" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accuracy" /> | `string` | Specifies the accuracy of a computation. |
| <CopyableCode code="count" /> | `integer` | Number of members in the client group. Use this value together with the value of ```accuracy```. If accuracy is `exact` then the value represents the actual number of members in the cloud. When accuracy is `estimated`, the actual number of members is larger than the value of ```count```. |
| <CopyableCode code="endTime" /> | `string` | Membership interval start time. |
| <CopyableCode code="groupId" /> | `string` | Client Group URI. |
| <CopyableCode code="startTime" /> | `string` | Membership interval start time. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clientGroupName, resourceGroupName, subscriptionId, workspaceName" /> |

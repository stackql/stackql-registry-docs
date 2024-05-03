---
title: channels_with_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - channels_with_keys
  - bot_service
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
<tr><td><b>Name</b></td><td><code>channels_with_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.channels_with_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="changedTime" /> | `string` | Changed time of the resource |
| <CopyableCode code="entityTag" /> | `string` | Entity tag of the resource |
| <CopyableCode code="properties" /> | `object` | Channel definition |
| <CopyableCode code="provisioningState" /> | `string` | Provisioning state of the resource |
| <CopyableCode code="resource" /> | `object` | Channel definition |
| <CopyableCode code="setting" /> | `object` | Channel settings definition |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="channelName, resourceGroupName, resourceName, subscriptionId" /> |

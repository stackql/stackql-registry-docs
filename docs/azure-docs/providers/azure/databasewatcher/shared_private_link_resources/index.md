---
title: shared_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_private_link_resources
  - databasewatcher
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
<tr><td><b>Name</b></td><td><code>shared_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.databasewatcher.shared_private_link_resources" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sharedPrivateLinkResourceName, subscriptionId, watcherName" /> | Get a SharedPrivateLinkResource |
| <CopyableCode code="list_by_watcher" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, watcherName" /> | List SharedPrivateLinkResource resources by Watcher |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sharedPrivateLinkResourceName, subscriptionId, watcherName" /> | Create a SharedPrivateLinkResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sharedPrivateLinkResourceName, subscriptionId, watcherName" /> | Delete a SharedPrivateLinkResource |

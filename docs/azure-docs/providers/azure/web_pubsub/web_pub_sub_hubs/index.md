---
title: web_pub_sub_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - web_pub_sub_hubs
  - web_pubsub
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
<tr><td><b>Name</b></td><td><code>web_pub_sub_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web_pubsub.web_pub_sub_hubs" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, resourceName, subscriptionId" /> | Get a hub setting. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | List hub settings. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hubName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Create or update a hub setting. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hubName, resourceGroupName, resourceName, subscriptionId" /> | Delete a hub setting. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | List hub settings. |

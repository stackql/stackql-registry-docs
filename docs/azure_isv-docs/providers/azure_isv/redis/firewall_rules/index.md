---
title: firewall_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_rules
  - redis
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>firewall_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis.firewall_rules" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cacheName, resourceGroupName, ruleName, subscriptionId" /> | Gets a single firewall rule in a specified redis cache. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Gets all firewall rules in the specified redis cache. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cacheName, resourceGroupName, ruleName, subscriptionId, data__properties" /> | Create or update a redis cache firewall rule |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cacheName, resourceGroupName, ruleName, subscriptionId" /> | Deletes a single firewall rule in a specified redis cache. |

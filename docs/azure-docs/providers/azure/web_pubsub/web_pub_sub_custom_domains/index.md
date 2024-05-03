---
title: web_pub_sub_custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - web_pub_sub_custom_domains
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
<tr><td><b>Name</b></td><td><code>web_pub_sub_custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web_pubsub.web_pub_sub_custom_domains" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, resourceName, subscriptionId" /> | Get a custom domain. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | List all custom domains. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Create or update a custom domain. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, resourceName, subscriptionId" /> | Delete a custom domain. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | List all custom domains. |

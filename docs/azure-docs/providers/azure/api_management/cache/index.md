---
title: cache
hide_title: false
hide_table_of_contents: false
keywords:
  - cache
  - api_management
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
<tr><td><b>Name</b></td><td><code>cache</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.cache" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cacheId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the Cache specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of all external Caches in the specified service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cacheId, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates an External Cache to be used in Api Management instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, cacheId, resourceGroupName, serviceName, subscriptionId" /> | Deletes specific Cache. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, cacheId, resourceGroupName, serviceName, subscriptionId" /> | Updates the details of the cache specified by its identifier. |

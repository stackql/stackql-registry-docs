---
title: content_item
hide_title: false
hide_table_of_contents: false
keywords:
  - content_item
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
<tr><td><b>Name</b></td><td><code>content_item</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.content_item" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="contentItemId, contentTypeId, resourceGroupName, serviceName, subscriptionId" /> | Returns the developer portal's content item specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="contentTypeId, resourceGroupName, serviceName, subscriptionId" /> | Lists developer portal's content items specified by the provided content type. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="contentItemId, contentTypeId, resourceGroupName, serviceName, subscriptionId" /> | Creates a new developer portal's content item specified by the provided content type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, contentItemId, contentTypeId, resourceGroupName, serviceName, subscriptionId" /> | Removes the specified developer portal's content item. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="contentTypeId, resourceGroupName, serviceName, subscriptionId" /> | Lists developer portal's content items specified by the provided content type. |

---
title: tag_api_link
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_api_link
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
<tr><td><b>Name</b></td><td><code>tag_api_link</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.tag_api_link" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiLinkId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Gets the API link for the tag. |
| <CopyableCode code="list_by_product" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, tagId" /> | Lists a collection of the API links associated with a tag. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiLinkId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Adds an API to the specified tag via link. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiLinkId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Deletes the specified API from the specified tag. |
| <CopyableCode code="_list_by_product" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, tagId" /> | Lists a collection of the API links associated with a tag. |

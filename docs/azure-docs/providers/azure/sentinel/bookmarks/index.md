---
title: bookmarks
hide_title: false
hide_table_of_contents: false
keywords:
  - bookmarks
  - sentinel
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
<tr><td><b>Name</b></td><td><code>bookmarks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.bookmarks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Describes bookmark properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bookmarkId, resourceGroupName, subscriptionId, workspaceName" /> | Gets a bookmark. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all bookmarks. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="bookmarkId, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates the bookmark. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bookmarkId, resourceGroupName, subscriptionId, workspaceName" /> | Delete the bookmark. |

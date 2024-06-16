---
title: afd_origins
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_origins
  - cdn
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
<tr><td><b>Name</b></td><td><code>afd_origins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.afd_origins" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="originGroupName, originName, profileName, resourceGroupName, subscriptionId" /> | Gets an existing origin within an origin group. |
| <CopyableCode code="list_by_origin_group" /> | `SELECT` | <CopyableCode code="originGroupName, profileName, resourceGroupName, subscriptionId" /> | Lists all of the existing origins within an origin group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="originGroupName, originName, profileName, resourceGroupName, subscriptionId" /> | Creates a new origin within the specified origin group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="originGroupName, originName, profileName, resourceGroupName, subscriptionId" /> | Deletes an existing origin within an origin group. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="originGroupName, originName, profileName, resourceGroupName, subscriptionId" /> | Updates an existing origin within an origin group. |

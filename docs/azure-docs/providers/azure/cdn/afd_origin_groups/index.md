---
title: afd_origin_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_origin_groups
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
<tr><td><b>Name</b></td><td><code>afd_origin_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.afd_origin_groups" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="originGroupName, profileName, resourceGroupName, subscriptionId" /> | Gets an existing origin group within a profile. |
| <CopyableCode code="list_by_profile" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Lists all of the existing origin groups within a profile. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="originGroupName, profileName, resourceGroupName, subscriptionId" /> | Creates a new origin group within the specified profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="originGroupName, profileName, resourceGroupName, subscriptionId" /> | Deletes an existing origin group within a profile. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="originGroupName, profileName, resourceGroupName, subscriptionId" /> | Updates an existing origin group within a profile. |

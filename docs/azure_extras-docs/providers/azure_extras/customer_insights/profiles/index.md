---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - customer_insights
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The profile type definition. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, profileName, resourceGroupName, subscriptionId" /> | Gets information about the specified profile. |
| <CopyableCode code="list_by_hub" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all profile in the hub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hubName, profileName, resourceGroupName, subscriptionId" /> | Creates a profile within a Hub, or updates an existing profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hubName, profileName, resourceGroupName, subscriptionId" /> | Deletes a profile within a hub |
| <CopyableCode code="_list_by_hub" /> | `EXEC` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all profile in the hub. |

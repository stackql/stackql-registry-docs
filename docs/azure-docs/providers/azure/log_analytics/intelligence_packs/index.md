---
title: intelligence_packs
hide_title: false
hide_table_of_contents: false
keywords:
  - intelligence_packs
  - log_analytics
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
<tr><td><b>Name</b></td><td><code>intelligence_packs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.intelligence_packs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the intelligence pack. |
| <CopyableCode code="displayName" /> | `string` | The display name of the intelligence pack. |
| <CopyableCode code="enabled" /> | `boolean` | The enabled boolean for the intelligence pack. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Lists all the intelligence packs possible and whether they are enabled or disabled for a given workspace. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="intelligencePackName, resourceGroupName, subscriptionId, workspaceName" /> | Disables an intelligence pack for a given workspace. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="intelligencePackName, resourceGroupName, subscriptionId, workspaceName" /> | Enables an intelligence pack for a given workspace. |

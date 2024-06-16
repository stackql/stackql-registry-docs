---
title: defender_for_ai_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - defender_for_ai_settings
  - cognitive_services
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
<tr><td><b>Name</b></td><td><code>defender_for_ai_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.defender_for_ai_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource Etag. |
| <CopyableCode code="properties" /> | `object` | The Defender for AI resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, defenderForAISettingName, resourceGroupName, subscriptionId" /> | Gets the specified Defender for AI setting by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the Defender for AI settings. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, defenderForAISettingName, resourceGroupName, subscriptionId" /> | Creates or Updates the specified Defender for AI setting. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, defenderForAISettingName, resourceGroupName, subscriptionId" /> | Updates the specified Defender for AI setting. |

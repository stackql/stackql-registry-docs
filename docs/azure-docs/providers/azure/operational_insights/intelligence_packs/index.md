---
title: intelligence_packs
hide_title: false
hide_table_of_contents: false
keywords:
  - intelligence_packs
  - operational_insights
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>intelligence_packs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operational_insights.intelligence_packs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the intelligence pack. |
| `displayName` | `string` | The display name of the intelligence pack. |
| `enabled` | `boolean` | The enabled boolean for the intelligence pack. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IntelligencePacks_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Lists all the intelligence packs possible and whether they are enabled or disabled for a given workspace. |
| `IntelligencePacks_Disable` | `EXEC` | `intelligencePackName, resourceGroupName, subscriptionId, workspaceName` | Disables an intelligence pack for a given workspace. |
| `IntelligencePacks_Enable` | `EXEC` | `intelligencePackName, resourceGroupName, subscriptionId, workspaceName` | Enables an intelligence pack for a given workspace. |

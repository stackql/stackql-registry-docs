---
title: product_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - product_settings
  - security_insights
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
<tr><td><b>Name</b></td><td><code>product_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.product_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `kind` | `string` | The kind of the setting |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProductSettings_Get` | `SELECT` | `resourceGroupName, settingsName, subscriptionId, workspaceName` | Gets a setting. |
| `ProductSettings_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List of all the settings |
| `ProductSettings_Delete` | `DELETE` | `resourceGroupName, settingsName, subscriptionId, workspaceName` | Delete setting of the product. |
| `ProductSettings_Update` | `EXEC` | `resourceGroupName, settingsName, subscriptionId, workspaceName, data__kind` | Updates setting. |

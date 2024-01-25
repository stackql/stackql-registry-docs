---
title: rai_blocklist_items
hide_title: false
hide_table_of_contents: false
keywords:
  - rai_blocklist_items
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rai_blocklist_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cognitive_services.rai_blocklist_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Resource Etag. |
| `properties` | `object` | RAI Custom Blocklist Item properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, raiBlocklistItemName, raiBlocklistName, resourceGroupName, subscriptionId` | Gets the specified custom blocklist Item associated with the custom blocklist. |
| `list` | `SELECT` | `accountName, raiBlocklistName, resourceGroupName, subscriptionId` | Gets the blocklist items associated with the custom blocklist. |
| `create_or_update` | `INSERT` | `accountName, raiBlocklistItemName, raiBlocklistName, resourceGroupName, subscriptionId` | Update the state of specified blocklist item associated with the Azure OpenAI account. |
| `delete` | `DELETE` | `accountName, raiBlocklistItemName, raiBlocklistName, resourceGroupName, subscriptionId` | Deletes the specified blocklist Item associated with the custom blocklist. |
| `_list` | `EXEC` | `accountName, raiBlocklistName, resourceGroupName, subscriptionId` | Gets the blocklist items associated with the custom blocklist. |

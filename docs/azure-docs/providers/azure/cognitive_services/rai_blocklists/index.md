---
title: rai_blocklists
hide_title: false
hide_table_of_contents: false
keywords:
  - rai_blocklists
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
<tr><td><b>Name</b></td><td><code>rai_blocklists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cognitive_services.rai_blocklists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Resource Etag. |
| `properties` | `object` | RAI Custom Blocklist properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, raiBlocklistName, resourceGroupName, subscriptionId` | Gets the specified custom blocklist associated with the Azure OpenAI account. |
| `list` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the custom blocklists associated with the Azure OpenAI account. |
| `create_or_update` | `INSERT` | `accountName, raiBlocklistName, resourceGroupName, subscriptionId` | Update the state of specified blocklist associated with the Azure OpenAI account. |
| `delete` | `DELETE` | `accountName, raiBlocklistName, resourceGroupName, subscriptionId` | Deletes the specified custom blocklist associated with the Azure OpenAI account. |
| `_list` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Gets the custom blocklists associated with the Azure OpenAI account. |

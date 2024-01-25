---
title: encryption_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - encryption_scopes
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
<tr><td><b>Name</b></td><td><code>encryption_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cognitive_services.encryption_scopes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Resource Etag. |
| `properties` | `object` | Properties to EncryptionScope |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, encryptionScopeName, resourceGroupName, subscriptionId` | Gets the specified EncryptionScope associated with the Cognitive Services account. |
| `list` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the content filters associated with the Azure OpenAI account. |
| `create_or_update` | `INSERT` | `accountName, encryptionScopeName, resourceGroupName, subscriptionId` | Update the state of specified encryptionScope associated with the Cognitive Services account. |
| `delete` | `DELETE` | `accountName, encryptionScopeName, resourceGroupName, subscriptionId` | Deletes the specified encryptionScope associated with the Cognitive Services account. |
| `_list` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Gets the content filters associated with the Azure OpenAI account. |

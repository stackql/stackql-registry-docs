---
title: api_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - api_keys
  - application_insights
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
<tr><td><b>Name</b></td><td><code>api_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.api_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID of the API key inside an Application Insights component. It is auto generated when the API key is created. |
| `name` | `string` | The name of the API key. |
| `linkedWriteProperties` | `array` | The write access rights of this API Key. |
| `apiKey` | `string` | The API key value. It will be only return once when the API Key was created. |
| `createdDate` | `string` | The create date of this API key. |
| `linkedReadProperties` | `array` | The read access rights of this API Key. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `APIKeys_Get` | `SELECT` | `keyId, resourceGroupName, resourceName, subscriptionId` | Get the API Key for this key id. |
| `APIKeys_List` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Gets a list of API keys of an Application Insights component. |
| `APIKeys_Create` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create an API Key of an Application Insights component. |
| `APIKeys_Delete` | `DELETE` | `keyId, resourceGroupName, resourceName, subscriptionId` | Delete an API Key of an Application Insights component. |

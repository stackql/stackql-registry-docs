---
title: content_key_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - content_key_policies
  - media_services
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>content_key_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.media_services.content_key_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The properties of the Content Key Policy. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ContentKeyPolicies_Get` | `SELECT` | `accountName, api-version, contentKeyPolicyName, resourceGroupName, subscriptionId` | Get the details of a Content Key Policy in the Media Services account |
| `ContentKeyPolicies_List` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | Lists the Content Key Policies in the account |
| `ContentKeyPolicies_CreateOrUpdate` | `INSERT` | `accountName, api-version, contentKeyPolicyName, resourceGroupName, subscriptionId` | Create or update a Content Key Policy in the Media Services account |
| `ContentKeyPolicies_Delete` | `DELETE` | `accountName, api-version, contentKeyPolicyName, resourceGroupName, subscriptionId` | Deletes a Content Key Policy in the Media Services account |
| `ContentKeyPolicies_GetPolicyPropertiesWithSecrets` | `EXEC` | `accountName, api-version, contentKeyPolicyName, resourceGroupName, subscriptionId` | Get a Content Key Policy including secret values |
| `ContentKeyPolicies_Update` | `EXEC` | `accountName, api-version, contentKeyPolicyName, resourceGroupName, subscriptionId` | Updates an existing Content Key Policy in the Media Services account |

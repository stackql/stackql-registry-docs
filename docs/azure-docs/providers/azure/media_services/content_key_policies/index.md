---
title: content_key_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - content_key_policies
  - media_services
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
<tr><td><b>Name</b></td><td><code>content_key_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.media_services.content_key_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The properties of the Content Key Policy. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, api-version, contentKeyPolicyName, resourceGroupName, subscriptionId` | Get the details of a Content Key Policy in the Media Services account |
| `list` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | Lists the Content Key Policies in the account |
| `create_or_update` | `INSERT` | `accountName, api-version, contentKeyPolicyName, resourceGroupName, subscriptionId` | Create or update a Content Key Policy in the Media Services account |
| `delete` | `DELETE` | `accountName, api-version, contentKeyPolicyName, resourceGroupName, subscriptionId` | Deletes a Content Key Policy in the Media Services account |
| `_list` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Lists the Content Key Policies in the account |
| `update` | `EXEC` | `accountName, api-version, contentKeyPolicyName, resourceGroupName, subscriptionId` | Updates an existing Content Key Policy in the Media Services account |

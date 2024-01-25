---
title: streaming_locators
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_locators
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
<tr><td><b>Name</b></td><td><code>streaming_locators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.media_services.streaming_locators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of the Streaming Locator. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, api-version, resourceGroupName, streamingLocatorName, subscriptionId` | Get the details of a Streaming Locator in the Media Services account |
| `list` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | Lists the Streaming Locators in the account |
| `create` | `INSERT` | `accountName, api-version, resourceGroupName, streamingLocatorName, subscriptionId` | Create a Streaming Locator in the Media Services account |
| `delete` | `DELETE` | `accountName, api-version, resourceGroupName, streamingLocatorName, subscriptionId` | Deletes a Streaming Locator in the Media Services account |
| `_list` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Lists the Streaming Locators in the account |

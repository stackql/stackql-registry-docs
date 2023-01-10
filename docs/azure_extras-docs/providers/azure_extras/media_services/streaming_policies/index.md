---
title: streaming_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_policies
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
<tr><td><b>Name</b></td><td><code>streaming_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.media_services.streaming_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Class to specify properties of Streaming Policy |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `StreamingPolicies_Get` | `SELECT` | `accountName, api-version, resourceGroupName, streamingPolicyName, subscriptionId` | Get the details of a Streaming Policy in the Media Services account |
| `StreamingPolicies_List` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | Lists the Streaming Policies in the account |
| `StreamingPolicies_Create` | `INSERT` | `accountName, api-version, resourceGroupName, streamingPolicyName, subscriptionId` | Create a Streaming Policy in the Media Services account |
| `StreamingPolicies_Delete` | `DELETE` | `accountName, api-version, resourceGroupName, streamingPolicyName, subscriptionId` | Deletes a Streaming Policy in the Media Services account |

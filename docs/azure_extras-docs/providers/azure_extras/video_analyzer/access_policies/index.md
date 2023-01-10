---
title: access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policies
  - video_analyzer
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
<tr><td><b>Name</b></td><td><code>access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.video_analyzer.access_policies</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AccessPolicies_Get` | `SELECT` | `accessPolicyName, accountName, resourceGroupName, subscriptionId` | Retrieves an existing access policy resource with the given name. |
| `AccessPolicies_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Retrieves all existing access policy resources, along with their JSON representations. |
| `AccessPolicies_CreateOrUpdate` | `INSERT` | `accessPolicyName, accountName, resourceGroupName, subscriptionId` | Creates a new access policy resource or updates an existing one with the given name. |
| `AccessPolicies_Delete` | `DELETE` | `accessPolicyName, accountName, resourceGroupName, subscriptionId` | Deletes an existing access policy resource with the given name. |
| `AccessPolicies_Update` | `EXEC` | `accessPolicyName, accountName, resourceGroupName, subscriptionId` | Updates individual properties of an existing access policy resource with the given name. |

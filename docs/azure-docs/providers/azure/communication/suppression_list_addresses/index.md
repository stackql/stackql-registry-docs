---
title: suppression_list_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - suppression_list_addresses
  - communication
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
<tr><td><b>Name</b></td><td><code>suppression_list_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.communication.suppression_list_addresses</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `addressId, domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName` | Get a SuppressionListAddress. |
| `list` | `SELECT` | `domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName` | Get all the addresses in a suppression list. |
| `create_or_update` | `INSERT` | `addressId, domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName` | Create or update a SuppressionListAddress. |
| `delete` | `DELETE` | `addressId, domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName` | Operation to delete a single address from a suppression list. |
| `_list` | `EXEC` | `domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName` | Get all the addresses in a suppression list. |

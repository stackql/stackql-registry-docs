---
title: publishers
hide_title: false
hide_table_of_contents: false
keywords:
  - publishers
  - edge_marketplace
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
<tr><td><b>Name</b></td><td><code>publishers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.edge_marketplace.publishers</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `publisherName, resourceUri` | Get a Publisher |
| `list` | `SELECT` | `resourceUri` | List Publisher resources by parent |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List Publisher resources in subscription |
| `_list` | `EXEC` | `resourceUri` | List Publisher resources by parent |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List Publisher resources in subscription |

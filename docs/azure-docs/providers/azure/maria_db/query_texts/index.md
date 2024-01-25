---
title: query_texts
hide_title: false
hide_table_of_contents: false
keywords:
  - query_texts
  - maria_db
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
<tr><td><b>Name</b></td><td><code>query_texts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maria_db.query_texts</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `queryId, resourceGroupName, serverName, subscriptionId` | Retrieve the Query-Store query texts for the queryId. |
| `list_by_server` | `SELECT` | `queryIds, resourceGroupName, serverName, subscriptionId` | Retrieve the Query-Store query texts for specified queryIds. |
| `_list_by_server` | `EXEC` | `queryIds, resourceGroupName, serverName, subscriptionId` | Retrieve the Query-Store query texts for specified queryIds. |

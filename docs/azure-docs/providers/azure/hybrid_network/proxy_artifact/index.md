---
title: proxy_artifact
hide_title: false
hide_table_of_contents: false
keywords:
  - proxy_artifact
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>proxy_artifact</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.proxy_artifact</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `artifactName, artifactStoreName, publisherName, resourceGroupName, subscriptionId` |
| `_get` | `EXEC` | `artifactName, artifactStoreName, publisherName, resourceGroupName, subscriptionId` |

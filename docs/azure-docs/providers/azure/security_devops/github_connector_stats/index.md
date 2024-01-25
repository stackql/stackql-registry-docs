---
title: github_connector_stats
hide_title: false
hide_table_of_contents: false
keywords:
  - github_connector_stats
  - security_devops
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
<tr><td><b>Name</b></td><td><code>github_connector_stats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_devops.github_connector_stats</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `gitHubConnectorName, resourceGroupName, subscriptionId` |
| `_get` | `EXEC` | `gitHubConnectorName, resourceGroupName, subscriptionId` |

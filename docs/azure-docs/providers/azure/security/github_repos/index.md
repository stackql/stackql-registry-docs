---
title: github_repos
hide_title: false
hide_table_of_contents: false
keywords:
  - github_repos
  - security
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
<tr><td><b>Name</b></td><td><code>github_repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.github_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | GitHub Repository properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `ownerName, repoName, resourceGroupName, securityConnectorName, subscriptionId` |
| `list` | `SELECT` | `ownerName, resourceGroupName, securityConnectorName, subscriptionId` |
| `_list` | `EXEC` | `ownerName, resourceGroupName, securityConnectorName, subscriptionId` |

---
title: git_lab_projects
hide_title: false
hide_table_of_contents: false
keywords:
  - git_lab_projects
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
<tr><td><b>Name</b></td><td><code>git_lab_projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.git_lab_projects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | GitLab Project properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `groupFQName, projectName, resourceGroupName, securityConnectorName, subscriptionId` |
| `list` | `SELECT` | `groupFQName, resourceGroupName, securityConnectorName, subscriptionId` |
| `_list` | `EXEC` | `groupFQName, resourceGroupName, securityConnectorName, subscriptionId` |

---
title: azure_dev_ops_orgs
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_dev_ops_orgs
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
<tr><td><b>Name</b></td><td><code>azure_dev_ops_orgs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.azure_dev_ops_orgs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Azure DevOps Organization properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `orgName, resourceGroupName, securityConnectorName, subscriptionId` |
| `list` | `SELECT` | `resourceGroupName, securityConnectorName, subscriptionId` |
| `create_or_update` | `INSERT` | `orgName, resourceGroupName, securityConnectorName, subscriptionId` |
| `_list` | `EXEC` | `resourceGroupName, securityConnectorName, subscriptionId` |
| `update` | `EXEC` | `orgName, resourceGroupName, securityConnectorName, subscriptionId` |

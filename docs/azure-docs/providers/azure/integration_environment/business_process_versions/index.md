---
title: business_process_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - business_process_versions
  - integration_environment
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
<tr><td><b>Name</b></td><td><code>business_process_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.integration_environment.business_process_versions</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `applicationName, businessProcessName, businessProcessVersion, resourceGroupName, spaceName, subscriptionId` | Get a BusinessProcessVersion |
| `list_by_business_process` | `SELECT` | `applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId` | List BusinessProcessVersion resources by BusinessProcess |
| `_list_by_business_process` | `EXEC` | `applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId` | List BusinessProcessVersion resources by BusinessProcess |

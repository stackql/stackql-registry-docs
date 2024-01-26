---
title: script_cmdlets
hide_title: false
hide_table_of_contents: false
keywords:
  - script_cmdlets
  - vmware
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>script_cmdlets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.vmware.script_cmdlets</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `privateCloudName, resourceGroupName, scriptCmdletName, scriptPackageName, subscriptionId` | Return information about a script cmdlet resource in a specific package on a private cloud |
| `list` | `SELECT` | `privateCloudName, resourceGroupName, scriptPackageName, subscriptionId` | List script cmdlet resources available for a private cloud to create a script execution resource on a private cloud |
| `_list` | `EXEC` | `privateCloudName, resourceGroupName, scriptPackageName, subscriptionId` | List script cmdlet resources available for a private cloud to create a script execution resource on a private cloud |

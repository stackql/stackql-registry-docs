---
title: script_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - script_packages
  - vmware
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
<tr><td><b>Name</b></td><td><code>script_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.vmware.script_packages</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ScriptPackages_Get` | `SELECT` | `privateCloudName, resourceGroupName, scriptPackageName, subscriptionId` | Get a script package available to run on a private cloud |
| `ScriptPackages_List` | `SELECT` | `privateCloudName, resourceGroupName, subscriptionId` | List script packages available to run on the private cloud |

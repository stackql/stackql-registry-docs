---
title: os_updates
hide_title: false
hide_table_of_contents: false
keywords:
  - os_updates
  - test_base
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
<tr><td><b>Name</b></td><td><code>os_updates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.os_updates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of an OS Update. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `OSUpdates_Get` | `SELECT` | `osUpdateResourceName, packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Gets an OS Update by name in which the package was tested before. |
| `OSUpdates_List` | `SELECT` | `osUpdateType, packageName, resourceGroupName, subscriptionId, testBaseAccountName` | Lists the OS Updates in which the package were tested before. |

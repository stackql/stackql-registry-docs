---
title: available_os
hide_title: false
hide_table_of_contents: false
keywords:
  - available_os
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
<tr><td><b>Name</b></td><td><code>available_os</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.available_os</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The Available OS properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AvailableOS_Get` | `SELECT` | `availableOSResourceName, resourceGroupName, subscriptionId, testBaseAccountName` | Gets an available OS to run a package under a Test Base Account. |
| `AvailableOS_List` | `SELECT` | `osUpdateType, resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the available OSs to run a package under a Test Base Account. |

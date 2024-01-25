---
title: updates_parent
hide_title: false
hide_table_of_contents: false
keywords:
  - updates_parent
  - maintenance
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
<tr><td><b>Name</b></td><td><code>updates_parent</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maintenance.updates_parent</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `impactDurationInSec` | `integer` | Duration of impact in seconds |
| `impactType` | `string` | The impact type |
| `maintenanceScope` | `string` | The impact area |
| `notBefore` | `string` | Time when Azure will start force updates if not self-updated by customer before this time |
| `properties` | `object` | Properties for update |
| `status` | `string` | The status |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId` |
| `_list` | `EXEC` | `providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId` |

---
title: public_maintenance_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - public_maintenance_configurations
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
<tr><td><b>Name</b></td><td><code>public_maintenance_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maintenance.public_maintenance_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier of the resource |
| `name` | `string` | Name of the resource |
| `location` | `string` | Gets or sets location of the resource |
| `properties` | `object` | Properties for maintenance configuration |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Gets or sets tags of the resource |
| `type` | `string` | Type of the resource |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PublicMaintenanceConfigurations_Get` | `SELECT` | `resourceName, subscriptionId` |
| `PublicMaintenanceConfigurations_List` | `SELECT` | `subscriptionId` |

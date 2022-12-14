---
title: supported_operating_systems
hide_title: false
hide_table_of_contents: false
keywords:
  - supported_operating_systems
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>supported_operating_systems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.supported_operating_systems</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `location` | `string` | Resource Location |
| `properties` | `object` | Supported operating systems properties. |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SupportedOperatingSystems_Get` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` |

---
title: capabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - capabilities
  - sql
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
<tr><td><b>Name</b></td><td><code>capabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.capabilities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The location name. |
| `reason` | `string` | The reason for the capability not being available. |
| `status` | `string` | The status of the capability. |
| `supportedManagedInstanceVersions` | `array` | The list of supported managed instance versions. |
| `supportedServerVersions` | `array` | The list of supported server versions. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Capabilities_ListByLocation` | `SELECT` | `locationName, subscriptionId` |

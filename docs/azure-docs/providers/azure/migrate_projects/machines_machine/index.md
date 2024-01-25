---
title: machines_machine
hide_title: false
hide_table_of_contents: false
keywords:
  - machines_machine
  - migrate_projects
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
<tr><td><b>Name</b></td><td><code>machines_machine</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.migrate_projects.machines_machine</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the relative URL to get to this REST resource. |
| `name` | `string` | Gets or sets the name of this REST resource. |
| `properties` | `object` | Properties of the machine resource. |
| `type` | `string` | Gets the type of this REST resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `api-version, machineName, migrateProjectName, resourceGroupName, subscriptionId` |

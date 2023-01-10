---
title: machines
hide_title: false
hide_table_of_contents: false
keywords:
  - machines
  - migrate
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
<tr><td><b>Name</b></td><td><code>machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.migrate.machines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Path reference to this machine. /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Migrate/assessmentProjects/&#123;projectName&#125;/machines/&#123;machineName&#125; |
| `name` | `string` | Name of the machine. It is a GUID which is unique identifier of machine in private data center. For user-readable name, we have a displayName property on this machine. |
| `properties` | `object` | Properties of a machine. |
| `type` | `string` | Type of the object = [Microsoft.Migrate/assessmentProjects/machines]. |
| `eTag` | `string` | For optimistic concurrency control. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Machines_Get` | `SELECT` | `api-version, machineName, projectName, resourceGroupName, subscriptionId` | Get the machine with the specified name. Returns a json object of type 'machine' defined in Models section. |
| `Machines_ListByProject` | `SELECT` | `api-version, projectName, resourceGroupName, subscriptionId` | Get data of all the machines available in the project. Returns a json array of objects of type 'machine' defined in Models section. |

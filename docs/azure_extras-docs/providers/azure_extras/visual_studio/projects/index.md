---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - visual_studio
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
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.visual_studio.projects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier of the resource. |
| `name` | `string` | Resource name. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Key/value pair of resource properties. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, rootResourceName, subscriptionId` | Gets the details of a Team Services project resource. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, rootResourceName, subscriptionId` | Gets all Visual Studio Team Services project resources created in the specified Team Services account. |
| `create` | `INSERT` | `resourceGroupName, resourceName, rootResourceName, subscriptionId` | Creates a Team Services project in the collection with the specified name. 'VersionControlOption' and 'ProcessTemplateId' must be specified in the resource properties. Valid values for VersionControlOption: Git, Tfvc. Valid values for ProcessTemplateId: 6B724908-EF14-45CF-84F8-768B5384DA45, ADCC42AB-9882-485E-A3ED-7678F01F66BC, 27450541-8E31-4150-9947-DC59F998FC01 (these IDs correspond to Scrum, Agile, and CMMI process templates). |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, rootResourceName, subscriptionId` | Gets all Visual Studio Team Services project resources created in the specified Team Services account. |
| `update` | `EXEC` | `resourceGroupName, resourceName, rootResourceName, subscriptionId` | Updates the tags of the specified Team Services project. |

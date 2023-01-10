---
title: arm_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - arm_templates
  - dev_test_labs
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
<tr><td><b>Name</b></td><td><code>arm_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_test_labs.arm_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `type` | `string` | The type of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | Properties of an Azure Resource Manager template. |
| `tags` | `object` | The tags of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ArmTemplates_Get` | `SELECT` | `api-version, artifactSourceName, labName, name, resourceGroupName, subscriptionId` | Get azure resource manager template. |
| `ArmTemplates_List` | `SELECT` | `api-version, artifactSourceName, labName, resourceGroupName, subscriptionId` | List azure resource manager templates in a given artifact source. |

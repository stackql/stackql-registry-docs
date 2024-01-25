---
title: virtual_machine_image_templates_run_outputs
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_image_templates_run_outputs
  - image_builder
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
<tr><td><b>Name</b></td><td><code>virtual_machine_image_templates_run_outputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.image_builder.virtual_machine_image_templates_run_outputs</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `imageTemplateName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `imageTemplateName, resourceGroupName, subscriptionId` |

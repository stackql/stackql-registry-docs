---
title: features
hide_title: false
hide_table_of_contents: false
keywords:
  - features
  - compute_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.compute_admin.features</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties of features. |
| `type` | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `featureName, location, subscriptionId` | Get an existing feature. |
| `list` | `SELECT` | `location, subscriptionId` | Get a list of existing features. |
| `_list` | `EXEC` | `location, subscriptionId` | Get a list of existing features. |
| `features` | `EXEC` | `featureName, location, subscriptionId` | Disable the tenant subscription feature. |

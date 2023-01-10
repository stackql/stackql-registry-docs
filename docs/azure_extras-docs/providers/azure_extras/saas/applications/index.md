---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - saas
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.saas.applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | the resource Id. |
| `name` | `string` | the resource name. |
| `properties` | `object` | Saas resource properties. |
| `tags` | `object` | the resource tags. |
| `type` | `string` | the resource type. |
| `location` | `string` | the resource location. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Applications_List` | `SELECT` | `resourceGroupName, subscriptionId` |

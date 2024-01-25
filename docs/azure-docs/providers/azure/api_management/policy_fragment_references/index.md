---
title: policy_fragment_references
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_fragment_references
  - api_management
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
<tr><td><b>Name</b></td><td><code>policy_fragment_references</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.policy_fragment_references</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `count` | `integer` | Total record count number. |
| `nextLink` | `string` | Next page link if any. |
| `value` | `array` | A collection of resources. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `id, resourceGroupName, serviceName, subscriptionId` |

---
title: locations_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_usages
  - hdinsight
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
<tr><td><b>Name</b></td><td><code>locations_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hdinsight.locations_usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | The details about the localizable name of a type of usage. |
| `currentValue` | `integer` | The current usage. |
| `limit` | `integer` | The maximum allowed usage. |
| `unit` | `string` | The type of measurement for usage. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `location, subscriptionId` |
| `_list` | `EXEC` | `location, subscriptionId` |

---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - vmware_cloud_simple
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.vmware_cloud_simple.usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | User name model |
| `currentValue` | `integer` | The current usage value |
| `limit` | `integer` | limit of a given sku in a region for a subscription. The maximum permitted value for the usage quota. If there is no limit, this value will be -1 |
| `unit` | `string` | The usages' unit |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `api-version, regionId, subscriptionId` |
| `_list` | `EXEC` | `api-version, regionId, subscriptionId` |

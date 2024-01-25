---
title: record_sets_all_by_dns_zone
hide_title: false
hide_table_of_contents: false
keywords:
  - record_sets_all_by_dns_zone
  - dns
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
<tr><td><b>Name</b></td><td><code>record_sets_all_by_dns_zone</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dns.record_sets_all_by_dns_zone</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the record set. |
| `name` | `string` | The name of the record set. |
| `etag` | `string` | The etag of the record set. |
| `properties` | `object` | Represents the properties of the records in the record set. |
| `type` | `string` | The type of the record set. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, subscriptionId, zoneName` |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, zoneName` |

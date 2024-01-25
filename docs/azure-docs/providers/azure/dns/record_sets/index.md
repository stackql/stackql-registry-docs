---
title: record_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - record_sets
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
<tr><td><b>Name</b></td><td><code>record_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dns.record_sets</code></td></tr>
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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `recordType, relativeRecordSetName, resourceGroupName, subscriptionId, zoneName` | Gets a record set. |
| `list_by_dns_zone` | `SELECT` | `resourceGroupName, subscriptionId, zoneName` | Lists all record sets in a DNS zone. |
| `list_by_type` | `SELECT` | `recordType, resourceGroupName, subscriptionId, zoneName` | Lists the record sets of a specified type in a DNS zone. |
| `create_or_update` | `INSERT` | `recordType, relativeRecordSetName, resourceGroupName, subscriptionId, zoneName` | Creates or updates a record set within a DNS zone. Record sets of type SOA can be updated but not created (they are created when the DNS zone is created). |
| `delete` | `DELETE` | `recordType, relativeRecordSetName, resourceGroupName, subscriptionId, zoneName` | Deletes a record set from a DNS zone. This operation cannot be undone. Record sets of type SOA cannot be deleted (they are deleted when the DNS zone is deleted). |
| `_list_by_dns_zone` | `EXEC` | `resourceGroupName, subscriptionId, zoneName` | Lists all record sets in a DNS zone. |
| `_list_by_type` | `EXEC` | `recordType, resourceGroupName, subscriptionId, zoneName` | Lists the record sets of a specified type in a DNS zone. |
| `update` | `EXEC` | `recordType, relativeRecordSetName, resourceGroupName, subscriptionId, zoneName` | Updates a record set within a DNS zone. |

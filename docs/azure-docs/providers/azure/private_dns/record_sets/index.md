---
title: record_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - record_sets
  - private_dns
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
<tr><td><b>Id</b></td><td><code>azure.private_dns.record_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the record set. |
| `name` | `string` | The name of the record set. |
| `properties` | `object` | Represents the properties of the records in the record set. |
| `type` | `string` | The type of the record set. |
| `etag` | `string` | The ETag of the record set. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RecordSets_Get` | `SELECT` | `privateZoneName, recordType, relativeRecordSetName, resourceGroupName, subscriptionId` | Gets a record set. |
| `RecordSets_List` | `SELECT` | `privateZoneName, resourceGroupName, subscriptionId` | Lists all record sets in a Private DNS zone. |
| `RecordSets_ListByType` | `SELECT` | `privateZoneName, recordType, resourceGroupName, subscriptionId` | Lists the record sets of a specified type in a Private DNS zone. |
| `RecordSets_CreateOrUpdate` | `INSERT` | `privateZoneName, recordType, relativeRecordSetName, resourceGroupName, subscriptionId` | Creates or updates a record set within a Private DNS zone. |
| `RecordSets_Delete` | `DELETE` | `privateZoneName, recordType, relativeRecordSetName, resourceGroupName, subscriptionId` | Deletes a record set from a Private DNS zone. This operation cannot be undone. |
| `RecordSets_Update` | `EXEC` | `privateZoneName, recordType, relativeRecordSetName, resourceGroupName, subscriptionId` | Updates a record set within a Private DNS zone. |

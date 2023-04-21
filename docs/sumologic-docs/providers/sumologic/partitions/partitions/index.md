---
title: partitions
hide_title: false
hide_table_of_contents: false
keywords:
  - partitions
  - partitions
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.partitions.partitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier for the partition. |
| `name` | `string` | The name of the partition. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `retentionPeriod` | `integer` | The number of days to retain data in the partition, or -1 to use the default value for your account.  Only relevant if your account has variable retention enabled. |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `indexType` | `string` | This has the value `DefaultIndex`, `AuditIndex`or `Partition` depending upon the type of partition. |
| `totalBytes` | `integer` | Size of data in partition in bytes. |
| `analyticsTier` | `string` | The Data Tier where the data in the partition will reside. Possible values are:<br />              1. `continuous`<br />              2. `frequent`<br />              3. `infrequent`<br />Note: The "infrequent" and "frequent" tiers are only available to Cloud Flex Credits Enterprise Suite accounts. |
| `routingExpression` | `string` | The query that defines the data to be included in the partition. |
| `retentionEffectiveAt` | `string` | When the newRetentionPeriod will become effective in UTC format. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `dataForwardingId` | `string` | Id of the data forwarding configuration to be used by the partition. |
| `isActive` | `boolean` | This has the value `true` if the partition is active and `false` if it has been decommissioned. |
| `newRetentionPeriod` | `integer` | If the retention period is scheduled to be updated in the future (i.e., if retention period is previously reduced with value of reduceRetentionPeriodImmediately as false), this property gives the future value of retention period while retentionPeriod gives the current value. retentionPeriod will take up the value of newRetentionPeriod after the scheduled time. |
| `isCompliant` | `boolean` | Whether the partition is compliant or not. Mark a partition as compliant if it contains data used for compliance or audit purpose. Retention for a compliant partition can only be increased and cannot be reduced after the partition is marked compliant. A partition once marked compliant, cannot be marked non-compliant later. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getPartition` | `SELECT` | `id` | Get a partition with the given identifier from the organization. |
| `listPartitions` | `SELECT` |  | Get a list of all partitions in the organization. The response is paginated with a default limit of 100 partitions per page. |
| `createPartition` | `INSERT` | `data__name, data__routingExpression` | Create a new partition. |
| `updatePartition` | `EXEC` | `id` | Update an existing partition in the organization. |

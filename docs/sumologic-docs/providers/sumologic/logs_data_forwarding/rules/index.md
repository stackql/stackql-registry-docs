---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - logs_data_forwarding
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
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.logs_data_forwarding.rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique identifier of the data forwarding rule. |
| `format` | `string` | Format of the payload. |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `bucket` | `object` |  |
| `destinationId` | `string` | The data forwarding destination id. |
| `fileFormat` | `string` | Specify the path prefix to a directory in the S3 bucket and how to format the file name. |
| `payloadSchema` | `string` | Schema for the payload. |
| `indexId` | `string` | The `id` of the Partition or Scheduled View the rule applies to. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `enabled` | `boolean` | True when the data forwarding rule is enabled. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getDataForwardingRule` | `SELECT` | `indexId` | Get the details of an S3 data forwarding rule by its Partition or Scheduled View identifier. |
| `getRulesAndBuckets` | `SELECT` |  | Get a list of all S3 data forwarding rules. |
| `createDataForwardingRule` | `INSERT` | `data__destinationId, data__indexId` | Create a data forwarding rule to send data from a Partition or Scheduled View to an S3 bucket. |
| `deleteDataForwardingRule` | `DELETE` | `indexId` | Delete an S3 data forwarding rule by its Partition or Scheduled View identifier. |
| `updateDataForwardingRule` | `EXEC` | `indexId` | Update an S3 data forwarding rule by its Partition or Scheduled View identifier. |

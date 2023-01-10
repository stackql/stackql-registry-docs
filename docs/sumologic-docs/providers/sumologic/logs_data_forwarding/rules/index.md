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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getDataForwardingRule` | `SELECT` | `indexId` | Get the details of an S3 data forwarding rule by its Partition or Scheduled View identifier. |
| `getRulesAndBuckets` | `SELECT` |  | Get a list of all S3 data forwarding rules. |
| `createDataForwardingRule` | `INSERT` | `data__destinationId, data__indexId` | Create a data forwarding rule to send data from a Partition or Scheduled View to an S3 bucket. |
| `deleteDataForwardingRule` | `DELETE` | `indexId` | Delete an S3 data forwarding rule by its Partition or Scheduled View identifier. |
| `updateDataForwardingRule` | `EXEC` | `indexId` | Update an S3 data forwarding rule by its Partition or Scheduled View identifier. |

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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.logs_data_forwarding.rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique identifier of the data forwarding rule. |
| <CopyableCode code="bucket" /> | `object` |  |
| <CopyableCode code="createdAt" /> | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| <CopyableCode code="createdBy" /> | `string` | Identifier of the user who created the resource. |
| <CopyableCode code="destinationId" /> | `string` | The data forwarding destination id. |
| <CopyableCode code="enabled" /> | `boolean` | True when the data forwarding rule is enabled. |
| <CopyableCode code="fileFormat" /> | `string` | Specify the path prefix to a directory in the S3 bucket and how to format the file name. |
| <CopyableCode code="format" /> | `string` | Format of the payload. |
| <CopyableCode code="indexId" /> | `string` | The `id` of the Partition or Scheduled View the rule applies to. |
| <CopyableCode code="modifiedAt" /> | `string` | Last modification timestamp in UTC. |
| <CopyableCode code="modifiedBy" /> | `string` | Identifier of the user who last modified the resource. |
| <CopyableCode code="payloadSchema" /> | `string` | Schema for the payload. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getDataForwardingRule" /> | `SELECT` | <CopyableCode code="indexId, region" /> | Get the details of an S3 data forwarding rule by its Partition or Scheduled View identifier. |
| <CopyableCode code="getRulesAndBuckets" /> | `SELECT` | <CopyableCode code="region" /> | Get a list of all S3 data forwarding rules. |
| <CopyableCode code="createDataForwardingRule" /> | `INSERT` | <CopyableCode code="data__destinationId, data__indexId, region" /> | Create a data forwarding rule to send data from a Partition or Scheduled View to an S3 bucket. |
| <CopyableCode code="deleteDataForwardingRule" /> | `DELETE` | <CopyableCode code="indexId, region" /> | Delete an S3 data forwarding rule by its Partition or Scheduled View identifier. |
| <CopyableCode code="updateDataForwardingRule" /> | `EXEC` | <CopyableCode code="indexId, region" /> | Update an S3 data forwarding rule by its Partition or Scheduled View identifier. |

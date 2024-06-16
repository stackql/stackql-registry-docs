---
title: shares_synchronization_details
hide_title: false
hide_table_of_contents: false
keywords:
  - shares_synchronization_details
  - data_share
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>shares_synchronization_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.shares_synchronization_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the data set |
| <CopyableCode code="dataSetId" /> | `string` | Id of data set |
| <CopyableCode code="dataSetType" /> | `string` | Type of the data set |
| <CopyableCode code="durationMs" /> | `integer` | Duration of data set level copy |
| <CopyableCode code="endTime" /> | `string` | End time of data set level copy |
| <CopyableCode code="filesRead" /> | `integer` | The number of files read from the source data set |
| <CopyableCode code="filesWritten" /> | `integer` | The number of files written into the sink data set |
| <CopyableCode code="message" /> | `string` | Error message if any |
| <CopyableCode code="rowsCopied" /> | `integer` | The number of files copied into the sink data set |
| <CopyableCode code="rowsRead" /> | `integer` | The number of rows read from the source data set. |
| <CopyableCode code="sizeRead" /> | `integer` | The size of the data read from the source data set in bytes |
| <CopyableCode code="sizeWritten" /> | `integer` | The size of the data written into the sink data set in bytes |
| <CopyableCode code="startTime" /> | `string` | Start time of data set level copy |
| <CopyableCode code="status" /> | `string` | Raw Status |
| <CopyableCode code="vCore" /> | `integer` | The vCore units consumed for the data set synchronization |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, shareName, subscriptionId" /> |

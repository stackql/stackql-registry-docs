---
title: backups_latest_status
hide_title: false
hide_table_of_contents: false
keywords:
  - backups_latest_status
  - netapp
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>backups_latest_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.backups_latest_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="errorMessage" /> | `string` | Displays error message if the backup is in an error state |
| <CopyableCode code="healthy" /> | `boolean` | Backup health status |
| <CopyableCode code="lastTransferSize" /> | `integer` | Displays the last transfer size |
| <CopyableCode code="lastTransferType" /> | `string` | Displays the last transfer type |
| <CopyableCode code="mirrorState" /> | `string` | The status of the backup |
| <CopyableCode code="relationshipStatus" /> | `string` | Status of the backup mirror relationship |
| <CopyableCode code="totalTransferBytes" /> | `integer` | Displays the total bytes transferred |
| <CopyableCode code="transferProgressBytes" /> | `integer` | Displays the total number of bytes transferred for the ongoing operation |
| <CopyableCode code="unhealthyReason" /> | `string` | Reason for the unhealthy backup relationship |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> |

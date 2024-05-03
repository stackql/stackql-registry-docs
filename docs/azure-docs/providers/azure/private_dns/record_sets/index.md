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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>record_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.private_dns.record_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the record set. |
| <CopyableCode code="name" /> | `string` | The name of the record set. |
| <CopyableCode code="etag" /> | `string` | The ETag of the record set. |
| <CopyableCode code="properties" /> | `object` | Represents the properties of the records in the record set. |
| <CopyableCode code="type" /> | `string` | The type of the record set. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateZoneName, recordType, relativeRecordSetName, resourceGroupName, subscriptionId" /> | Gets a record set. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId" /> | Lists all record sets in a Private DNS zone. |
| <CopyableCode code="list_by_type" /> | `SELECT` | <CopyableCode code="privateZoneName, recordType, resourceGroupName, subscriptionId" /> | Lists the record sets of a specified type in a Private DNS zone. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateZoneName, recordType, relativeRecordSetName, resourceGroupName, subscriptionId" /> | Creates or updates a record set within a Private DNS zone. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateZoneName, recordType, relativeRecordSetName, resourceGroupName, subscriptionId" /> | Deletes a record set from a Private DNS zone. This operation cannot be undone. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId" /> | Lists all record sets in a Private DNS zone. |
| <CopyableCode code="_list_by_type" /> | `EXEC` | <CopyableCode code="privateZoneName, recordType, resourceGroupName, subscriptionId" /> | Lists the record sets of a specified type in a Private DNS zone. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="privateZoneName, recordType, relativeRecordSetName, resourceGroupName, subscriptionId" /> | Updates a record set within a Private DNS zone. |

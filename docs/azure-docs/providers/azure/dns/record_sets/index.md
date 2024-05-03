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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>record_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns.record_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the record set. |
| <CopyableCode code="name" /> | `string` | The name of the record set. |
| <CopyableCode code="etag" /> | `string` | The etag of the record set. |
| <CopyableCode code="properties" /> | `object` | Represents the properties of the records in the record set. |
| <CopyableCode code="type" /> | `string` | The type of the record set. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="recordType, relativeRecordSetName, resourceGroupName, subscriptionId, zoneName" /> | Gets a record set. |
| <CopyableCode code="list_by_dns_zone" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> | Lists all record sets in a DNS zone. |
| <CopyableCode code="list_by_type" /> | `SELECT` | <CopyableCode code="recordType, resourceGroupName, subscriptionId, zoneName" /> | Lists the record sets of a specified type in a DNS zone. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="recordType, relativeRecordSetName, resourceGroupName, subscriptionId, zoneName" /> | Creates or updates a record set within a DNS zone. Record sets of type SOA can be updated but not created (they are created when the DNS zone is created). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="recordType, relativeRecordSetName, resourceGroupName, subscriptionId, zoneName" /> | Deletes a record set from a DNS zone. This operation cannot be undone. Record sets of type SOA cannot be deleted (they are deleted when the DNS zone is deleted). |
| <CopyableCode code="_list_by_dns_zone" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> | Lists all record sets in a DNS zone. |
| <CopyableCode code="_list_by_type" /> | `EXEC` | <CopyableCode code="recordType, resourceGroupName, subscriptionId, zoneName" /> | Lists the record sets of a specified type in a DNS zone. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="recordType, relativeRecordSetName, resourceGroupName, subscriptionId, zoneName" /> | Updates a record set within a DNS zone. |

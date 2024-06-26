---
title: replication_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_policies
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>replication_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Protection profile custom data details. |
| <CopyableCode code="type" /> | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, policyName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of a replication policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Lists the replication policies for a vault. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, policyName, resourceGroupName, resourceName, subscriptionId" /> | The operation to create a replication policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, policyName, resourceGroupName, resourceName, subscriptionId" /> | The operation to delete a replication policy. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, policyName, resourceGroupName, resourceName, subscriptionId" /> | The operation to update a replication policy. |

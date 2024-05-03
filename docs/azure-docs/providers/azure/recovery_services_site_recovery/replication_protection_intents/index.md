---
title: replication_protection_intents
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protection_intents
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
<tr><td><b>Name</b></td><td><code>replication_protection_intents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_protection_intents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Replication protection intent custom data details. |
| <CopyableCode code="type" /> | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, intentObjectName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of an ASR replication protection intent. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Gets the list of ASR replication protection intent objects in the vault. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, intentObjectName, resourceGroupName, resourceName, subscriptionId" /> | The operation to create an ASR replication protection intent item. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Gets the list of ASR replication protection intent objects in the vault. |

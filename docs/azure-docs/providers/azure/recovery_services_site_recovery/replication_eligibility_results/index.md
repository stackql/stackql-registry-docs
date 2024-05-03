---
title: replication_eligibility_results
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_eligibility_results
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
<tr><td><b>Name</b></td><td><code>replication_eligibility_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_eligibility_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets Unique ARM identifier for this object. |
| <CopyableCode code="name" /> | `string` | Gets the name of this object. |
| <CopyableCode code="properties" /> | `object` | Properties model for replication eligibility results API. |
| <CopyableCode code="type" /> | `string` | Gets the object type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, virtualMachineName" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, virtualMachineName" /> |
| <CopyableCode code="exec_get" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, virtualMachineName" /> |

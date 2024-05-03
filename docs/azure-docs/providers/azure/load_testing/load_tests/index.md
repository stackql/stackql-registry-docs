---
title: load_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - load_tests
  - load_testing
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
<tr><td><b>Name</b></td><td><code>load_tests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.load_testing.load_tests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | LoadTest resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="loadTestName, resourceGroupName, subscriptionId" /> | Get a LoadTest resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists loadtest resources in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists loadtests resources in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="loadTestName, resourceGroupName, subscriptionId" /> | Create or update LoadTest resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="loadTestName, resourceGroupName, subscriptionId" /> | Delete a LoadTest resource. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists loadtest resources in a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists loadtests resources in a subscription. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="loadTestName, resourceGroupName, subscriptionId" /> | Update a loadtest resource. |

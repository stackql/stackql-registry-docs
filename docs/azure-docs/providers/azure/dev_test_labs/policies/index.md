---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - dev_test_labs
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
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a Policy. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, labName, name, policySetName, resourceGroupName, subscriptionId" /> | Get policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, labName, policySetName, resourceGroupName, subscriptionId" /> | List policies in a given policy set. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, labName, name, policySetName, resourceGroupName, subscriptionId, data__properties" /> | Create or replace an existing policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, labName, name, policySetName, resourceGroupName, subscriptionId" /> | Delete policy. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, labName, policySetName, resourceGroupName, subscriptionId" /> | List policies in a given policy set. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, labName, name, policySetName, resourceGroupName, subscriptionId" /> | Allows modifying tags of policies. All other properties will be ignored. |

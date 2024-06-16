---
title: partner_namespaces_shared_access_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_namespaces_shared_access_keys
  - event_grid
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
<tr><td><b>Name</b></td><td><code>partner_namespaces_shared_access_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.partner_namespaces_shared_access_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="key1" /> | `string` | Shared access key1 for the partner namespace. |
| <CopyableCode code="key2" /> | `string` | Shared access key2 for the partner namespace. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="partnerNamespaceName, resourceGroupName, subscriptionId" /> |

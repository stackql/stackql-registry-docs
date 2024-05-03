---
title: flighting_rings
hide_title: false
hide_table_of_contents: false
keywords:
  - flighting_rings
  - test_base
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>flighting_rings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.flighting_rings" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="flightingRingResourceName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a flighting ring of a Test Base Account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the flighting rings of a Test Base Account. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the flighting rings of a Test Base Account. |

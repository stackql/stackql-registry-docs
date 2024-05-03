---
title: available_os
hide_title: false
hide_table_of_contents: false
keywords:
  - available_os
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
<tr><td><b>Name</b></td><td><code>available_os</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.available_os" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="availableOSResourceName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets an available OS to run a package under a Test Base Account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="osUpdateType, resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the available OSs to run a package under a Test Base Account. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="osUpdateType, resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the available OSs to run a package under a Test Base Account. |

---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - elastic
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.elastic.versions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="region, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="region, subscriptionId" /> |
| <CopyableCode code="details" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |

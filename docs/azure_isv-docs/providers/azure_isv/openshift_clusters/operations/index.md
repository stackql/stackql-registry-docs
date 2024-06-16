---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - openshift_clusters
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.openshift_clusters.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Operation name: &#123;provider&#125;/&#123;resource&#125;/&#123;operation&#125;. |
| <CopyableCode code="display" /> | `object` | Display represents the display details of an operation. |
| <CopyableCode code="origin" /> | `string` | Sources of requests to this operation.  Comma separated list with valid values user or system, e.g. "user,system". |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` |  |

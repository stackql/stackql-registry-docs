---
title: recommendation_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - recommendation_metadata
  - advisor
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
<tr><td><b>Name</b></td><td><code>recommendation_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.advisor.recommendation_metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource Id of the metadata entity. |
| <CopyableCode code="name" /> | `string` | The name of the metadata entity. |
| <CopyableCode code="properties" /> | `object` | The metadata entity properties |
| <CopyableCode code="type" /> | `string` | The type of the metadata entity. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name" /> |
| <CopyableCode code="list" /> | `SELECT` |  |

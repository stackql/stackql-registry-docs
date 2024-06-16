---
title: access_review_default_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_default_settings
  - authorization
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
<tr><td><b>Name</b></td><td><code>access_review_default_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_default_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The access review default settings id. This is only going to be default |
| <CopyableCode code="name" /> | `string` | The access review default settings name. This is always going to be Access Review Default Settings |
| <CopyableCode code="properties" /> | `object` | Settings of an Access Review. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="subscriptionId" /> |

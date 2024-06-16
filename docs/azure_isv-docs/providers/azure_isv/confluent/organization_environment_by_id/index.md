---
title: organization_environment_by_id
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_environment_by_id
  - confluent
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
<tr><td><b>Name</b></td><td><code>organization_environment_by_id</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.confluent.organization_environment_by_id" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the environment |
| <CopyableCode code="name" /> | `string` | Display name of the environment |
| <CopyableCode code="kind" /> | `string` | Type of environment |
| <CopyableCode code="properties" /> | `object` | Environment resource property |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentId, organizationName, resourceGroupName, subscriptionId" /> |

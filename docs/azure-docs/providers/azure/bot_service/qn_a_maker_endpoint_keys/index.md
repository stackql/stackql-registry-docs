---
title: qn_a_maker_endpoint_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - qn_a_maker_endpoint_keys
  - bot_service
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
<tr><td><b>Name</b></td><td><code>qn_a_maker_endpoint_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.qn_a_maker_endpoint_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="installedVersion" /> | `string` | Current version of runtime. |
| <CopyableCode code="lastStableVersion" /> | `string` | Latest version of runtime. |
| <CopyableCode code="primaryEndpointKey" /> | `string` | Primary Access Key. |
| <CopyableCode code="secondaryEndpointKey" /> | `string` | Secondary Access Key. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |

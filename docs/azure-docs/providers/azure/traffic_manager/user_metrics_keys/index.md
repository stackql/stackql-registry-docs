---
title: user_metrics_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - user_metrics_keys
  - traffic_manager
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
<tr><td><b>Name</b></td><td><code>user_metrics_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.traffic_manager.user_metrics_keys" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get the subscription-level key used for Real User Metrics collection. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="subscriptionId" /> | Create or update a subscription-level key used for Real User Metrics collection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="subscriptionId" /> | Delete a subscription-level key used for Real User Metrics collection. |

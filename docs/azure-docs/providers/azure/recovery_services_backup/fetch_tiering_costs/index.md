---
title: fetch_tiering_costs
hide_title: false
hide_table_of_contents: false
keywords:
  - fetch_tiering_costs
  - recovery_services_backup
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>fetch_tiering_costs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fetch_tiering_costs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.fetch_tiering_costs" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="post" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName, data__objectType, data__sourceTierType, data__targetTierType" /> | Provides the details of the tiering related sizes and cost.
Status of the operation can be fetched using GetTieringCostOperationStatus API and result using GetTieringCostOperationResult API. |

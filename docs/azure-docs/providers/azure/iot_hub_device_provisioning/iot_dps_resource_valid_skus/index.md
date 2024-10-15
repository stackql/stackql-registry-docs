---
title: iot_dps_resource_valid_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_dps_resource_valid_skus
  - iot_hub_device_provisioning
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

Creates, updates, deletes, gets or lists a <code>iot_dps_resource_valid_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iot_dps_resource_valid_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub_device_provisioning.iot_dps_resource_valid_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Sku name. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="provisioningServiceName, resourceGroupName, subscriptionId" /> | Gets the list of valid SKUs and tiers for a provisioning service. |

## `SELECT` examples

Gets the list of valid SKUs and tiers for a provisioning service.


```sql
SELECT
name
FROM azure.iot_hub_device_provisioning.iot_dps_resource_valid_skus
WHERE provisioningServiceName = '{{ provisioningServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
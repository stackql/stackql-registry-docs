---
title: resource_valid_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_valid_skus
  - iot_hub
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

Creates, updates, deletes, gets or lists a <code>resource_valid_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_valid_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.resource_valid_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capacity" /> | `object` | IoT Hub capacity information. |
| <CopyableCode code="resourceType" /> | `string` | The type of the resource. |
| <CopyableCode code="sku" /> | `object` | Information about the SKU of the IoT hub. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Get the list of valid SKUs for an IoT hub. |

## `SELECT` examples

Get the list of valid SKUs for an IoT hub.


```sql
SELECT
capacity,
resourceType,
sku
FROM azure.iot_hub.resource_valid_skus
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
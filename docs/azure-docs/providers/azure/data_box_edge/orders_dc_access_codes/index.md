---
title: orders_dc_access_codes
hide_title: false
hide_table_of_contents: false
keywords:
  - orders_dc_access_codes
  - data_box_edge
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

Creates, updates, deletes, gets or lists a <code>orders_dc_access_codes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>orders_dc_access_codes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.orders_dc_access_codes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | DCAccessCode Properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
properties
FROM azure.data_box_edge.orders_dc_access_codes
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
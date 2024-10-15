---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - vmware_cloud_simple
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

Creates, updates, deletes, gets or lists a <code>usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | User name model |
| <CopyableCode code="currentValue" /> | `integer` | The current usage value |
| <CopyableCode code="limit" /> | `integer` | limit of a given sku in a region for a subscription. The maximum permitted value for the usage quota. If there is no limit, this value will be -1 |
| <CopyableCode code="unit" /> | `string` | The usages' unit |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="regionId, subscriptionId" /> | Returns list of usage in region |

## `SELECT` examples

Returns list of usage in region


```sql
SELECT
name,
currentValue,
limit,
unit
FROM azure_isv.vmware_cloud_simple.usages
WHERE regionId = '{{ regionId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
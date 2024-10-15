---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - test_base
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

Creates, updates, deletes, gets or lists a <code>skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the SKU. This is typically a letter + number code, such as B0 or S0. |
| <CopyableCode code="capabilities" /> | `array` | The capabilities of a SKU. |
| <CopyableCode code="locations" /> | `array` | The locations that the SKU is available. |
| <CopyableCode code="resourceType" /> | `string` | The type of resource the SKU applies to. |
| <CopyableCode code="tier" /> | `string` | The tier of this particular SKU. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the available SKUs of Test Base Account in a subscription. |

## `SELECT` examples

Lists the available SKUs of Test Base Account in a subscription.


```sql
SELECT
name,
capabilities,
locations,
resourceType,
tier
FROM azure_extras.test_base.skus
WHERE subscriptionId = '{{ subscriptionId }}';
```
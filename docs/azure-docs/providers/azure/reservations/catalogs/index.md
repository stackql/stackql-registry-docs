---
title: catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs
  - reservations
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

Creates, updates, deletes, gets or lists a <code>catalogs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.reservations.catalogs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of sku |
| <CopyableCode code="billingPlans" /> | `object` | The billing plan options available for this sku. |
| <CopyableCode code="capabilities" /> | `array` |  |
| <CopyableCode code="locations" /> | `array` |  |
| <CopyableCode code="msrp" /> | `object` | Pricing information about the sku |
| <CopyableCode code="resourceType" /> | `string` | The type of resource the sku applies to. |
| <CopyableCode code="restrictions" /> | `array` |  |
| <CopyableCode code="size" /> | `string` | The size of this sku |
| <CopyableCode code="skuProperties" /> | `array` |  |
| <CopyableCode code="terms" /> | `array` | Available reservation terms for this resource |
| <CopyableCode code="tier" /> | `string` | The tier of this sku |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
name,
billingPlans,
capabilities,
locations,
msrp,
resourceType,
restrictions,
size,
skuProperties,
terms,
tier
FROM azure.reservations.catalogs
WHERE subscriptionId = '{{ subscriptionId }}';
```
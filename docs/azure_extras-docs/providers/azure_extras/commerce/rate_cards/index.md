---
title: rate_cards
hide_title: false
hide_table_of_contents: false
keywords:
  - rate_cards
  - commerce
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

Creates, updates, deletes, gets or lists a <code>rate_cards</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rate_cards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.commerce.rate_cards" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="Currency" /> | `string` | The currency in which the rates are provided. |
| <CopyableCode code="IsTaxIncluded" /> | `boolean` | All rates are pretax, so this will always be returned as 'false'. |
| <CopyableCode code="Locale" /> | `string` | The culture in which the resource information is localized. |
| <CopyableCode code="Meters" /> | `array` | A list of meters. |
| <CopyableCode code="OfferTerms" /> | `array` | A list of offer terms. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="$filter, subscriptionId" /> | Enables you to query for the resource/meter metadata and related prices used in a given subscription by Offer ID, Currency, Locale and Region. The metadata associated with the billing meters, including but not limited to service names, types, resources, units of measure, and regions, is subject to change at any time and without notice. If you intend to use this billing data in an automated fashion, please use the billing meter GUID to uniquely identify each billable item. If the billing meter GUID is scheduled to change due to a new billing model, you will be notified in advance of the change.  |

## `SELECT` examples

Enables you to query for the resource/meter metadata and related prices used in a given subscription by Offer ID, Currency, Locale and Region. The metadata associated with the billing meters, including but not limited to service names, types, resources, units of measure, and regions, is subject to change at any time and without notice. If you intend to use this billing data in an automated fashion, please use the billing meter GUID to uniquely identify each billable item. If the billing meter GUID is scheduled to change due to a new billing model, you will be notified in advance of the change. 


```sql
SELECT
Currency,
IsTaxIncluded,
Locale,
Meters,
OfferTerms
FROM azure_extras.commerce.rate_cards
WHERE $filter = '{{ $filter }}'
AND subscriptionId = '{{ subscriptionId }}';
```
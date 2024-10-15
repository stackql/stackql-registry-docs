---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - lab_services
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.lab_services.skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the SKU. |
| <CopyableCode code="capabilities" /> | `array` | The capabilities of the SKU. |
| <CopyableCode code="capacity" /> | `object` | The scale out/in options of the SKU. |
| <CopyableCode code="costs" /> | `array` | Metadata for retrieving price info of a lab services SKUs. |
| <CopyableCode code="family" /> | `string` | The family of the SKU. |
| <CopyableCode code="locations" /> | `array` | List of locations that are available for a size. |
| <CopyableCode code="resourceType" /> | `string` | The lab services resource type. |
| <CopyableCode code="restrictions" /> | `array` | Restrictions of a lab services SKUs. |
| <CopyableCode code="size" /> | `string` | The SKU size. |
| <CopyableCode code="tier" /> | `string` | The tier of the SKU. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns a list of Azure Lab Services resource SKUs. |

## `SELECT` examples

Returns a list of Azure Lab Services resource SKUs.


```sql
SELECT
name,
capabilities,
capacity,
costs,
family,
locations,
resourceType,
restrictions,
size,
tier
FROM azure.lab_services.skus
WHERE subscriptionId = '{{ subscriptionId }}';
```
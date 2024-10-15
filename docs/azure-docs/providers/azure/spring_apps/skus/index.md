---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - spring_apps
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Gets the name of SKU. |
| <CopyableCode code="capacity" /> | `object` | The SKU capacity |
| <CopyableCode code="locationInfo" /> | `array` | Gets a list of locations and availability zones in those locations where the SKU is available. |
| <CopyableCode code="locations" /> | `array` | Gets the set of locations that the SKU is available. |
| <CopyableCode code="resourceType" /> | `string` | Gets the type of resource the SKU applies to. |
| <CopyableCode code="restrictions" /> | `array` | Gets the restrictions because of which SKU cannot be used. This is
empty if there are no restrictions. |
| <CopyableCode code="tier" /> | `string` | Gets the tier of SKU. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the available skus of the Microsoft.AppPlatform provider. |

## `SELECT` examples

Lists all of the available skus of the Microsoft.AppPlatform provider.


```sql
SELECT
name,
capacity,
locationInfo,
locations,
resourceType,
restrictions,
tier
FROM azure.spring_apps.skus
WHERE subscriptionId = '{{ subscriptionId }}';
```
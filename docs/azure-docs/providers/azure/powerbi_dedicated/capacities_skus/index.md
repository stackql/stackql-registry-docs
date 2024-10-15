---
title: capacities_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - capacities_skus
  - powerbi_dedicated
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

Creates, updates, deletes, gets or lists a <code>capacities_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacities_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_dedicated.capacities_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the SKU level. |
| <CopyableCode code="capacity" /> | `integer` | The capacity of the SKU. |
| <CopyableCode code="tier" /> | `string` | The name of the Azure pricing tier to which the SKU applies. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists eligible SKUs for PowerBI Dedicated resource provider. |

## `SELECT` examples

Lists eligible SKUs for PowerBI Dedicated resource provider.


```sql
SELECT
name,
capacity,
tier
FROM azure.powerbi_dedicated.capacities_skus
WHERE subscriptionId = '{{ subscriptionId }}';
```
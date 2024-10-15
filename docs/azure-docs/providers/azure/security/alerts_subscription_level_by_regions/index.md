---
title: alerts_subscription_level_by_regions
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts_subscription_level_by_regions
  - security
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

Creates, updates, deletes, gets or lists a <code>alerts_subscription_level_by_regions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts_subscription_level_by_regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.alerts_subscription_level_by_regions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | describes security alert properties. |
| <CopyableCode code="type" /> | `string` | Resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="ascLocation, subscriptionId" /> | List all the alerts that are associated with the subscription that are stored in a specific location |

## `SELECT` examples

List all the alerts that are associated with the subscription that are stored in a specific location


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.alerts_subscription_level_by_regions
WHERE ascLocation = '{{ ascLocation }}'
AND subscriptionId = '{{ subscriptionId }}';
```
---
title: benefit_recommendations
hide_title: false
hide_table_of_contents: false
keywords:
  - benefit_recommendations
  - cost_management
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

Creates, updates, deletes, gets or lists a <code>benefit_recommendations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>benefit_recommendations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.benefit_recommendations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind/type of the benefit. |
| <CopyableCode code="properties" /> | `object` | The properties of the benefit recommendations. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="billingScope" /> | List of recommendations for purchasing savings plan. |

## `SELECT` examples

List of recommendations for purchasing savings plan.


```sql
SELECT
kind,
properties
FROM azure.cost_management.benefit_recommendations
WHERE billingScope = '{{ billingScope }}';
```
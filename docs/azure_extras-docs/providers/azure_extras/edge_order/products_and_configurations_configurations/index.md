---
title: products_and_configurations_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - products_and_configurations_configurations
  - edge_order
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

Creates, updates, deletes, gets or lists a <code>products_and_configurations_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>products_and_configurations_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.edge_order.products_and_configurations_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of configuration. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List configurations for the given product family, product line and product for the given subscription. |

## `SELECT` examples

List configurations for the given product family, product line and product for the given subscription.


```sql
SELECT
properties
FROM azure_extras.edge_order.products_and_configurations_configurations
WHERE subscriptionId = '{{ subscriptionId }}';
```
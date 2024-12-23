---
title: consumer_fulfillments
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - consumer_fulfillments
  - marketplace
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>consumer_fulfillments</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consumer_fulfillments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.consumer_fulfillments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="fulfillment_type" /> | `string` |
| <CopyableCode code="listing_id" /> | `string` |
| <CopyableCode code="recipient_type" /> | `string` |
| <CopyableCode code="repo_info" /> | `object` |
| <CopyableCode code="share_info" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="listing_id, deployment_name" /> | Get all listings fulfillments associated with a listing. A |

## `SELECT` examples

```sql
SELECT
fulfillment_type,
listing_id,
recipient_type,
repo_info,
share_info
FROM databricks_workspace.marketplace.consumer_fulfillments
WHERE listing_id = '{{ listing_id }}' AND
deployment_name = '{{ deployment_name }}';
```

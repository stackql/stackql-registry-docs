---
title: consumer_listing_content
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - consumer_listing_content
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

Operations on a <code>consumer_listing_content</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consumer_listing_content</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.consumer_listing_content" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="data_object_type" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="listing_id, deployment_name" /> | Get a high level preview of the metadata of listing installable content. |

## `SELECT` examples

```sql
SELECT
name,
data_object_type
FROM databricks_workspace.marketplace.consumer_listing_content
WHERE listing_id = '{{ listing_id }}' AND
deployment_name = '{{ deployment_name }}';
```

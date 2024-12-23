---
title: node_types
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - node_types
  - compute
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

Operations on a <code>node_types</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.node_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="category" /> | `string` |
| <CopyableCode code="display_order" /> | `integer` |
| <CopyableCode code="instance_type_id" /> | `string` |
| <CopyableCode code="is_deprecated" /> | `boolean` |
| <CopyableCode code="is_hidden" /> | `boolean` |
| <CopyableCode code="is_io_cache_enabled" /> | `boolean` |
| <CopyableCode code="memory_mb" /> | `integer` |
| <CopyableCode code="node_instance_type" /> | `object` |
| <CopyableCode code="node_type_id" /> | `string` |
| <CopyableCode code="num_cores" /> | `integer` |
| <CopyableCode code="num_gpus" /> | `integer` |
| <CopyableCode code="support_cluster_tags" /> | `boolean` |
| <CopyableCode code="support_ebs_volumes" /> | `boolean` |
| <CopyableCode code="support_port_forwarding" /> | `boolean` |
| <CopyableCode code="supports_elastic_disk" /> | `boolean` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listnodetypes" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Returns a list of supported Spark node types. These node types can be used to launch a cluster. |

## `SELECT` examples

```sql
SELECT
description,
category,
display_order,
instance_type_id,
is_deprecated,
is_hidden,
is_io_cache_enabled,
memory_mb,
node_instance_type,
node_type_id,
num_cores,
num_gpus,
support_cluster_tags,
support_ebs_volumes,
support_port_forwarding,
supports_elastic_disk
FROM databricks_workspace.compute.node_types
WHERE deployment_name = '{{ deployment_name }}';
```

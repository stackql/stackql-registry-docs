---
title: spark_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - spark_versions
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

Operations on a <code>spark_versions</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>spark_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.spark_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="key" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="sparkversions" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Returns the list of available Spark versions. These versions can be used to launch a cluster. |

## `SELECT` examples

```sql
SELECT
name,
key
FROM databricks_workspace.compute.spark_versions
WHERE deployment_name = '{{ deployment_name }}';
```

---
title: zones
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - zones
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

Operations on a <code>zones</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.zones" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="default_zone" /> | `string` |
| <CopyableCode code="zones" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listzones" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Returns a list of availability zones where clusters can be created in (For example, us-west-2a). These zones can be used to launch a cluster. |

## `SELECT` examples

```sql
SELECT
default_zone,
zones
FROM databricks_workspace.compute.zones
WHERE deployment_name = '{{ deployment_name }}';
```

---
title: schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - schemas
  - realtimeserving
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

Operations on a <code>schemas</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.realtimeserving.schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="info" /> | `object` |
| <CopyableCode code="openapi" /> | `string` |
| <CopyableCode code="paths" /> | `object` |
| <CopyableCode code="servers" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getopenapi" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Get the query schema of the serving endpoint in OpenAPI format. The schema contains information for the supported paths, input and output format and datatypes. |

## `SELECT` examples

```sql
SELECT
info,
openapi,
paths,
servers
FROM databricks_workspace.realtimeserving.schemas
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

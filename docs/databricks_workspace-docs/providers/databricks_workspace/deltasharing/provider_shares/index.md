---
title: provider_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - provider_shares
  - deltasharing
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

Operations on a <code>provider_shares</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.deltasharing.provider_shares" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listshares" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Gets an array of a specified provider's shares within the metastore where: |

## `SELECT` examples

```sql
SELECT
name
FROM databricks_workspace.deltasharing.provider_shares
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

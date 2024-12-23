---
title: storage_credential_validation
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - storage_credential_validation
  - unitycatalog
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

Operations on a <code>storage_credential_validation</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_credential_validation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.storage_credential_validation" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="isDir" /> | `boolean` |
| <CopyableCode code="results" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="validate" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Validates a storage credential. At least one of |

## `SELECT` examples

```sql
SELECT
isDir,
results
FROM databricks_workspace.unitycatalog.storage_credential_validation
WHERE deployment_name = '{{ deployment_name }}';
```

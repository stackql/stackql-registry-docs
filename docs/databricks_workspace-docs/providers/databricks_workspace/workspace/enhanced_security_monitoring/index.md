---
title: enhanced_security_monitoring
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - enhanced_security_monitoring
  - workspace
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

Operations on a <code>enhanced_security_monitoring</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enhanced_security_monitoring</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.enhanced_security_monitoring" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="enhanced_security_monitoring_workspace" /> | `object` |
| <CopyableCode code="etag" /> | `string` |
| <CopyableCode code="setting_name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets the enhanced security monitoring setting. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | Updates the enhanced security monitoring setting for the workspace. A fresh etag needs to be provided in |

## `SELECT` examples

```sql
SELECT
enhanced_security_monitoring_workspace,
etag,
setting_name
FROM databricks_workspace.workspace.enhanced_security_monitoring
WHERE deployment_name = '{{ deployment_name }}';
```

## `UPDATE` example

Updates a <code>enhanced_security_monitoring</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.workspace.enhanced_security_monitoring
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE deployment_name = '{{ deployment_name }}';
```

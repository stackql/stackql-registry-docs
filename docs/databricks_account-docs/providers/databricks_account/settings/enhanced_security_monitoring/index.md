---
title: enhanced_security_monitoring
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - enhanced_security_monitoring
  - settings
  - databricks_account
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_account/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>enhanced_security_monitoring</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enhanced_security_monitoring</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.enhanced_security_monitoring" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="esm_enablement_account" /> | `object` |
| <CopyableCode code="etag" /> | `string` |
| <CopyableCode code="setting_name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets the enhanced security monitoring setting for new workspaces. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="account_id" /> | Updates the value of the enhanced security monitoring setting for new workspaces. |

## `SELECT` examples

```sql
SELECT
esm_enablement_account,
etag,
setting_name
FROM databricks_account.settings.enhanced_security_monitoring
WHERE account_id = '{{ account_id }}';
```

## `UPDATE` example

Updates a <code>enhanced_security_monitoring</code> resource.

```sql
/*+ update */
UPDATE databricks_account.settings.enhanced_security_monitoring
SET { field = value }
WHERE account_id = '{{ account_id }}';
```

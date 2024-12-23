---
title: compliance_security_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - compliance_security_profile
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

Operations on a <code>compliance_security_profile</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>compliance_security_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.settings.compliance_security_profile" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="csp_enablement_account" /> | `object` |
| <CopyableCode code="etag" /> | `string` |
| <CopyableCode code="setting_name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets the compliance security profile setting for new workspaces. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="account_id" /> | Updates the value of the compliance security profile setting for new workspaces. |

## `SELECT` examples

```sql
SELECT
csp_enablement_account,
etag,
setting_name
FROM databricks_account.settings.compliance_security_profile
WHERE account_id = '{{ account_id }}';
```

## `UPDATE` example

Updates a <code>compliance_security_profile</code> resource.

```sql
/*+ update */
UPDATE databricks_account.settings.compliance_security_profile
SET { field = value }
WHERE account_id = '{{ account_id }}';
```

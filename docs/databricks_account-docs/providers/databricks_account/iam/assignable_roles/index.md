---
title: assignable_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - assignable_roles
  - iam
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

Operations on a <code>assignable_roles</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignable_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.assignable_roles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getassignablerolesforresource" /> | `SELECT` | <CopyableCode code="account_id, resource" /> | Gets all the roles that can be granted on an account level resource. A role is grantable if the rule set on the resource can contain an access rule of the role. |

## `SELECT` examples

```sql
SELECT
name
FROM databricks_account.iam.assignable_roles
WHERE account_id = '{{ account_id }}' AND
resource = '{{ resource }}';
```

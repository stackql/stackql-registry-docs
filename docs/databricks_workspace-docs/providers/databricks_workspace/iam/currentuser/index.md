---
title: currentuser
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - currentuser
  - iam
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

Operations on a <code>currentuser</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>currentuser</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.iam.currentuser" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `object` |
| <CopyableCode code="active" /> | `boolean` |
| <CopyableCode code="displayName" /> | `string` |
| <CopyableCode code="emails" /> | `array` |
| <CopyableCode code="entitlements" /> | `array` |
| <CopyableCode code="externalId" /> | `string` |
| <CopyableCode code="groups" /> | `array` |
| <CopyableCode code="roles" /> | `array` |
| <CopyableCode code="schemas" /> | `array` |
| <CopyableCode code="userName" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="me" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Get details about the current method caller's identity. |

## `SELECT` examples

```sql
SELECT
id,
name,
active,
displayName,
emails,
entitlements,
externalId,
groups,
roles,
schemas,
userName
FROM databricks_workspace.iam.currentuser
WHERE deployment_name = '{{ deployment_name }}';
```

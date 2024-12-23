---
title: user_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - user_tokens
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

Operations on a <code>user_tokens</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.user_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="creation_time" /> | `integer` |
| <CopyableCode code="expiry_time" /> | `integer` |
| <CopyableCode code="token_id" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listtokens" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Lists all the valid tokens for a user-workspace pair. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates and returns a token for a user. If this call is made through token authentication, it creates a token with the same client ID as the authenticated token. If the user's token quota is exceeded, this call returns an error |
| <CopyableCode code="revoketoken" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Revokes an access token. |

## `SELECT` examples

```sql
SELECT
comment,
creation_time,
expiry_time,
token_id
FROM databricks_workspace.workspace.user_tokens
WHERE deployment_name = '{{ deployment_name }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_tokens</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'user_tokens', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.workspace.user_tokens (
deployment_name,
data__lifetime_seconds,
data__comment
)
SELECT 
'{{ deployment_name }}',
'{{ lifetime_seconds }}',
'{{ comment }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: lifetime_seconds
    value: 0
  - name: comment
    value: string

```

</TabItem>
</Tabs>

---
title: service_principal_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - service_principal_secrets
  - oauth
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

Operations on a <code>service_principal_secrets</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_principal_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.oauth.service_principal_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="create_time" /> | `string` |
| <CopyableCode code="secret_hash" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="update_time" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id, service_principal_id" /> | List all secrets associated with the given service principal. This operation only returns information about the secrets themselves and does not include the secret values. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id, service_principal_id" /> | Create a secret for the given service principal. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, secret_id, service_principal_id" /> | Delete a secret from the given service principal. |

## `SELECT` examples

```sql
SELECT
id,
create_time,
secret_hash,
status,
update_time
FROM databricks_account.oauth.service_principal_secrets
WHERE account_id = '{{ account_id }}' AND
service_principal_id = '{{ service_principal_id }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_principal_secrets</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'service_principal_secrets', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.oauth.service_principal_secrets (
account_id,
service_principal_id
)
SELECT 
'{{ account_id }}',
'{{ service_principal_id }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []  # No request body parameters required
```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>service_principal_secrets</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.oauth.service_principal_secrets
WHERE account_id = '{{ account_id }}' AND
secret_id = '{{ secret_id }}' AND
service_principal_id = '{{ service_principal_id }}';
```

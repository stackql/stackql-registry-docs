---
title: consumer_installations
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - consumer_installations
  - marketplace
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

Operations on a <code>consumer_installations</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consumer_installations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.consumer_installations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="catalog_name" /> | `string` |
| <CopyableCode code="error_message" /> | `string` |
| <CopyableCode code="installed_on" /> | `integer` |
| <CopyableCode code="listing_id" /> | `string` |
| <CopyableCode code="listing_name" /> | `string` |
| <CopyableCode code="recipient_type" /> | `string` |
| <CopyableCode code="repo_name" /> | `string` |
| <CopyableCode code="repo_path" /> | `string` |
| <CopyableCode code="share_name" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="token_detail" /> | `object` |
| <CopyableCode code="tokens" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | List all installations across all listings. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="listing_id, deployment_name" /> | Install payload associated with a Databricks Marketplace listing. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="installation_id, listing_id, deployment_name" /> | Uninstall an installation associated with a Databricks Marketplace listing. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="installation_id, listing_id, deployment_name" /> | This is a update API that will update the part of the fields defined in the installation table as well as interact with external services according to the fields not included in the installation table |

## `SELECT` examples

```sql
SELECT
id,
catalog_name,
error_message,
installed_on,
listing_id,
listing_name,
recipient_type,
repo_name,
repo_path,
share_name,
status,
token_detail,
tokens
FROM databricks_workspace.marketplace.consumer_installations
WHERE deployment_name = '{{ deployment_name }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>consumer_installations</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'consumer_installations', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.marketplace.consumer_installations (
listing_id,
deployment_name,
data__share_name,
data__catalog_name,
data__repo_detail,
data__recipient_type,
data__accepted_consumer_terms
)
SELECT 
'{{ listing_id }}',
'{{ deployment_name }}',
'{{ share_name }}',
'{{ catalog_name }}',
'{{ repo_detail }}',
'{{ recipient_type }}',
'{{ accepted_consumer_terms }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: share_name
    value: string
  - name: catalog_name
    value: string
  - name: repo_detail
    value:
      repo_name: string
      repo_path: string
  - name: recipient_type
    value: DELTA_SHARING_RECIPIENT_TYPE_DATABRICKS
  - name: accepted_consumer_terms
    value:
      version: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>consumer_installations</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.marketplace.consumer_installations
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE installation_id = '{{ installation_id }}' AND
listing_id = '{{ listing_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>consumer_installations</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.marketplace.consumer_installations
WHERE installation_id = '{{ installation_id }}' AND
listing_id = '{{ listing_id }}' AND
deployment_name = '{{ deployment_name }}';
```

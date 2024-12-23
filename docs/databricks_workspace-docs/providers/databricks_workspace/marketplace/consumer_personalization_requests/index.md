---
title: consumer_personalization_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - consumer_personalization_requests
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

Operations on a <code>consumer_personalization_requests</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consumer_personalization_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.consumer_personalization_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="consumer_region" /> | `object` |
| <CopyableCode code="contact_info" /> | `object` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="intended_use" /> | `string` |
| <CopyableCode code="is_from_lighthouse" /> | `boolean` |
| <CopyableCode code="listing_id" /> | `string` |
| <CopyableCode code="listing_name" /> | `string` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="provider_id" /> | `string` |
| <CopyableCode code="recipient_type" /> | `string` |
| <CopyableCode code="share" /> | `object` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="status_message" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="listing_id, deployment_name" /> | Get the personalization request for a listing. Each consumer can make at |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | List personalization requests for a consumer across all listings. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="listing_id, deployment_name" /> | Create a personalization request for a listing. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'consumer_personalization_requests (list)', value: 'list' },
        { label: 'consumer_personalization_requests (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
comment,
consumer_region,
contact_info,
created_at,
intended_use,
is_from_lighthouse,
listing_id,
listing_name,
metastore_id,
provider_id,
recipient_type,
share,
status,
status_message,
updated_at
FROM databricks_workspace.marketplace.consumer_personalization_requests
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
comment,
consumer_region,
contact_info,
created_at,
intended_use,
is_from_lighthouse,
listing_id,
listing_name,
metastore_id,
provider_id,
recipient_type,
share,
status,
status_message,
updated_at
FROM databricks_workspace.marketplace.consumer_personalization_requests
WHERE listing_id = '{{ listing_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>consumer_personalization_requests</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'consumer_personalization_requests', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.marketplace.consumer_personalization_requests (
listing_id,
deployment_name,
data__comment,
data__intended_use,
data__first_name,
data__last_name,
data__company,
data__is_from_lighthouse,
data__recipient_type,
data__accepted_consumer_terms
)
SELECT 
'{{ listing_id }}',
'{{ deployment_name }}',
'{{ comment }}',
'{{ intended_use }}',
'{{ first_name }}',
'{{ last_name }}',
'{{ company }}',
'{{ is_from_lighthouse }}',
'{{ recipient_type }}',
'{{ accepted_consumer_terms }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: comment
    value: string
  - name: intended_use
    value: string
  - name: first_name
    value: string
  - name: last_name
    value: string
  - name: company
    value: string
  - name: is_from_lighthouse
    value: true
  - name: recipient_type
    value: DELTA_SHARING_RECIPIENT_TYPE_DATABRICKS
  - name: accepted_consumer_terms
    value:
      version: string

```

</TabItem>
</Tabs>

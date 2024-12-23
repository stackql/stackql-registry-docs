---
title: serving_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - serving_endpoints
  - realtimeserving
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

Operations on a <code>serving_endpoints</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serving_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.realtimeserving.serving_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="config" /> | `object` |
| <CopyableCode code="creation_timestamp" /> | `integer` |
| <CopyableCode code="creator" /> | `string` |
| <CopyableCode code="last_updated_timestamp" /> | `integer` |
| <CopyableCode code="permission_level" /> | `string` |
| <CopyableCode code="route_optimized" /> | `boolean` |
| <CopyableCode code="state" /> | `object` |
| <CopyableCode code="tags" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Retrieves the details for a single serving endpoint. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, deployment_name" /> |  |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="name, deployment_name" /> | Used to batch add and delete tags from a serving endpoint with a single API call. |
| <CopyableCode code="updateconfig" /> | `UPDATE` | <CopyableCode code="name, deployment_name" /> | Updates any combination of the serving endpoint's served entities, the compute configuration of those served entities, and the endpoint's traffic config. An endpoint that already has an update in progress can not be updated until the current update completes or fails. |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="name, deployment_name" /> | Used to update the rate limits of a serving endpoint. NOTE: Only foundation model endpoints are currently supported. For external models, use AI Gateway to manage rate limits. |
| <CopyableCode code="query" /> | `EXEC` | <CopyableCode code="name, deployment_name" /> |  |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'serving_endpoints (list)', value: 'list' },
        { label: 'serving_endpoints (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
name,
config,
creation_timestamp,
creator,
last_updated_timestamp,
permission_level,
route_optimized,
state,
tags
FROM databricks_workspace.realtimeserving.serving_endpoints
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
name,
config,
creation_timestamp,
creator,
last_updated_timestamp,
permission_level,
route_optimized,
state,
tags
FROM databricks_workspace.realtimeserving.serving_endpoints
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>serving_endpoints</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'serving_endpoints', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.realtimeserving.serving_endpoints (
deployment_name,
data__name,
data__config,
data__ai_gateway,
data__tags
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ config }}',
'{{ ai_gateway }}',
'{{ tags }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: openai_endpoint
  - name: config
    value:
      served_entities:
      - name: openai_embeddings
        external_model:
          name: text-embedding-ada-002
          provider: openai
          task: llm/v1/embeddings
          openai_config:
            openai_api_key: '{{secrets/my_scope/my_openai_api_key}}'
  - name: ai_gateway
    value:
      usage_tracking_config:
        enabled: true
      inference_table_config:
        catalog_name: my-catalog
        schema_name: my-schema
        table_name_prefix: my-prefix
        enabled: true
      rate_limits:
      - calls: 100
        key: user
        renewal_period: minute
      guardrails:
        input:
          safety: true
          pii:
            behavior: BLOCK
          valid_topics:
          - topic1
          - topic2
          invalid_keywords:
          - keyword1
          - keyword2
        output:
          safety: true
          pii:
            behavior: BLOCK
          valid_topics:
          - topic1
          - topic2
          invalid_keywords:
          - keyword1
          - keyword2
  - name: tags
    value:
    - key: team
      value: gen-ai

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>serving_endpoints</code> resource.

<Tabs
    defaultValue="patch"
    values={[
        { label: 'patch', value: 'patch' },
        { label: 'updateconfig', value: 'updateconfig' }
    ]
}>
<TabItem value="patch">
```sql
/*+ update */
UPDATE databricks_workspace.realtimeserving.serving_endpoints
SET { field = value }
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
</TabItem>
<TabItem value="updateconfig">
```sql
/*+ update */
UPDATE databricks_workspace.realtimeserving.serving_endpoints
SET { field = value }
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces a <code>serving_endpoints</code> resource.

```sql
/*+ update */
REPLACE databricks_workspace.realtimeserving.serving_endpoints
SET { field = value }
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>serving_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.realtimeserving.serving_endpoints
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

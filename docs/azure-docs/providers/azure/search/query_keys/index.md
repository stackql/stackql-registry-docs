---
title: query_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - query_keys
  - search
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>query_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>query_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search.query_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the query API key. Query names are optional, but assigning a name can help you remember how it's used. |
| <CopyableCode code="key" /> | `string` | The value of the query API key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_search_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, searchServiceName, subscriptionId" /> | Returns the list of query API keys for the given Azure AI Search service. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, searchServiceName, subscriptionId" /> | Generates a new query key for the specified search service. You can create up to 50 query keys per service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="key, resourceGroupName, searchServiceName, subscriptionId" /> | Deletes the specified query key. Unlike admin keys, query keys are not regenerated. The process for regenerating a query key is to delete and then recreate it. |

## `SELECT` examples

Returns the list of query API keys for the given Azure AI Search service.


```sql
SELECT
name,
key
FROM azure.search.query_keys
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND searchServiceName = '{{ searchServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>query_keys</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.search.query_keys (
name,
resourceGroupName,
searchServiceName,
subscriptionId
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ searchServiceName }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>query_keys</code> resource.

```sql
/*+ delete */
DELETE FROM azure.search.query_keys
WHERE key = '{{ key }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND searchServiceName = '{{ searchServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

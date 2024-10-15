---
title: sql_pool_metadata_sync_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_metadata_sync_configs
  - synapse
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

Creates, updates, deletes, gets or lists a <code>sql_pool_metadata_sync_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_metadata_sync_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_metadata_sync_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Metadata Sync Config properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get the metadata sync configuration for a SQL pool |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Set the metadata sync configuration for a SQL pool |

## `SELECT` examples

Get the metadata sync configuration for a SQL pool


```sql
SELECT
properties
FROM azure.synapse.sql_pool_metadata_sync_configs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sql_pool_metadata_sync_configs</code> resource.

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
INSERT INTO azure.synapse.sql_pool_metadata_sync_configs (
resourceGroupName,
sqlPoolName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ sqlPoolName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: enabled
          value: boolean
        - name: syncIntervalInMinutes
          value: integer

```
</TabItem>
</Tabs>

---
title: datastores
hide_title: false
hide_table_of_contents: false
keywords:
  - datastores
  - apigee
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

Creates, updates, deletes, gets or lists a <code>datastores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datastores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.datastores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="createTime" /> | `string` | Output only. Datastore create time, in milliseconds since the epoch of 1970-01-01T00:00:00Z |
| <CopyableCode code="datastoreConfig" /> | `object` | Configuration detail for datastore |
| <CopyableCode code="displayName" /> | `string` | Required. Display name in UI |
| <CopyableCode code="lastUpdateTime" /> | `string` | Output only. Datastore last update time, in milliseconds since the epoch of 1970-01-01T00:00:00Z |
| <CopyableCode code="org" /> | `string` | Output only. Organization that the datastore belongs to |
| <CopyableCode code="self" /> | `string` | Output only. Resource link of Datastore. Example: `/organizations/{org}/analytics/datastores/{uuid}` |
| <CopyableCode code="targetType" /> | `string` | Destination storage type. Supported types `gcs` or `bigquery`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_analytics_datastores_get" /> | `SELECT` | <CopyableCode code="datastoresId, organizationsId" /> | Get a Datastore |
| <CopyableCode code="organizations_analytics_datastores_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | List Datastores |
| <CopyableCode code="organizations_analytics_datastores_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Create a Datastore for an org |
| <CopyableCode code="organizations_analytics_datastores_delete" /> | `DELETE` | <CopyableCode code="datastoresId, organizationsId" /> | Delete a Datastore from an org. |
| <CopyableCode code="organizations_analytics_datastores_update" /> | `REPLACE` | <CopyableCode code="datastoresId, organizationsId" /> | Update a Datastore |
| <CopyableCode code="organizations_analytics_datastores_test" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Test if Datastore configuration is correct. This includes checking if credentials provided by customer have required permissions in target destination storage |

## `SELECT` examples

List Datastores

```sql
SELECT
createTime,
datastoreConfig,
displayName,
lastUpdateTime,
org,
self,
targetType
FROM google.apigee.datastores
WHERE organizationsId = '{{ organizationsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>datastores</code> resource.

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
INSERT INTO google.apigee.datastores (
organizationsId,
datastoreConfig,
displayName,
targetType
)
SELECT 
'{{ organizationsId }}',
'{{ datastoreConfig }}',
'{{ displayName }}',
'{{ targetType }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: datastoreConfig
      value:
        - name: path
          value: string
        - name: projectId
          value: string
        - name: bucketName
          value: string
        - name: datasetName
          value: string
        - name: tablePrefix
          value: string
    - name: displayName
      value: string
    - name: org
      value: string
    - name: lastUpdateTime
      value: string
    - name: self
      value: string
    - name: createTime
      value: string
    - name: targetType
      value: string

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>datastores</code> resource.

```sql
/*+ update */
REPLACE google.apigee.datastores
SET 
datastoreConfig = '{{ datastoreConfig }}',
displayName = '{{ displayName }}',
targetType = '{{ targetType }}'
WHERE 
datastoresId = '{{ datastoresId }}'
AND organizationsId = '{{ organizationsId }}';
```

## `DELETE` example

Deletes the specified <code>datastores</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.datastores
WHERE datastoresId = '{{ datastoresId }}'
AND organizationsId = '{{ organizationsId }}';
```

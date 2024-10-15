---
title: data_collection_rule_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - data_collection_rule_associations
  - monitor
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

Creates, updates, deletes, gets or lists a <code>data_collection_rule_associations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_collection_rule_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.data_collection_rule_associations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="etag" /> | `string` | Resource entity tag (ETag). |
| <CopyableCode code="properties" /> | `object` | Resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="associationName, resourceUri" /> |  |
| <CopyableCode code="list_by_data_collection_endpoint" /> | `SELECT` | <CopyableCode code="dataCollectionEndpointName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_resource" /> | `SELECT` | <CopyableCode code="resourceUri" /> |  |
| <CopyableCode code="list_by_rule" /> | `SELECT` | <CopyableCode code="dataCollectionRuleName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="associationName, resourceUri" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="associationName, resourceUri" /> |  |

## `SELECT` examples




```sql
SELECT
id,
name,
etag,
properties,
systemData,
type
FROM azure.monitor.data_collection_rule_associations
WHERE resourceUri = '{{ resourceUri }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_collection_rule_associations</code> resource.

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
INSERT INTO azure.monitor.data_collection_rule_associations (
associationName,
resourceUri,
properties
)
SELECT 
'{{ associationName }}',
'{{ resourceUri }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: etag
      value: string
    - name: systemData
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>data_collection_rule_associations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.monitor.data_collection_rule_associations
WHERE associationName = '{{ associationName }}'
AND resourceUri = '{{ resourceUri }}';
```

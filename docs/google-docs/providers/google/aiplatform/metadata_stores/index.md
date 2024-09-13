
---
title: metadata_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata_stores
  - aiplatform
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

Creates, updates, deletes or gets an <code>metadata_store</code> resource or lists <code>metadata_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metadata_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.metadata_stores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the MetadataStore instance. |
| <CopyableCode code="description" /> | `string` | Description of the MetadataStore. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this MetadataStore was created. |
| <CopyableCode code="dataplexConfig" /> | `object` | Represents Dataplex integration settings. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="state" /> | `object` | Represents state information for a MetadataStore. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this MetadataStore was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Retrieves a specific MetadataStore. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists MetadataStores for a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Initializes a MetadataStore, including allocation of resources. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Deletes a single MetadataStore and all its child resources (Artifacts, Executions, and Contexts). |

## `SELECT` examples

Lists MetadataStores for a Location.

```sql
SELECT
name,
description,
createTime,
dataplexConfig,
encryptionSpec,
state,
updateTime
FROM google.aiplatform.metadata_stores
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>metadata_stores</code> resource.

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
INSERT INTO google.aiplatform.metadata_stores (
locationsId,
projectsId,
dataplexConfig,
state,
name,
createTime,
description,
encryptionSpec,
updateTime
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ dataplexConfig }}',
'{{ state }}',
'{{ name }}',
'{{ createTime }}',
'{{ description }}',
'{{ encryptionSpec }}',
'{{ updateTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: dataplexConfig
        value: '{{ dataplexConfig }}'
      - name: state
        value: '{{ state }}'
      - name: name
        value: '{{ name }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: description
        value: '{{ description }}'
      - name: encryptionSpec
        value: '{{ encryptionSpec }}'
      - name: updateTime
        value: '{{ updateTime }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified metadata_store resource.

```sql
DELETE FROM google.aiplatform.metadata_stores
WHERE locationsId = '{{ locationsId }}'
AND metadataStoresId = '{{ metadataStoresId }}'
AND projectsId = '{{ projectsId }}';
```

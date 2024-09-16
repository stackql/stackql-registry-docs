---
title: user_data_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - user_data_mappings
  - healthcare
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

Creates, updates, deletes, gets or lists a <code>user_data_mappings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_data_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.user_data_mappings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name of the User data mapping, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/userDataMappings/{user_data_mapping_id}`. |
| <CopyableCode code="archiveTime" /> | `string` | Output only. Indicates the time when this mapping was archived. |
| <CopyableCode code="archived" /> | `boolean` | Output only. Indicates whether this mapping is archived. |
| <CopyableCode code="dataId" /> | `string` | Required. A unique identifier for the mapped resource. |
| <CopyableCode code="resourceAttributes" /> | `array` | Attributes of the resource. Only explicitly set attributes are displayed here. Attribute definitions with defaults set implicitly apply to these User data mappings. Attributes listed here must be single valued, that is, exactly one value is specified for the field "values" in each Attribute. |
| <CopyableCode code="userId" /> | `string` | Required. User's UUID provided by the client. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId, userDataMappingsId" /> | Gets the specified User data mapping. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId" /> | Lists the User data mappings in the specified consent store. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId" /> | Creates a new User data mapping in the parent consent store. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId, userDataMappingsId" /> | Deletes the specified User data mapping. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId, userDataMappingsId" /> | Updates the specified User data mapping. |
| <CopyableCode code="archive" /> | `EXEC` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId, userDataMappingsId" /> | Archives the specified User data mapping. |

## `SELECT` examples

Lists the User data mappings in the specified consent store.

```sql
SELECT
name,
archiveTime,
archived,
dataId,
resourceAttributes,
userId
FROM google.healthcare.user_data_mappings
WHERE consentStoresId = '{{ consentStoresId }}'
AND datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_data_mappings</code> resource.

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
INSERT INTO google.healthcare.user_data_mappings (
consentStoresId,
datasetsId,
locationsId,
projectsId,
name,
dataId,
userId,
resourceAttributes,
archived,
archiveTime
)
SELECT 
'{{ consentStoresId }}',
'{{ datasetsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ dataId }}',
'{{ userId }}',
'{{ resourceAttributes }}',
true|false,
'{{ archiveTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: dataId
      value: '{{ dataId }}'
    - name: userId
      value: '{{ userId }}'
    - name: resourceAttributes
      value: '{{ resourceAttributes }}'
    - name: archived
      value: '{{ archived }}'
    - name: archiveTime
      value: '{{ archiveTime }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>user_data_mappings</code> resource.

```sql
/*+ update */
UPDATE google.healthcare.user_data_mappings
SET 
name = '{{ name }}',
dataId = '{{ dataId }}',
userId = '{{ userId }}',
resourceAttributes = '{{ resourceAttributes }}',
archived = true|false,
archiveTime = '{{ archiveTime }}'
WHERE 
consentStoresId = '{{ consentStoresId }}'
AND datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND userDataMappingsId = '{{ userDataMappingsId }}';
```

## `DELETE` example

Deletes the specified <code>user_data_mappings</code> resource.

```sql
/*+ delete */
DELETE FROM google.healthcare.user_data_mappings
WHERE consentStoresId = '{{ consentStoresId }}'
AND datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND userDataMappingsId = '{{ userDataMappingsId }}';
```

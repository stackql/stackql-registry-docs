---
title: partitions
hide_title: false
hide_table_of_contents: false
keywords:
  - partitions
  - dataplex
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

Creates, updates, deletes, gets or lists a <code>partitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.partitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Partition values used in the HTTP URL must be double encoded. For example, url_encode(url_encode(value)) can be used to encode "US:CA/CA#Sunnyvale so that the request URL ends with "/partitions/US%253ACA/CA%2523Sunnyvale". The name field in the response retains the encoded format. |
| <CopyableCode code="etag" /> | `string` | Optional. The etag for this partition. |
| <CopyableCode code="location" /> | `string` | Required. Immutable. The location of the entity data within the partition, for example, gs://bucket/path/to/entity/key1=value1/key2=value2. Or projects//datasets//tables/ |
| <CopyableCode code="values" /> | `array` | Required. Immutable. The set of values representing the partition, which correspond to the partition schema defined in the parent entity. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_lakes_zones_entities_partitions_get" /> | `SELECT` | <CopyableCode code="entitiesId, lakesId, locationsId, partitionsId, projectsId, zonesId" /> | Get a metadata partition of an entity. |
| <CopyableCode code="projects_locations_lakes_zones_entities_partitions_list" /> | `SELECT` | <CopyableCode code="entitiesId, lakesId, locationsId, projectsId, zonesId" /> | List metadata partitions of an entity. |
| <CopyableCode code="projects_locations_lakes_zones_entities_partitions_create" /> | `INSERT` | <CopyableCode code="entitiesId, lakesId, locationsId, projectsId, zonesId" /> | Create a metadata partition. |
| <CopyableCode code="projects_locations_lakes_zones_entities_partitions_delete" /> | `DELETE` | <CopyableCode code="entitiesId, lakesId, locationsId, partitionsId, projectsId, zonesId" /> | Delete a metadata partition. |

## `SELECT` examples

List metadata partitions of an entity.

```sql
SELECT
name,
etag,
location,
values
FROM google.dataplex.partitions
WHERE entitiesId = '{{ entitiesId }}'
AND lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND zonesId = '{{ zonesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>partitions</code> resource.

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
INSERT INTO google.dataplex.partitions (
entitiesId,
lakesId,
locationsId,
projectsId,
zonesId,
name,
values,
location,
etag
)
SELECT 
'{{ entitiesId }}',
'{{ lakesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ zonesId }}',
'{{ name }}',
'{{ values }}',
'{{ location }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: values
        value: '{{ values }}'
      - name: location
        value: '{{ location }}'
      - name: etag
        value: '{{ etag }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>partitions</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataplex.partitions
WHERE entitiesId = '{{ entitiesId }}'
AND lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND partitionsId = '{{ partitionsId }}'
AND projectsId = '{{ projectsId }}'
AND zonesId = '{{ zonesId }}';
```

---
title: entities
hide_title: false
hide_table_of_contents: false
keywords:
  - entities
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

Creates, updates, deletes, gets or lists a <code>entities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.entities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Required. A user-provided entity ID. It is mutable, and will be used as the published table name. Specifying a new ID in an update entity request will override the existing value. The ID must contain only letters (a-z, A-Z), numbers (0-9), and underscores, and consist of 256 or fewer characters. |
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the entity, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/entities/{id}. |
| <CopyableCode code="description" /> | `string` | Optional. User friendly longer description text. Must be shorter than or equal to 1024 characters. |
| <CopyableCode code="access" /> | `object` | Describes the access mechanism of the data within its storage location. |
| <CopyableCode code="asset" /> | `string` | Required. Immutable. The ID of the asset associated with the storage location containing the entity data. The entity must be with in the same zone with the asset. |
| <CopyableCode code="catalogEntry" /> | `string` | Output only. The name of the associated Data Catalog entry. |
| <CopyableCode code="compatibility" /> | `object` | Provides compatibility information for various metadata stores. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the entity was created. |
| <CopyableCode code="dataPath" /> | `string` | Required. Immutable. The storage path of the entity data. For Cloud Storage data, this is the fully-qualified path to the entity, such as gs://bucket/path/to/data. For BigQuery data, this is the name of the table resource, such as projects/project_id/datasets/dataset_id/tables/table_id. |
| <CopyableCode code="dataPathPattern" /> | `string` | Optional. The set of items within the data path constituting the data in the entity, represented as a glob path. Example: gs://bucket/path/to/data/**/*.csv. |
| <CopyableCode code="displayName" /> | `string` | Optional. Display name must be shorter than or equal to 256 characters. |
| <CopyableCode code="etag" /> | `string` | Optional. The etag associated with the entity, which can be retrieved with a GetEntity request. Required for update and delete requests. |
| <CopyableCode code="format" /> | `object` | Describes the format of the data within its storage location. |
| <CopyableCode code="schema" /> | `object` | Schema information describing the structure and layout of the data. |
| <CopyableCode code="system" /> | `string` | Required. Immutable. Identifies the storage system of the entity data. |
| <CopyableCode code="type" /> | `string` | Required. Immutable. The type of entity. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated unique ID for the Entity. This ID will be different if the Entity is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the entity was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_lakes_zones_entities_get" /> | `SELECT` | <CopyableCode code="entitiesId, lakesId, locationsId, projectsId, zonesId" /> | Get a metadata entity. |
| <CopyableCode code="projects_locations_lakes_zones_entities_list" /> | `SELECT` | <CopyableCode code="lakesId, locationsId, projectsId, zonesId" /> | List metadata entities in a zone. |
| <CopyableCode code="projects_locations_lakes_zones_entities_create" /> | `INSERT` | <CopyableCode code="lakesId, locationsId, projectsId, zonesId" /> | Create a metadata entity. |
| <CopyableCode code="projects_locations_lakes_zones_entities_delete" /> | `DELETE` | <CopyableCode code="entitiesId, lakesId, locationsId, projectsId, zonesId" /> | Delete a metadata entity. |
| <CopyableCode code="projects_locations_lakes_zones_entities_update" /> | `REPLACE` | <CopyableCode code="entitiesId, lakesId, locationsId, projectsId, zonesId" /> | Update a metadata entity. Only supports full resource update. |

## `SELECT` examples

List metadata entities in a zone.

```sql
SELECT
id,
name,
description,
access,
asset,
catalogEntry,
compatibility,
createTime,
dataPath,
dataPathPattern,
displayName,
etag,
format,
schema,
system,
type,
uid,
updateTime
FROM google.dataplex.entities
WHERE lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND zonesId = '{{ zonesId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>entities</code> resource.

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
INSERT INTO google.dataplex.entities (
lakesId,
locationsId,
projectsId,
zonesId,
displayName,
description,
etag,
type,
asset,
dataPath,
dataPathPattern,
system,
format,
schema
)
SELECT 
'{{ lakesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ zonesId }}',
'{{ displayName }}',
'{{ description }}',
'{{ etag }}',
'{{ type }}',
'{{ asset }}',
'{{ dataPath }}',
'{{ dataPathPattern }}',
'{{ system }}',
'{{ format }}',
'{{ schema }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: displayName
      value: string
    - name: description
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: id
      value: string
    - name: etag
      value: string
    - name: type
      value: string
    - name: asset
      value: string
    - name: dataPath
      value: string
    - name: dataPathPattern
      value: string
    - name: catalogEntry
      value: string
    - name: system
      value: string
    - name: format
      value:
        - name: format
          value: string
        - name: compressionFormat
          value: string
        - name: mimeType
          value: string
        - name: csv
          value:
            - name: encoding
              value: string
            - name: headerRows
              value: integer
            - name: delimiter
              value: string
            - name: quote
              value: string
        - name: json
          value:
            - name: encoding
              value: string
        - name: iceberg
          value:
            - name: metadataLocation
              value: string
    - name: compatibility
      value:
        - name: hiveMetastore
          value:
            - name: compatible
              value: boolean
            - name: reason
              value: string
    - name: access
      value:
        - name: read
          value: string
    - name: uid
      value: string
    - name: schema
      value:
        - name: userManaged
          value: boolean
        - name: fields
          value:
            - - name: name
                value: string
              - name: description
                value: string
              - name: type
                value: string
              - name: mode
                value: string
              - name: fields
                value:
                  - - name: name
                      value: string
                    - name: description
                      value: string
                    - name: type
                      value: string
                    - name: mode
                      value: string
                    - name: fields
                      value:
                        - - name: name
                            value: string
                          - name: description
                            value: string
                          - name: type
                            value: string
                          - name: mode
                            value: string
                          - name: fields
                            value:
                              - - name: name
                                  value: string
                                - name: description
                                  value: string
                                - name: type
                                  value: string
                                - name: mode
                                  value: string
                                - name: fields
                                  value:
                                    - - name: name
                                        value: string
                                      - name: description
                                        value: string
                                      - name: type
                                        value: string
                                      - name: mode
                                        value: string
                                      - name: fields
                                        value:
                                          - - name: name
                                              value: string
                                            - name: description
                                              value: string
                                            - name: type
                                              value: string
                                            - name: mode
                                              value: string
                                            - name: fields
                                              value:
                                                - - name: name
                                                    value: string
                                                  - name: description
                                                    value: string
                                                  - name: type
                                                    value: string
                                                  - name: mode
                                                    value: string
                                                  - name: fields
                                                    value:
                                                      - - name: name
                                                          value: string
                                                        - name: description
                                                          value: string
                                                        - name: type
                                                          value: string
                                                        - name: mode
                                                          value: string
                                                        - name: fields
                                                          value:
                                                            - - name: name
                                                                value: string
                                                              - name: description
                                                                value: string
                                                              - name: type
                                                                value: string
                                                              - name: mode
                                                                value: string
                                                              - name: fields
                                                                value:
                                                                  - []
        - name: partitionFields
          value:
            - - name: name
                value: string
              - name: type
                value: string
        - name: partitionStyle
          value: string

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>entities</code> resource.

```sql
/*+ update */
REPLACE google.dataplex.entities
SET 
displayName = '{{ displayName }}',
description = '{{ description }}',
etag = '{{ etag }}',
type = '{{ type }}',
asset = '{{ asset }}',
dataPath = '{{ dataPath }}',
dataPathPattern = '{{ dataPathPattern }}',
system = '{{ system }}',
format = '{{ format }}',
schema = '{{ schema }}'
WHERE 
entitiesId = '{{ entitiesId }}'
AND lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND zonesId = '{{ zonesId }}';
```

## `DELETE` example

Deletes the specified <code>entities</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataplex.entities
WHERE entitiesId = '{{ entitiesId }}'
AND lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND zonesId = '{{ zonesId }}';
```

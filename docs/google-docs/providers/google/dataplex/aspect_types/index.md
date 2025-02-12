---
title: aspect_types
hide_title: false
hide_table_of_contents: false
keywords:
  - aspect_types
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

Creates, updates, deletes, gets or lists a <code>aspect_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aspect_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.aspect_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the AspectType, of the form: projects/{project_number}/locations/{location_id}/aspectTypes/{aspect_type_id}. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the AspectType. |
| <CopyableCode code="authorization" /> | `object` | Autorization for an AspectType. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the AspectType was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="etag" /> | `string` | The service computes this checksum. The client may send it on update and delete requests to ensure it has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the AspectType. |
| <CopyableCode code="metadataTemplate" /> | `object` | MetadataTemplate definition for an AspectType. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the AspectType. If you delete and recreate the AspectType with the same name, then this ID will be different. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the AspectType was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_aspect_types_get" /> | `SELECT` | <CopyableCode code="aspectTypesId, locationsId, projectsId" /> | Gets an AspectType. |
| <CopyableCode code="projects_locations_aspect_types_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists AspectType resources in a project and location. |
| <CopyableCode code="projects_locations_aspect_types_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an AspectType. |
| <CopyableCode code="projects_locations_aspect_types_delete" /> | `DELETE` | <CopyableCode code="aspectTypesId, locationsId, projectsId" /> | Deletes an AspectType. |
| <CopyableCode code="projects_locations_aspect_types_patch" /> | `UPDATE` | <CopyableCode code="aspectTypesId, locationsId, projectsId" /> | Updates an AspectType. |

## `SELECT` examples

Lists AspectType resources in a project and location.

```sql
SELECT
name,
description,
authorization,
createTime,
displayName,
etag,
labels,
metadataTemplate,
uid,
updateTime
FROM google.dataplex.aspect_types
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>aspect_types</code> resource.

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
INSERT INTO google.dataplex.aspect_types (
locationsId,
projectsId,
description,
displayName,
labels,
etag,
authorization,
metadataTemplate
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ description }}',
'{{ displayName }}',
'{{ labels }}',
'{{ etag }}',
'{{ authorization }}',
'{{ metadataTemplate }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: uid
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: description
      value: string
    - name: displayName
      value: string
    - name: labels
      value: object
    - name: etag
      value: string
    - name: authorization
      value:
        - name: alternateUsePermission
          value: string
    - name: metadataTemplate
      value:
        - name: index
          value: integer
        - name: name
          value: string
        - name: type
          value: string
        - name: recordFields
          value:
            - - name: index
                value: integer
              - name: name
                value: string
              - name: type
                value: string
              - name: recordFields
                value:
                  - - name: index
                      value: integer
                    - name: name
                      value: string
                    - name: type
                      value: string
                    - name: recordFields
                      value:
                        - - name: index
                            value: integer
                          - name: name
                            value: string
                          - name: type
                            value: string
                          - name: recordFields
                            value:
                              - - name: index
                                  value: integer
                                - name: name
                                  value: string
                                - name: type
                                  value: string
                                - name: recordFields
                                  value:
                                    - - name: index
                                        value: integer
                                      - name: name
                                        value: string
                                      - name: type
                                        value: string
                                      - name: recordFields
                                        value:
                                          - - name: index
                                              value: integer
                                            - name: name
                                              value: string
                                            - name: type
                                              value: string
                                            - name: recordFields
                                              value:
                                                - - name: index
                                                    value: integer
                                                  - name: name
                                                    value: string
                                                  - name: type
                                                    value: string
                                                  - name: recordFields
                                                    value:
                                                      - - name: index
                                                          value: integer
                                                        - name: name
                                                          value: string
                                                        - name: type
                                                          value: string
                                                        - name: recordFields
                                                          value:
                                                            - - name: index
                                                                value: integer
                                                              - name: name
                                                                value: string
                                                              - name: type
                                                                value: string
                                                              - name: recordFields
                                                                value:
                                                                  - []
                                                              - name: enumValues
                                                                value:
                                                                  - []
                                                              - name: typeId
                                                                value: string
                                                              - name: typeRef
                                                                value: string
                                                              - name: constraints
                                                                value: []
                                                              - name: annotations
                                                                value: []
                                                        - name: enumValues
                                                          value:
                                                            - - name: index
                                                                value: integer
                                                              - name: name
                                                                value: string
                                                              - name: deprecated
                                                                value: string
                                                        - name: typeId
                                                          value: string
                                                        - name: typeRef
                                                          value: string
                                                  - name: enumValues
                                                    value:
                                                      - - name: index
                                                          value: integer
                                                        - name: name
                                                          value: string
                                                        - name: deprecated
                                                          value: string
                                                  - name: typeId
                                                    value: string
                                                  - name: typeRef
                                                    value: string
                                            - name: enumValues
                                              value:
                                                - - name: index
                                                    value: integer
                                                  - name: name
                                                    value: string
                                                  - name: deprecated
                                                    value: string
                                            - name: typeId
                                              value: string
                                            - name: typeRef
                                              value: string
                                      - name: enumValues
                                        value:
                                          - - name: index
                                              value: integer
                                            - name: name
                                              value: string
                                            - name: deprecated
                                              value: string
                                      - name: typeId
                                        value: string
                                      - name: typeRef
                                        value: string
                                - name: enumValues
                                  value:
                                    - - name: index
                                        value: integer
                                      - name: name
                                        value: string
                                      - name: deprecated
                                        value: string
                                - name: typeId
                                  value: string
                                - name: typeRef
                                  value: string
                          - name: enumValues
                            value:
                              - - name: index
                                  value: integer
                                - name: name
                                  value: string
                                - name: deprecated
                                  value: string
                          - name: typeId
                            value: string
                          - name: typeRef
                            value: string
                    - name: enumValues
                      value:
                        - - name: index
                            value: integer
                          - name: name
                            value: string
                          - name: deprecated
                            value: string
                    - name: typeId
                      value: string
                    - name: typeRef
                      value: string
              - name: enumValues
                value:
                  - - name: index
                      value: integer
                    - name: name
                      value: string
                    - name: deprecated
                      value: string
              - name: typeId
                value: string
              - name: typeRef
                value: string
        - name: enumValues
          value:
            - - name: index
                value: integer
              - name: name
                value: string
              - name: deprecated
                value: string
        - name: typeId
          value: string
        - name: typeRef
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>aspect_types</code> resource.

```sql
/*+ update */
UPDATE google.dataplex.aspect_types
SET 
description = '{{ description }}',
displayName = '{{ displayName }}',
labels = '{{ labels }}',
etag = '{{ etag }}',
authorization = '{{ authorization }}',
metadataTemplate = '{{ metadataTemplate }}'
WHERE 
aspectTypesId = '{{ aspectTypesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>aspect_types</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataplex.aspect_types
WHERE aspectTypesId = '{{ aspectTypesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

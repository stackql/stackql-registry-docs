---
title: data_attribute_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - data_attribute_bindings
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

Creates, updates, deletes or gets an <code>data_attribute_binding</code> resource or lists <code>data_attribute_bindings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_attribute_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.data_attribute_bindings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the Data Attribute Binding, of the form: projects/{project_number}/locations/{location}/dataAttributeBindings/{data_attribute_binding_id} |
| <CopyableCode code="description" /> | `string` | Optional. Description of the DataAttributeBinding. |
| <CopyableCode code="attributes" /> | `array` | Optional. List of attributes to be associated with the resource, provided in the form: projects/{project}/locations/{location}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id} |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the DataAttributeBinding was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Etags must be used when calling the DeleteDataAttributeBinding and the UpdateDataAttributeBinding method. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the DataAttributeBinding. |
| <CopyableCode code="paths" /> | `array` | Optional. The list of paths for items within the associated resource (eg. columns and partitions within a table) along with attribute bindings. |
| <CopyableCode code="resource" /> | `string` | Optional. Immutable. The resource name of the resource that is associated to attributes. Presently, only entity resource is supported in the form: projects/{project}/locations/{location}/lakes/{lake}/zones/{zone}/entities/{entity_id} Must belong in the same project and region as the attribute binding, and there can only exist one active binding for a resource. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the DataAttributeBinding. This ID will be different if the DataAttributeBinding is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the DataAttributeBinding was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_data_attribute_bindings_get" /> | `SELECT` | <CopyableCode code="dataAttributeBindingsId, locationsId, projectsId" /> | Retrieves a DataAttributeBinding resource. |
| <CopyableCode code="projects_locations_data_attribute_bindings_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists DataAttributeBinding resources in a project and location. |
| <CopyableCode code="projects_locations_data_attribute_bindings_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a DataAttributeBinding resource. |
| <CopyableCode code="projects_locations_data_attribute_bindings_delete" /> | `DELETE` | <CopyableCode code="dataAttributeBindingsId, locationsId, projectsId" /> | Deletes a DataAttributeBinding resource. All attributes within the DataAttributeBinding must be deleted before the DataAttributeBinding can be deleted. |
| <CopyableCode code="projects_locations_data_attribute_bindings_patch" /> | `UPDATE` | <CopyableCode code="dataAttributeBindingsId, locationsId, projectsId" /> | Updates a DataAttributeBinding resource. |

## `SELECT` examples

Lists DataAttributeBinding resources in a project and location.

```sql
SELECT
name,
description,
attributes,
createTime,
displayName,
etag,
labels,
paths,
resource,
uid,
updateTime
FROM google.dataplex.data_attribute_bindings
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_attribute_bindings</code> resource.

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
INSERT INTO google.dataplex.data_attribute_bindings (
locationsId,
projectsId,
name,
uid,
createTime,
updateTime,
description,
displayName,
labels,
etag,
resource,
attributes,
paths
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ uid }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ description }}',
'{{ displayName }}',
'{{ labels }}',
'{{ etag }}',
'{{ resource }}',
'{{ attributes }}',
'{{ paths }}'
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
      - name: uid
        value: '{{ uid }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: description
        value: '{{ description }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: labels
        value: '{{ labels }}'
      - name: etag
        value: '{{ etag }}'
      - name: resource
        value: '{{ resource }}'
      - name: attributes
        value: '{{ attributes }}'
      - name: paths
        value: '{{ paths }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a data_attribute_binding only if the necessary resources are available.

```sql
UPDATE google.dataplex.data_attribute_bindings
SET 
name = '{{ name }}',
uid = '{{ uid }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
labels = '{{ labels }}',
etag = '{{ etag }}',
resource = '{{ resource }}',
attributes = '{{ attributes }}',
paths = '{{ paths }}'
WHERE 
dataAttributeBindingsId = '{{ dataAttributeBindingsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified data_attribute_binding resource.

```sql
DELETE FROM google.dataplex.data_attribute_bindings
WHERE dataAttributeBindingsId = '{{ dataAttributeBindingsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

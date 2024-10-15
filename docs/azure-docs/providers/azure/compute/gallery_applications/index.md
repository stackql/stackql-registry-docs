---
title: gallery_applications
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_applications
  - compute
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

Creates, updates, deletes, gets or lists a <code>gallery_applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gallery_applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.gallery_applications" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gallery_applications', value: 'view', },
        { label: 'gallery_applications', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_actions" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_of_life_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="eula" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryApplicationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="privacy_statement_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="release_note_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a gallery Application Definition. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryApplicationName, galleryName, resourceGroupName, subscriptionId" /> | Retrieves information about a gallery Application Definition. |
| <CopyableCode code="list_by_gallery" /> | `SELECT` | <CopyableCode code="galleryName, resourceGroupName, subscriptionId" /> | List gallery Application Definitions in a gallery. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="galleryApplicationName, galleryName, resourceGroupName, subscriptionId" /> | Create or update a gallery Application Definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="galleryApplicationName, galleryName, resourceGroupName, subscriptionId" /> | Delete a gallery Application. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="galleryApplicationName, galleryName, resourceGroupName, subscriptionId" /> | Update a gallery Application Definition. |

## `SELECT` examples

List gallery Application Definitions in a gallery.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gallery_applications', value: 'view', },
        { label: 'gallery_applications', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
custom_actions,
end_of_life_date,
eula,
galleryApplicationName,
galleryName,
location,
privacy_statement_uri,
release_note_uri,
resourceGroupName,
subscriptionId,
supported_os_type,
tags,
type
FROM azure.compute.vw_gallery_applications
WHERE galleryName = '{{ galleryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.compute.gallery_applications
WHERE galleryName = '{{ galleryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gallery_applications</code> resource.

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
INSERT INTO azure.compute.gallery_applications (
galleryApplicationName,
galleryName,
resourceGroupName,
subscriptionId,
properties,
location,
tags
)
SELECT 
'{{ galleryApplicationName }}',
'{{ galleryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: description
          value: string
        - name: eula
          value: string
        - name: privacyStatementUri
          value: string
        - name: releaseNoteUri
          value: string
        - name: endOfLifeDate
          value: string
        - name: supportedOSType
          value: string
        - name: customActions
          value:
            - - name: name
                value: string
              - name: script
                value: string
              - name: description
                value: string
              - name: parameters
                value:
                  - - name: name
                      value: string
                    - name: required
                      value: boolean
                    - name: type
                      value: string
                    - name: defaultValue
                      value: string
                    - name: description
                      value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>gallery_applications</code> resource.

```sql
/*+ update */
UPDATE azure.compute.gallery_applications
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
galleryApplicationName = '{{ galleryApplicationName }}'
AND galleryName = '{{ galleryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>gallery_applications</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.gallery_applications
WHERE galleryApplicationName = '{{ galleryApplicationName }}'
AND galleryName = '{{ galleryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

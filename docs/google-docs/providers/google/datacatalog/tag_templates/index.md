---
title: tag_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_templates
  - datacatalog
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

Creates, updates, deletes, gets or lists a <code>tag_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datacatalog.tag_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the tag template in URL format. Note: The tag template itself and its child resources might not be stored in the location specified in its name. |
| <CopyableCode code="dataplexTransferStatus" /> | `string` | Optional. Transfer status of the TagTemplate |
| <CopyableCode code="displayName" /> | `string` | Display name for this template. Defaults to an empty string. The name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), and can't start or end with spaces. The maximum length is 200 characters. |
| <CopyableCode code="fields" /> | `object` | Required. Map of tag template field IDs to the settings for the field. This map is an exhaustive list of the allowed fields. The map must contain at least one field and at most 500 fields. The keys to this map are tag template field IDs. The IDs have the following limitations: * Can contain uppercase and lowercase letters, numbers (0-9) and underscores (_). * Must be at least 1 character and at most 64 characters long. * Must start with a letter or underscore. |
| <CopyableCode code="isPubliclyReadable" /> | `boolean` | Indicates whether tags created with this template are public. Public tags do not require tag template access to appear in ListTags API response. Additionally, you can search for a public tag by value with a simple search query in addition to using a ``tag:`` predicate. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_tag_templates_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, tagTemplatesId" /> | Gets a tag template. |
| <CopyableCode code="projects_locations_tag_templates_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a tag template. You must enable the Data Catalog API in the project identified by the `parent` parameter. For more information, see [Data Catalog resource project] (https://cloud.google.com/data-catalog/docs/concepts/resource-project). |
| <CopyableCode code="projects_locations_tag_templates_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, tagTemplatesId" /> | Deletes a tag template and all tags that use it. You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |
| <CopyableCode code="projects_locations_tag_templates_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, tagTemplatesId" /> | Updates a tag template. You can't update template fields with this method. These fields are separate resources with their own create, update, and delete methods. You must enable the Data Catalog API in the project identified by the `tag_template.name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |

## `SELECT` examples

Gets a tag template.

```sql
SELECT
name,
dataplexTransferStatus,
displayName,
fields,
isPubliclyReadable
FROM google.datacatalog.tag_templates
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tagTemplatesId = '{{ tagTemplatesId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tag_templates</code> resource.

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
INSERT INTO google.datacatalog.tag_templates (
locationsId,
projectsId,
name,
displayName,
isPubliclyReadable,
fields,
dataplexTransferStatus
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
{{ isPubliclyReadable }},
'{{ fields }}',
'{{ dataplexTransferStatus }}'
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
    - name: isPubliclyReadable
      value: boolean
    - name: fields
      value: object
    - name: dataplexTransferStatus
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tag_templates</code> resource.

```sql
/*+ update */
UPDATE google.datacatalog.tag_templates
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
isPubliclyReadable = true|false,
fields = '{{ fields }}',
dataplexTransferStatus = '{{ dataplexTransferStatus }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tagTemplatesId = '{{ tagTemplatesId }}';
```

## `DELETE` example

Deletes the specified <code>tag_templates</code> resource.

```sql
/*+ delete */
DELETE FROM google.datacatalog.tag_templates
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tagTemplatesId = '{{ tagTemplatesId }}';
```

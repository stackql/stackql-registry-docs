---
title: taxonomies
hide_title: false
hide_table_of_contents: false
keywords:
  - taxonomies
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

Creates, updates, deletes, gets or lists a <code>taxonomies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>taxonomies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datacatalog.taxonomies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name of this taxonomy in URL format. Note: Policy tag manager generates unique taxonomy IDs. |
| <CopyableCode code="description" /> | `string` | Optional. Description of this taxonomy. If not set, defaults to empty. The description must contain only Unicode characters, tabs, newlines, carriage returns, and page breaks, and be at most 2000 bytes long when encoded in UTF-8. |
| <CopyableCode code="activatedPolicyTypes" /> | `array` | Optional. A list of policy types that are activated for this taxonomy. If not set, defaults to an empty list. |
| <CopyableCode code="displayName" /> | `string` | Required. User-defined name of this taxonomy. The name can't start or end with spaces, must contain only Unicode letters, numbers, underscores, dashes, and spaces, and be at most 200 bytes long when encoded in UTF-8. The taxonomy display name must be unique within an organization. |
| <CopyableCode code="policyTagCount" /> | `integer` | Output only. Number of policy tags in this taxonomy. |
| <CopyableCode code="service" /> | `object` | The source system of the Taxonomy. |
| <CopyableCode code="taxonomyTimestamps" /> | `object` | Timestamps associated with this resource in a particular system. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_taxonomies_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, taxonomiesId" /> | Gets a taxonomy. |
| <CopyableCode code="projects_locations_taxonomies_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all taxonomies in a project in a particular location that you have a permission to view. |
| <CopyableCode code="projects_locations_taxonomies_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a taxonomy in a specified project. The taxonomy is initially empty, that is, it doesn't contain policy tags. |
| <CopyableCode code="projects_locations_taxonomies_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, taxonomiesId" /> | Deletes a taxonomy, including all policy tags in this taxonomy, their associated policies, and the policy tags references from BigQuery columns. |
| <CopyableCode code="projects_locations_taxonomies_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, taxonomiesId" /> | Updates a taxonomy, including its display name, description, and activated policy types. |
| <CopyableCode code="projects_locations_taxonomies_replace" /> | `REPLACE` | <CopyableCode code="locationsId, projectsId, taxonomiesId" /> | Replaces (updates) a taxonomy and all its policy tags. The taxonomy and its entire hierarchy of policy tags must be represented literally by `SerializedTaxonomy` and the nested `SerializedPolicyTag` messages. This operation automatically does the following: - Deletes the existing policy tags that are missing from the `SerializedPolicyTag`. - Creates policy tags that don't have resource names. They are considered new. - Updates policy tags with valid resources names accordingly. |
| <CopyableCode code="projects_locations_taxonomies_export" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Exports taxonomies in the requested type and returns them, including their policy tags. The requested taxonomies must belong to the same project. This method generates `SerializedTaxonomy` protocol buffers with nested policy tags that can be used as input for `ImportTaxonomies` calls. |
| <CopyableCode code="projects_locations_taxonomies_import" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Creates new taxonomies (including their policy tags) in a given project by importing from inlined or cross-regional sources. For a cross-regional source, new taxonomies are created by copying from a source in another region. For an inlined source, taxonomies and policy tags are created in bulk using nested protocol buffer structures. |

## `SELECT` examples

Lists all taxonomies in a project in a particular location that you have a permission to view.

```sql
SELECT
name,
description,
activatedPolicyTypes,
displayName,
policyTagCount,
service,
taxonomyTimestamps
FROM google.datacatalog.taxonomies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>taxonomies</code> resource.

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
INSERT INTO google.datacatalog.taxonomies (
locationsId,
projectsId,
name,
displayName,
description,
activatedPolicyTypes
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ activatedPolicyTypes }}'
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
    - name: policyTagCount
      value: integer
    - name: taxonomyTimestamps
      value:
        - name: createTime
          value: string
        - name: updateTime
          value: string
        - name: expireTime
          value: string
    - name: activatedPolicyTypes
      value:
        - string
    - name: service
      value:
        - name: name
          value: string
        - name: identity
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>taxonomies</code> resource.

```sql
/*+ update */
UPDATE google.datacatalog.taxonomies
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
activatedPolicyTypes = '{{ activatedPolicyTypes }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND taxonomiesId = '{{ taxonomiesId }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>taxonomies</code> resource.

```sql
/*+ update */
REPLACE google.datacatalog.taxonomies
SET 
serializedTaxonomy = '{{ serializedTaxonomy }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND taxonomiesId = '{{ taxonomiesId }}';
```

## `DELETE` example

Deletes the specified <code>taxonomies</code> resource.

```sql
/*+ delete */
DELETE FROM google.datacatalog.taxonomies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND taxonomiesId = '{{ taxonomiesId }}';
```

---
title: policy_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_tags
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

Creates, updates, deletes, gets or lists a <code>policy_tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datacatalog.policy_tags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name of this policy tag in the URL format. The policy tag manager generates unique taxonomy IDs and policy tag IDs. |
| <CopyableCode code="description" /> | `string` | Description of this policy tag. If not set, defaults to empty. The description must contain only Unicode characters, tabs, newlines, carriage returns and page breaks, and be at most 2000 bytes long when encoded in UTF-8. |
| <CopyableCode code="childPolicyTags" /> | `array` | Output only. Resource names of child policy tags of this policy tag. |
| <CopyableCode code="displayName" /> | `string` | Required. User-defined name of this policy tag. The name can't start or end with spaces and must be unique within the parent taxonomy, contain only Unicode letters, numbers, underscores, dashes and spaces, and be at most 200 bytes long when encoded in UTF-8. |
| <CopyableCode code="parentPolicyTag" /> | `string` | Resource name of this policy tag's parent policy tag. If empty, this is a top level tag. If not set, defaults to an empty string. For example, for the "LatLong" policy tag in the example above, this field contains the resource name of the "Geolocation" policy tag, and, for "Geolocation", this field is empty. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_taxonomies_policy_tags_get" /> | `SELECT` | <CopyableCode code="locationsId, policyTagsId, projectsId, taxonomiesId" /> | Gets a policy tag. |
| <CopyableCode code="projects_locations_taxonomies_policy_tags_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, taxonomiesId" /> | Lists all policy tags in a taxonomy. |
| <CopyableCode code="projects_locations_taxonomies_policy_tags_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, taxonomiesId" /> | Creates a policy tag in a taxonomy. |
| <CopyableCode code="projects_locations_taxonomies_policy_tags_delete" /> | `DELETE` | <CopyableCode code="locationsId, policyTagsId, projectsId, taxonomiesId" /> | Deletes a policy tag together with the following: * All of its descendant policy tags, if any * Policies associated with the policy tag and its descendants * References from BigQuery table schema of the policy tag and its descendants |
| <CopyableCode code="projects_locations_taxonomies_policy_tags_patch" /> | `UPDATE` | <CopyableCode code="locationsId, policyTagsId, projectsId, taxonomiesId" /> | Updates a policy tag, including its display name, description, and parent policy tag. |

## `SELECT` examples

Lists all policy tags in a taxonomy.

```sql
SELECT
name,
description,
childPolicyTags,
displayName,
parentPolicyTag
FROM google.datacatalog.policy_tags
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND taxonomiesId = '{{ taxonomiesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policy_tags</code> resource.

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
INSERT INTO google.datacatalog.policy_tags (
locationsId,
projectsId,
taxonomiesId,
name,
displayName,
description,
parentPolicyTag
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ taxonomiesId }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ parentPolicyTag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
displayName: string
description: string
parentPolicyTag: string
childPolicyTags:
  - type: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>policy_tags</code> resource.

```sql
/*+ update */
UPDATE google.datacatalog.policy_tags
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
parentPolicyTag = '{{ parentPolicyTag }}'
WHERE 
locationsId = '{{ locationsId }}'
AND policyTagsId = '{{ policyTagsId }}'
AND projectsId = '{{ projectsId }}'
AND taxonomiesId = '{{ taxonomiesId }}';
```

## `DELETE` example

Deletes the specified <code>policy_tags</code> resource.

```sql
/*+ delete */
DELETE FROM google.datacatalog.policy_tags
WHERE locationsId = '{{ locationsId }}'
AND policyTagsId = '{{ policyTagsId }}'
AND projectsId = '{{ projectsId }}'
AND taxonomiesId = '{{ taxonomiesId }}';
```

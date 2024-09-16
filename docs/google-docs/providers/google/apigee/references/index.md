---
title: references
hide_title: false
hide_table_of_contents: false
keywords:
  - references
  - apigee
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

Creates, updates, deletes, gets or lists a <code>references</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>references</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.references" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource id of this reference. Values must match the regular expression [\w\s\-.]+. |
| <CopyableCode code="description" /> | `string` | Optional. A human-readable description of this reference. |
| <CopyableCode code="refers" /> | `string` | Required. The id of the resource to which this reference refers. Must be the id of a resource that exists in the parent environment and is of the given resource_type. |
| <CopyableCode code="resourceType" /> | `string` | The type of resource referred to by this reference. Valid values are 'KeyStore' or 'TrustStore'. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_references_get" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId, referencesId" /> | Gets a Reference resource. |
| <CopyableCode code="organizations_environments_references_create" /> | `INSERT` | <CopyableCode code="environmentsId, organizationsId" /> | Creates a Reference in the specified environment. |
| <CopyableCode code="organizations_environments_references_delete" /> | `DELETE` | <CopyableCode code="environmentsId, organizationsId, referencesId" /> | Deletes a Reference from an environment. Returns the deleted Reference resource. |
| <CopyableCode code="organizations_environments_references_update" /> | `REPLACE` | <CopyableCode code="environmentsId, organizationsId, referencesId" /> | Updates an existing Reference. Note that this operation has PUT semantics; it will replace the entirety of the existing Reference with the resource in the request body. |

## `SELECT` examples

Gets a Reference resource.

```sql
SELECT
name,
description,
refers,
resourceType
FROM google.apigee.references
WHERE environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}'
AND referencesId = '{{ referencesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>references</code> resource.

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
INSERT INTO google.apigee.references (
environmentsId,
organizationsId,
name,
resourceType,
description,
refers
)
SELECT 
'{{ environmentsId }}',
'{{ organizationsId }}',
'{{ name }}',
'{{ resourceType }}',
'{{ description }}',
'{{ refers }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: resourceType
      value: '{{ resourceType }}'
    - name: description
      value: '{{ description }}'
    - name: refers
      value: '{{ refers }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Replaces all fields in the specified <code>references</code> resource.

```sql
/*+ update */
REPLACE google.apigee.references
SET 
name = '{{ name }}',
resourceType = '{{ resourceType }}',
description = '{{ description }}',
refers = '{{ refers }}'
WHERE 
environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}'
AND referencesId = '{{ referencesId }}';
```

## `DELETE` example

Deletes the specified <code>references</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.references
WHERE environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}'
AND referencesId = '{{ referencesId }}';
```

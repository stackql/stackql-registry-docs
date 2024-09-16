---
title: attribute_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - attribute_definitions
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

Creates, updates, deletes, gets or lists a <code>attribute_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attribute_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.healthcare.attribute_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name of the Attribute definition, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/attributeDefinitions/{attribute_definition_id}`. Cannot be changed after creation. |
| <CopyableCode code="description" /> | `string` | Optional. A description of the attribute. |
| <CopyableCode code="allowedValues" /> | `array` | Required. Possible values for the attribute. The number of allowed values must not exceed 500. An empty list is invalid. The list can only be expanded after creation. |
| <CopyableCode code="category" /> | `string` | Required. The category of the attribute. The value of this field cannot be changed after creation. |
| <CopyableCode code="consentDefaultValues" /> | `array` | Optional. Default values of the attribute in Consents. If no default values are specified, it defaults to an empty value. |
| <CopyableCode code="dataMappingDefaultValue" /> | `string` | Optional. Default value of the attribute in User data mappings. If no default value is specified, it defaults to an empty value. This field is only applicable to attributes of the category `RESOURCE`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="attributeDefinitionsId, consentStoresId, datasetsId, locationsId, projectsId" /> | Gets the specified Attribute definition. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId" /> | Lists the Attribute definitions in the specified consent store. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="consentStoresId, datasetsId, locationsId, projectsId" /> | Creates a new Attribute definition in the parent consent store. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="attributeDefinitionsId, consentStoresId, datasetsId, locationsId, projectsId" /> | Deletes the specified Attribute definition. Fails if the Attribute definition is referenced by any User data mapping, or the latest revision of any Consent. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="attributeDefinitionsId, consentStoresId, datasetsId, locationsId, projectsId" /> | Updates the specified Attribute definition. |

## `SELECT` examples

Lists the Attribute definitions in the specified consent store.

```sql
SELECT
name,
description,
allowedValues,
category,
consentDefaultValues,
dataMappingDefaultValue
FROM google.healthcare.attribute_definitions
WHERE consentStoresId = '{{ consentStoresId }}'
AND datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>attribute_definitions</code> resource.

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
INSERT INTO google.healthcare.attribute_definitions (
consentStoresId,
datasetsId,
locationsId,
projectsId,
name,
description,
category,
allowedValues,
consentDefaultValues,
dataMappingDefaultValue
)
SELECT 
'{{ consentStoresId }}',
'{{ datasetsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ category }}',
'{{ allowedValues }}',
'{{ consentDefaultValues }}',
'{{ dataMappingDefaultValue }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: category
      value: '{{ category }}'
    - name: allowedValues
      value: '{{ allowedValues }}'
    - name: consentDefaultValues
      value: '{{ consentDefaultValues }}'
    - name: dataMappingDefaultValue
      value: '{{ dataMappingDefaultValue }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>attribute_definitions</code> resource.

```sql
/*+ update */
UPDATE google.healthcare.attribute_definitions
SET 
name = '{{ name }}',
description = '{{ description }}',
category = '{{ category }}',
allowedValues = '{{ allowedValues }}',
consentDefaultValues = '{{ consentDefaultValues }}',
dataMappingDefaultValue = '{{ dataMappingDefaultValue }}'
WHERE 
attributeDefinitionsId = '{{ attributeDefinitionsId }}'
AND consentStoresId = '{{ consentStoresId }}'
AND datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>attribute_definitions</code> resource.

```sql
/*+ delete */
DELETE FROM google.healthcare.attribute_definitions
WHERE attributeDefinitionsId = '{{ attributeDefinitionsId }}'
AND consentStoresId = '{{ consentStoresId }}'
AND datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

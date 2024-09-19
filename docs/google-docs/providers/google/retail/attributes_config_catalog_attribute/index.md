---
title: attributes_config_catalog_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - attributes_config_catalog_attribute
  - retail
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

Creates, updates, deletes, gets or lists a <code>attributes_config_catalog_attribute</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attributes_config_catalog_attribute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.retail.attributes_config_catalog_attribute" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_catalogs_attributes_config_add_catalog_attribute" /> | `INSERT` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Adds the specified CatalogAttribute to the AttributesConfig. If the CatalogAttribute to add already exists, an ALREADY_EXISTS error is returned. |
| <CopyableCode code="projects_locations_catalogs_attributes_config_remove_catalog_attribute" /> | `DELETE` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Removes the specified CatalogAttribute from the AttributesConfig. If the CatalogAttribute to remove does not exist, a NOT_FOUND error is returned. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>attributes_config_catalog_attribute</code> resource.

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
INSERT INTO google.retail.attributes_config_catalog_attribute (
catalogsId,
locationsId,
projectsId,
catalogAttribute
)
SELECT 
'{{ catalogsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ catalogAttribute }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: catalogAttribute
      value:
        - name: key
          value: string
        - name: inUse
          value: boolean
        - name: type
          value: string
        - name: indexableOption
          value: string
        - name: dynamicFacetableOption
          value: string
        - name: searchableOption
          value: string
        - name: exactSearchableOption
          value: string
        - name: retrievableOption
          value: string
        - name: facetConfig
          value:
            - name: facetIntervals
              value:
                - - name: minimum
                    value: number
                  - name: exclusiveMinimum
                    value: number
                  - name: maximum
                    value: number
                  - name: exclusiveMaximum
                    value: number
            - name: ignoredFacetValues
              value:
                - - name: values
                    value:
                      - string
                  - name: startTime
                    value: string
                  - name: endTime
                    value: string
            - name: mergedFacetValues
              value:
                - - name: values
                    value:
                      - string
                  - name: mergedValue
                    value: string
            - name: mergedFacet
              value:
                - name: mergedFacetKey
                  value: string
            - name: rerankConfig
              value:
                - name: rerankFacet
                  value: boolean
                - name: facetValues
                  value:
                    - string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>attributes_config_catalog_attribute</code> resource.

```sql
/*+ delete */
DELETE FROM google.retail.attributes_config_catalog_attribute
WHERE catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

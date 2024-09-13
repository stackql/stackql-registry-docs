---
title: catalogs_attributes_config
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs_attributes_config
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

Creates, updates, deletes, gets or lists a <code>catalogs_attributes_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>catalogs_attributes_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.retail.catalogs_attributes_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Immutable. The fully qualified resource name of the attribute config. Format: `projects/*/locations/*/catalogs/*/attributesConfig` |
| <CopyableCode code="attributeConfigLevel" /> | `string` | Output only. The AttributeConfigLevel used for this catalog. |
| <CopyableCode code="catalogAttributes" /> | `object` | Enable attribute(s) config at catalog level. For example, indexable, dynamic_facetable, or searchable for each attribute. The key is catalog attribute's name. For example: `color`, `brands`, `attributes.custom_attribute`, such as `attributes.xyz`. The maximum number of catalog attributes allowed in a request is 1000. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_catalogs_get_attributes_config" /> | `SELECT` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Gets an AttributesConfig. |
| <CopyableCode code="projects_locations_catalogs_update_attributes_config" /> | `UPDATE` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Updates the AttributesConfig. The catalog attributes in the request will be updated in the catalog, or inserted if they do not exist. Existing catalog attributes not included in the request will remain unchanged. Attributes that are assigned to products, but do not exist at the catalog level, are always included in the response. The product attribute is assigned default values for missing catalog attribute fields, e.g., searchable and dynamic facetable options. |

## `SELECT` examples

Gets an AttributesConfig.

```sql
SELECT
name,
attributeConfigLevel,
catalogAttributes
FROM google.retail.catalogs_attributes_config
WHERE catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a <code>catalogs_attributes_config</code> resource.

```sql
/*+ update */
UPDATE google.retail.catalogs_attributes_config
SET 
name = '{{ name }}',
catalogAttributes = '{{ catalogAttributes }}',
attributeConfigLevel = '{{ attributeConfigLevel }}'
WHERE 
catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

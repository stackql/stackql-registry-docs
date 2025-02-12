---
title: attributes_config
hide_title: false
hide_table_of_contents: false
keywords:
  - attributes_config
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

Creates, updates, deletes, gets or lists a <code>attributes_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attributes_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.retail.attributes_config" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_catalogs_attributes_config_replace_catalog_attribute" /> | `REPLACE` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Replaces the specified CatalogAttribute in the AttributesConfig by updating the catalog attribute with the same CatalogAttribute.key. If the CatalogAttribute to replace does not exist, a NOT_FOUND error is returned. |

## `REPLACE` example

Replaces all fields in the specified <code>attributes_config</code> resource.

```sql
/*+ update */
REPLACE google.retail.attributes_config
SET 
catalogAttribute = '{{ catalogAttribute }}',
updateMask = '{{ updateMask }}'
WHERE 
catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

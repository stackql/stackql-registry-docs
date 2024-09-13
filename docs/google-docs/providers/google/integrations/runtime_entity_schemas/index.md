
---
title: runtime_entity_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - runtime_entity_schemas
  - integrations
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

Creates, updates, deletes or gets an <code>runtime_entity_schema</code> resource or lists <code>runtime_entity_schemas</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runtime_entity_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.runtime_entity_schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="arrayFieldSchema" /> | `string` | The above schema, but for an array of the associated entity. |
| <CopyableCode code="entity" /> | `string` | Name of the entity. |
| <CopyableCode code="fieldSchema" /> | `string` | List of fields in the entity. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_connections_runtime_entity_schemas_list" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Lists the JSON schemas for the properties of runtime entities, filtered by entity name. |

## `SELECT` examples

Lists the JSON schemas for the properties of runtime entities, filtered by entity name.

```sql
SELECT
arrayFieldSchema,
entity,
fieldSchema
FROM google.integrations.runtime_entity_schemas
WHERE connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

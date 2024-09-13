---
title: entities_entities_with_conditions
hide_title: false
hide_table_of_contents: false
keywords:
  - entities_entities_with_conditions
  - connectors
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

Creates, updates, deletes, gets or lists a <code>entities_entities_with_conditions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entities_entities_with_conditions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.connectors.entities_entities_with_conditions" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete_entities_with_conditions" /> | `DELETE` | <CopyableCode code="connectionsId, entityTypesId, locationsId, projectsId" /> | Deletes entities based on conditions specified in the request and not on entity id. |
| <CopyableCode code="update_entities_with_conditions" /> | `UPDATE` | <CopyableCode code="connectionsId, entityTypesId, locationsId, projectsId" /> | Updates entities based on conditions specified in the request and not on entity id. |

## `UPDATE` example

Updates a <code>entities_entities_with_conditions</code> resource.

```sql
/*+ update */
UPDATE google.connectors.entities_entities_with_conditions
SET 
name = '{{ name }}',
fields = '{{ fields }}'
WHERE 
connectionsId = '{{ connectionsId }}'
AND entityTypesId = '{{ entityTypesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>entities_entities_with_conditions</code> resource.

```sql
/*+ delete */
DELETE FROM google.connectors.entities_entities_with_conditions
WHERE connectionsId = '{{ connectionsId }}'
AND entityTypesId = '{{ entityTypesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

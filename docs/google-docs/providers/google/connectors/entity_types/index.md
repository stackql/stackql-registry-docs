---
title: entity_types
hide_title: false
hide_table_of_contents: false
keywords:
  - entity_types
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entity_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.connectors.entity_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the entity type. |
| <CopyableCode code="fields" /> | `array` | List containing metadata information about each field of the entity type. |
| <CopyableCode code="jsonSchema" /> | `object` | JsonSchema representation of schema metadata |
| <CopyableCode code="operations" /> | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionsId, entityTypesId, locationsId, projectsId" /> | Gets metadata of given entity type |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Lists metadata related to all entity types present in the external system. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Lists metadata related to all entity types present in the external system. |

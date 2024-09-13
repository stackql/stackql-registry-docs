---
title: connections_connection_schema_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - connections_connection_schema_metadata
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

Creates, updates, deletes, gets or lists a <code>connections_connection_schema_metadata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections_connection_schema_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.connections_connection_schema_metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actions" /> | `array` | List of actions. |
| <CopyableCode code="entities" /> | `array` | List of entity names. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_connections_get_connection_schema_metadata" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Lists the available entities and actions associated with a Connection. |

## `SELECT` examples

Lists the available entities and actions associated with a Connection.

```sql
SELECT
actions,
entities
FROM google.integrations.connections_connection_schema_metadata
WHERE connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - dlp
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

Creates, updates, deletes or gets an <code>connection</code> resource or lists <code>connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dlp.connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the connection: `projects/{project}/locations/{location}/connections/{name}`. |
| <CopyableCode code="cloudSql" /> | `object` | Cloud SQL connection properties. |
| <CopyableCode code="errors" /> | `array` | Output only. Set if status == ERROR, to provide additional details. Will store the last 10 errors sorted with the most recent first. |
| <CopyableCode code="state" /> | `string` | Required. The connection's state in its lifecycle. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_connections_get" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, organizationsId" /> | Get a Connection by name. |
| <CopyableCode code="organizations_locations_connections_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists Connections in a parent. Use SearchConnections to see all connections within an organization. |
| <CopyableCode code="projects_locations_connections_get" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Get a Connection by name. |
| <CopyableCode code="projects_locations_connections_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Connections in a parent. Use SearchConnections to see all connections within an organization. |
| <CopyableCode code="organizations_locations_connections_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Create a Connection to an external data source. |
| <CopyableCode code="projects_locations_connections_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a Connection to an external data source. |
| <CopyableCode code="organizations_locations_connections_delete" /> | `DELETE` | <CopyableCode code="connectionsId, locationsId, organizationsId" /> | Delete a Connection. |
| <CopyableCode code="projects_locations_connections_delete" /> | `DELETE` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Delete a Connection. |
| <CopyableCode code="organizations_locations_connections_patch" /> | `UPDATE` | <CopyableCode code="connectionsId, locationsId, organizationsId" /> | Update a Connection. |
| <CopyableCode code="projects_locations_connections_patch" /> | `UPDATE` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Update a Connection. |
| <CopyableCode code="organizations_locations_connections_search" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Searches for Connections in a parent. |
| <CopyableCode code="projects_locations_connections_search" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Searches for Connections in a parent. |

## `SELECT` examples

Lists Connections in a parent. Use SearchConnections to see all connections within an organization.

```sql
SELECT
name,
cloudSql,
errors,
state
FROM google.dlp.connections
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connections</code> resource.

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
INSERT INTO google.dlp.connections (
locationsId,
projectsId,
connection
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ connection }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: connection
        value: '{{ connection }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a connection only if the necessary resources are available.

```sql
UPDATE google.dlp.connections
SET 
updateMask = '{{ updateMask }}',
connection = '{{ connection }}'
WHERE 
connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified connection resource.

```sql
DELETE FROM google.dlp.connections
WHERE connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

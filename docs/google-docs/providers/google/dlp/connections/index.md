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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="dlp.connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the connection: `projects/&#123;project&#125;/locations/&#123;location&#125;/connections/&#123;name&#125;`. |
| <CopyableCode code="cloudSql" /> | `object` | Cloud SQL connection properties. |
| <CopyableCode code="errors" /> | `array` | Output only. Set if status == ERROR, to provide additional details. Will store the last 10 errors sorted with the most recent first. |
| <CopyableCode code="state" /> | `string` | Required. The connection's state in its lifecycle. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_connections_get" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Get a Connection by name. |
| <CopyableCode code="projects_locations_connections_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Connections in a parent. |
| <CopyableCode code="projects_locations_connections_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a Connection to an external data source. |
| <CopyableCode code="projects_locations_connections_delete" /> | `DELETE` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Delete a Connection. |
| <CopyableCode code="_projects_locations_connections_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists Connections in a parent. |
| <CopyableCode code="organizations_locations_connections_search" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Searches for Connections in a parent. |
| <CopyableCode code="projects_locations_connections_patch" /> | `EXEC` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Update a Connection. |
| <CopyableCode code="projects_locations_connections_search" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Searches for Connections in a parent. |

---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - bigqueryconnection
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigqueryconnection.connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the connection in the form of: `projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/connections/&#123;connection_id&#125;` |
| <CopyableCode code="description" /> | `string` | User provided description. |
| <CopyableCode code="cloudSql" /> | `object` | Connection properties specific to the Cloud SQL. |
| <CopyableCode code="creationTime" /> | `string` | Output only. The creation timestamp of the connection. |
| <CopyableCode code="friendlyName" /> | `string` | User provided display name for the connection. |
| <CopyableCode code="hasCredential" /> | `boolean` | Output only. True, if credential is configured for this connection. |
| <CopyableCode code="lastModifiedTime" /> | `string` | Output only. The last update timestamp of the connection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Returns specified connection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns a list of connections in the given project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new connection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Deletes connection and associated credential. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Returns a list of connections in the given project. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask. |

---
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
  - datastream
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
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datastream.routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource's name. |
| <CopyableCode code="createTime" /> | `string` | Output only. The create time of the resource. |
| <CopyableCode code="destinationAddress" /> | `string` | Required. Destination address for connection |
| <CopyableCode code="destinationPort" /> | `integer` | Destination port for connection |
| <CopyableCode code="displayName" /> | `string` | Required. Display name. |
| <CopyableCode code="labels" /> | `object` | Labels. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The update time of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, privateConnectionsId, projectsId, routesId" /> | Use this method to get details about a route. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, privateConnectionsId, projectsId" /> | Use this method to list routes created for a private connectivity configuration in a project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, privateConnectionsId, projectsId" /> | Use this method to create a route for a private connectivity configuration in a project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, privateConnectionsId, projectsId, routesId" /> | Use this method to delete a route. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, privateConnectionsId, projectsId" /> | Use this method to list routes created for a private connectivity configuration in a project and location. |

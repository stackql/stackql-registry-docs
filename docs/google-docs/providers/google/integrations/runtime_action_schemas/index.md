---
title: runtime_action_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - runtime_action_schemas
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runtime_action_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.runtime_action_schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="action" /> | `string` | Name of the action. |
| <CopyableCode code="inputSchema" /> | `string` | Input parameter schema for the action. |
| <CopyableCode code="outputSchema" /> | `string` | Output parameter schema for the action. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_locations_connections_runtime_action_schemas_list" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> |
| <CopyableCode code="_projects_locations_connections_runtime_action_schemas_list" /> | `EXEC` | <CopyableCode code="connectionsId, locationsId, projectsId" /> |

---
title: debugsessions
hide_title: false
hide_table_of_contents: false
keywords:
  - debugsessions
  - apigee
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
<tr><td><b>Name</b></td><td><code>debugsessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigee.debugsessions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The debug session ID. |
| <CopyableCode code="timestampMs" /> | `string` | The first transaction creation timestamp in millisecond, recorded by UAP. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_apis_revisions_debugsessions_get" /> | `SELECT` | <CopyableCode code="apisId, debugsessionsId, environmentsId, organizationsId, revisionsId" /> | Retrieves a debug session. |
| <CopyableCode code="organizations_environments_apis_revisions_debugsessions_list" /> | `SELECT` | <CopyableCode code="apisId, environmentsId, organizationsId, revisionsId" /> | Lists debug sessions that are currently active in the given API Proxy revision. |
| <CopyableCode code="organizations_environments_apis_revisions_debugsessions_create" /> | `INSERT` | <CopyableCode code="apisId, environmentsId, organizationsId, revisionsId" /> | Creates a debug session for a deployed API Proxy revision. |
| <CopyableCode code="_organizations_environments_apis_revisions_debugsessions_list" /> | `EXEC` | <CopyableCode code="apisId, environmentsId, organizationsId, revisionsId" /> | Lists debug sessions that are currently active in the given API Proxy revision. |

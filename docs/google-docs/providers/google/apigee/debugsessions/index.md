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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>debugsessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.debugsessions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The debug session ID. |
| `timestampMs` | `string` | The first transaction creation timestamp in millisecond, recorded by UAP. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_environments_apis_revisions_debugsessions_get` | `SELECT` | `apisId, debugsessionsId, environmentsId, organizationsId, revisionsId` | Retrieves a debug session. |
| `organizations_environments_apis_revisions_debugsessions_list` | `SELECT` | `apisId, environmentsId, organizationsId, revisionsId` | Lists debug sessions that are currently active in the given API Proxy revision. |
| `organizations_environments_apis_revisions_debugsessions_create` | `INSERT` | `apisId, environmentsId, organizationsId, revisionsId` | Creates a debug session for a deployed API Proxy revision. |
| `_organizations_environments_apis_revisions_debugsessions_list` | `EXEC` | `apisId, environmentsId, organizationsId, revisionsId` | Lists debug sessions that are currently active in the given API Proxy revision. |

---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - sql
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.sql.connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The user provided name of the resource, unique within this environment. |
| <CopyableCode code="_spec" /> | `object` |  |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="spec" /> | `object` | Encapsulates the model provider access details |
| <CopyableCode code="status" /> | `object` | The status of the Connection |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_sqlv1connection" /> | `SELECT` | <CopyableCode code="connection_name, environment_id, organization_id" /> | [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to read a Connection. |
| <CopyableCode code="list_sqlv1connections" /> | `SELECT` | <CopyableCode code="environment_id, organization_id" /> | [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Retrieve a sorted, filtered and paginated list of all Connections. |
| <CopyableCode code="create_sqlv1connection" /> | `INSERT` | <CopyableCode code="environment_id, organization_id" /> | [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to create a Connection. |
| <CopyableCode code="delete_sqlv1connection" /> | `DELETE` | <CopyableCode code="connection_name, environment_id, organization_id" /> | [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to delete a statement. |
| <CopyableCode code="update_sqlv1connection" /> | `EXEC` | <CopyableCode code="connection_name, environment_id, organization_id" /> | [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to update a connection. |

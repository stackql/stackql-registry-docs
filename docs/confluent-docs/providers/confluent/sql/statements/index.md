---
title: statements
hide_title: false
hide_table_of_contents: false
keywords:
  - statements
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
<tr><td><b>Name</b></td><td><code>statements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.sql.statements" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The user provided name of the resource, unique within this environment. |
| <CopyableCode code="_spec" /> | `object` |  |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="environment_id" /> | `string` | The unique identifier for the environment. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | The metadata of the statement. |
| <CopyableCode code="organization_id" /> | `string` | The unique identifier for the organization. |
| <CopyableCode code="result" /> | `object` | `Statement Result` represents a resource used to model results of SQL statements.<br />The API allows you to read your SQL statement result. |
| <CopyableCode code="spec" /> | `object` | The specs of the Statement |
| <CopyableCode code="status" /> | `object` | The status of the Statement |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_sqlv1statement" /> | `SELECT` | <CopyableCode code="environment_id, organization_id, statement_name" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to read a statement. |
| <CopyableCode code="list_sqlv1statements" /> | `SELECT` | <CopyableCode code="environment_id, organization_id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Retrieve a sorted, filtered, paginated list of all statements. |
| <CopyableCode code="create_sqlv1statement" /> | `INSERT` | <CopyableCode code="environment_id, organization_id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to create a statement. |
| <CopyableCode code="delete_sqlv1statement" /> | `DELETE` | <CopyableCode code="environment_id, organization_id, statement_name" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to delete a statement. |
| <CopyableCode code="patch_sqlv1statement" /> | `UPDATE` | <CopyableCode code="environment_id, organization_id, statement_name" /> | [![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to patch a statement. |
| <CopyableCode code="update_sqlv1statement" /> | `EXEC` | <CopyableCode code="environment_id, organization_id, statement_name" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to update a statement.<br />The request will fail with a 409 Conflict error if the Statement has changed since it was fetched.<br />In this case, do a GET, reapply the modifications, and try the update again. |

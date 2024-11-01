---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - iam
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.iam.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="auth_type" /> | `string` | The user's authentication method |
| <CopyableCode code="email" /> | `string` | The user's email address |
| <CopyableCode code="full_name" /> | `string` | The user's full name |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_iam_v2user" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to read a user. |
| <CopyableCode code="list_iam_v2users" /> | `SELECT` |  | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Retrieve a sorted, filtered, paginated list of all users. |
| <CopyableCode code="delete_iam_v2user" /> | `DELETE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to delete a user.<br /><br />If successful, this request will also recursively delete all of the user's associated resources,<br />including its cloud and cluster API keys.<br /> |
| <CopyableCode code="update_iam_v2user" /> | `UPDATE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to update a user.<br /><br /> |

---
title: audit_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - audit_logs
  - audit_logs
  - openai
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage openai resources using SQL
custom_edit_url: null
image: /img/providers/openai/stackql-openai-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>audit_logs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>audit_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.audit_logs.audit_logs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of this log. |
| <CopyableCode code="actor" /> | `object` | The actor who performed the audit logged action. |
| <CopyableCode code="api_key.created" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="api_key.deleted" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="api_key.updated" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="effective_at" /> | `integer` | The Unix timestamp (in seconds) of the event. |
| <CopyableCode code="invite.accepted" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="invite.deleted" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="invite.sent" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="login.failed" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="logout.failed" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="organization.updated" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="project" /> | `object` | The project that the action was scoped to. Absent for actions not scoped to projects. |
| <CopyableCode code="project.archived" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="project.created" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="project.updated" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="service_account.created" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="service_account.deleted" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="service_account.updated" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="type" /> | `string` | The event type. |
| <CopyableCode code="user.added" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="user.deleted" /> | `object` | The details for events with this `type`. |
| <CopyableCode code="user.updated" /> | `object` | The details for events with this `type`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_audit_logs" /> | `SELECT` | <CopyableCode code="" /> |  |

## `SELECT` examples




```sql
SELECT
id,
actor,
api_key.created,
api_key.deleted,
api_key.updated,
effective_at,
invite.accepted,
invite.deleted,
invite.sent,
login.failed,
logout.failed,
organization.updated,
project,
project.archived,
project.created,
project.updated,
service_account.created,
service_account.deleted,
service_account.updated,
type,
user.added,
user.deleted,
user.updated
FROM openai.audit_logs.audit_logs
;
```
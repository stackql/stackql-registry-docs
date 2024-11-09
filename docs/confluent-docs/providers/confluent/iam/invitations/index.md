---
title: invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - invitations
  - iam
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>invitations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.iam.invitations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="accepted_at" /> | `string` | The timestamp that the invitation was accepted |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="auth_type" /> | `string` | The user/invitee's authentication type. Note that only the [OrganizationAdmin role](https://docs.confluent.io/cloud/current/access-management/access-control/cloud-rbac.html#organizationadmin)
can invite AUTH_TYPE_LOCAL users to SSO organizations.
The user's auth_type is set as AUTH_TYPE_SSO by default if the organization has SSO enabled.
Otherwise, the user's auth_type is AUTH_TYPE_LOCAL by default. |
| <CopyableCode code="creator" /> | `object` | The invitation creator |
| <CopyableCode code="email" /> | `string` | The user/invitee's email address |
| <CopyableCode code="expires_at" /> | `string` | The timestamp that the invitation will expire |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="status" /> | `string` | The status of invitations |
| <CopyableCode code="user" /> | `object` | The user/invitee |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_iam_v2invitation" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Make a request to read an invitation. |
| <CopyableCode code="list_iam_v2invitations" /> | `SELECT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Retrieve a sorted, filtered, paginated list of all invitations. |
| <CopyableCode code="create_iam_v2invitation" /> | `INSERT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Make a request to create an invitation.

The newly invited user will not have any permissions. Give the user permission by assigning them to one or
more roles by creating
[role bindings](https://docs.confluent.io/cloud/current/api.html#tag/Role-Bindings-(iamv2))
for the created `user`. |
| <CopyableCode code="delete_iam_v2invitation" /> | `DELETE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Make a request to delete an invitation.

Delete will deactivate the user if the user didn't accept the invitation yet. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Retrieve a sorted, filtered, paginated list of all invitations.


```sql
SELECT
id,
accepted_at,
api_version,
auth_type,
creator,
email,
expires_at,
kind,
metadata,
status,
user
FROM confluent.iam.invitations
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>invitations</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO confluent.iam.invitations (
data__email
)
SELECT 
'{{ email }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: invitations
  props:
    - name: email
      value: string
    - name: auth_type
      value: string
    - name: user
      props:
        - name: id
          value: string
    - name: creator
      props:
        - name: id
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>invitations</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.iam.invitations
WHERE id = '{{ id }}';
```

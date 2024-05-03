---
title: object_access_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - object_access_controls
  - storage
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
<tr><td><b>Name</b></td><td><code>object_access_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storage.object_access_controls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the access-control entry. |
| <CopyableCode code="bucket" /> | `string` | The name of the bucket. |
| <CopyableCode code="domain" /> | `string` | The domain associated with the entity, if any. |
| <CopyableCode code="email" /> | `string` | The email address associated with the entity, if any. |
| <CopyableCode code="entity" /> | `string` | The entity holding the permission, in one of the following forms: <br />- user-userId <br />- user-email <br />- group-groupId <br />- group-email <br />- domain-domain <br />- project-team-projectId <br />- allUsers <br />- allAuthenticatedUsers Examples: <br />- The user liz@example.com would be user-liz@example.com. <br />- The group example@googlegroups.com would be group-example@googlegroups.com. <br />- To refer to all members of the Google Apps for Business domain example.com, the entity would be domain-example.com. |
| <CopyableCode code="entityId" /> | `string` | The ID for the entity, if any. |
| <CopyableCode code="etag" /> | `string` | HTTP 1.1 Entity tag for the access-control entry. |
| <CopyableCode code="generation" /> | `string` | The content generation of the object, if applied to an object. |
| <CopyableCode code="kind" /> | `string` | The kind of item this is. For object access control entries, this is always storage#objectAccessControl. |
| <CopyableCode code="object" /> | `string` | The name of the object, if applied to an object. |
| <CopyableCode code="projectTeam" /> | `object` | The project team associated with the entity, if any. |
| <CopyableCode code="role" /> | `string` | The access permission for the entity. |
| <CopyableCode code="selfLink" /> | `string` | The link to this access-control entry. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bucket, entity, object" /> | Returns the ACL entry for the specified entity on the specified object. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="bucket, object" /> | Retrieves ACL entries on the specified object. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="bucket, object" /> | Creates a new ACL entry on the specified object. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bucket, entity, object" /> | Permanently deletes the ACL entry for the specified entity on the specified object. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="bucket, entity, object" /> | Patches an ACL entry on the specified object. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="bucket, entity, object" /> | Updates an ACL entry on the specified object. |

---
title: bucket_access_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_access_controls
  - storage
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bucket_access_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.storage.bucket_access_controls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the access-control entry. |
| `email` | `string` | The email address associated with the entity, if any. |
| `bucket` | `string` | The name of the bucket. |
| `entityId` | `string` | The ID for the entity, if any. |
| `selfLink` | `string` | The link to this access-control entry. |
| `entity` | `string` | The entity holding the permission, in one of the following forms: <br />- user-userId <br />- user-email <br />- group-groupId <br />- group-email <br />- domain-domain <br />- project-team-projectId <br />- allUsers <br />- allAuthenticatedUsers Examples: <br />- The user liz@example.com would be user-liz@example.com. <br />- The group example@googlegroups.com would be group-example@googlegroups.com. <br />- To refer to all members of the Google Apps for Business domain example.com, the entity would be domain-example.com. |
| `etag` | `string` | HTTP 1.1 Entity tag for the access-control entry. |
| `kind` | `string` | The kind of item this is. For bucket access control entries, this is always storage#bucketAccessControl. |
| `projectTeam` | `object` | The project team associated with the entity, if any. |
| `role` | `string` | The access permission for the entity. |
| `domain` | `string` | The domain associated with the entity, if any. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bucketAccessControls_get` | `SELECT` | `bucket, entity` | Returns the ACL entry for the specified entity on the specified bucket. |
| `bucketAccessControls_list` | `SELECT` | `bucket` | Retrieves ACL entries on the specified bucket. |
| `bucketAccessControls_insert` | `INSERT` | `bucket` | Creates a new ACL entry on the specified bucket. |
| `bucketAccessControls_delete` | `DELETE` | `bucket, entity` | Permanently deletes the ACL entry for the specified entity on the specified bucket. |
| `bucketAccessControls_patch` | `EXEC` | `bucket, entity` | Patches an ACL entry on the specified bucket. |
| `bucketAccessControls_update` | `EXEC` | `bucket, entity` | Updates an ACL entry on the specified bucket. |

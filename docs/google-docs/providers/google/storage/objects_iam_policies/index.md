---
title: objects_iam_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - objects_iam_policies
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
<tr><td><b>Name</b></td><td><code>objects_iam_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storage.objects_iam_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="condition" /> | `object` | Represents an expression text. Example: title: "User account presence" description: "Determines whether the request has a user account" expression: "size(request.user) &gt; 0" |
| <CopyableCode code="members" /> | `array` | A collection of identifiers for members who may assume the provided role. Recognized identifiers are as follows:  <br />- allUsers — A special identifier that represents anyone on the internet; with or without a Google account.  <br />- allAuthenticatedUsers — A special identifier that represents anyone who is authenticated with a Google account or a service account.  <br />- user:emailid — An email address that represents a specific account. For example, user:alice@gmail.com or user:joe@example.com.  <br />- serviceAccount:emailid — An email address that represents a service account. For example,  serviceAccount:my-other-app@appspot.gserviceaccount.com .  <br />- group:emailid — An email address that represents a Google group. For example, group:admins@example.com.  <br />- domain:domain — A Google Apps domain name that represents all the users of that domain. For example, domain:google.com or domain:example.com.  <br />- projectOwner:projectid — Owners of the given project. For example, projectOwner:my-example-project  <br />- projectEditor:projectid — Editors of the given project. For example, projectEditor:my-example-project  <br />- projectViewer:projectid — Viewers of the given project. For example, projectViewer:my-example-project |
| <CopyableCode code="role" /> | `string` | The role to which members belong. Two types of roles are supported: new IAM roles, which grant permissions that do not map directly to those provided by ACLs, and legacy IAM roles, which do map directly to ACL permissions. All roles are of the format roles/storage.specificRole.<br />The new IAM roles are:  <br />- roles/storage.admin — Full control of Google Cloud Storage resources.  <br />- roles/storage.objectViewer — Read-Only access to Google Cloud Storage objects.  <br />- roles/storage.objectCreator — Access to create objects in Google Cloud Storage.  <br />- roles/storage.objectAdmin — Full control of Google Cloud Storage objects.   The legacy IAM roles are:  <br />- roles/storage.legacyObjectReader — Read-only access to objects without listing. Equivalent to an ACL entry on an object with the READER role.  <br />- roles/storage.legacyObjectOwner — Read/write access to existing objects without listing. Equivalent to an ACL entry on an object with the OWNER role.  <br />- roles/storage.legacyBucketReader — Read access to buckets with object listing. Equivalent to an ACL entry on a bucket with the READER role.  <br />- roles/storage.legacyBucketWriter — Read access to buckets with object listing/creation/deletion. Equivalent to an ACL entry on a bucket with the WRITER role.  <br />- roles/storage.legacyBucketOwner — Read and write access to existing buckets with object listing/creation/deletion. Equivalent to an ACL entry on a bucket with the OWNER role. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_iam_policy" /> | `SELECT` | <CopyableCode code="bucket, object" /> | Returns an IAM policy for the specified object. |
| <CopyableCode code="_get_iam_policy" /> | `EXEC` | <CopyableCode code="bucket, object" /> | Returns an IAM policy for the specified object. |
| <CopyableCode code="set_iam_policy" /> | `EXEC` | <CopyableCode code="bucket, object" /> | Updates an IAM policy for the specified object. |
| <CopyableCode code="test_iam_permissions" /> | `EXEC` | <CopyableCode code="bucket, object, permissions" /> | Tests a set of permissions on the given object to see which, if any, are held by the caller. |

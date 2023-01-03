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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>objects_iam_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.storage.objects_iam_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | The kind of item this is. For policies, this is always storage#policy. This field is ignored on input. |
| `resourceId` | `string` | The ID of the resource to which this policy belongs. Will be of the form projects/_/buckets/bucket for buckets, and projects/_/buckets/bucket/objects/object for objects. A specific generation may be specified by appending #generationNumber to the end of the object name, e.g. projects/_/buckets/my-bucket/objects/data.txt#17. The current generation can be denoted with #0. This field is ignored on input. |
| `version` | `integer` | The IAM policy format version. |
| `bindings` | `array` | An association between a role, which comes with a set of permissions, and members who may assume that role. |
| `etag` | `string` | HTTP 1.1  Entity tag for the policy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `objects_getIamPolicy` | `SELECT` | `bucket, object` | Returns an IAM policy for the specified object. |
| `objects_setIamPolicy` | `EXEC` | `bucket, object` | Updates an IAM policy for the specified object. |
| `objects_testIamPermissions` | `EXEC` | `bucket, object, permissions` | Tests a set of permissions on the given object to see which, if any, are held by the caller. |

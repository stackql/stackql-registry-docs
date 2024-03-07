---
title: work_group
hide_title: false
hide_table_of_contents: false
keywords:
  - work_group
  - athena
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>work_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>work_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>work_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.athena.work_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The workGroup name.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The workgroup description.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>One or more tags, separated by commas, that you want to attach to the workgroup as you create it</td></tr>
<tr><td><code>work_group_configuration</code></td><td><code>object</code></td><td>The workgroup configuration</td></tr>
<tr><td><code>work_group_configuration_updates</code></td><td><code>object</code></td><td>The workgroup configuration update object</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>The date and time the workgroup was created.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of the workgroup: ENABLED or DISABLED.</td></tr>
<tr><td><code>recursive_delete_option</code></td><td><code>boolean</code></td><td>The option to delete the workgroup and its contents even if the workgroup contains any named queries.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>work_group</code> resource, the following permissions are required:

### Read
<pre>
athena:GetWorkGroup,
athena:ListTagsForResource</pre>

### Delete
<pre>
athena:DeleteWorkGroup,
athena:GetWorkGroup,
athena:UntagResource</pre>

### Update
<pre>
athena:UpdateWorkGroup,
athena:TagResource,
athena:UntagResource,
iam:PassRole,
s3:GetBucketLocation,
s3:GetObject,
s3:ListBucket,
s3:ListBucketMultipartUploads,
s3:AbortMultipartUpload,
s3:PutObject,
s3:ListMultipartUploadParts,
kms:Decrypt,
kms:GenerateDataKey</pre>


## Example
```sql
SELECT
region,
name,
description,
tags,
work_group_configuration,
work_group_configuration_updates,
creation_time,
state,
recursive_delete_option
FROM awscc.athena.work_group
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Name&gt;'
```

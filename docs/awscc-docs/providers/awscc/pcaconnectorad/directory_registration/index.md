---
title: directory_registration
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_registration
  - pcaconnectorad
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>directory_registration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directory_registration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>directory_registration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.pcaconnectorad.directory_registration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>directory_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>directory_registration_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>directory_registration</code> resource, the following permissions are required:

### Read
<pre>
pca-connector-ad:ListTagsForResource,
pca-connector-ad:GetDirectoryRegistration</pre>

### Delete
<pre>
pca-connector-ad:GetDirectoryRegistration,
pca-connector-ad:DeleteDirectoryRegistration,
ds:DescribeDirectories,
ds:UnauthorizeApplication,
ds:UpdateAuthorizedApplication</pre>

### Update
<pre>
pca-connector-ad:ListTagsForResource,
pca-connector-ad:TagResource,
pca-connector-ad:UntagResource</pre>


## Example
```sql
SELECT
region,
directory_id,
directory_registration_arn,
tags
FROM awscc.pcaconnectorad.directory_registration
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DirectoryRegistrationArn&gt;'
```

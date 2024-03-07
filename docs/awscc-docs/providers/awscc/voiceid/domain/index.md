---
title: domain
hide_title: false
hide_table_of_contents: false
keywords:
  - domain
  - voiceid
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>domain</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>domain</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.voiceid.domain</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>server_side_encryption_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>domain</code> resource, the following permissions are required:

### Read
<pre>
voiceid:DescribeDomain,
voiceid:ListTagsForResource,
kms:Decrypt</pre>

### Update
<pre>
voiceid:DescribeDomain,
voiceid:UpdateDomain,
voiceid:TagResource,
voiceid:UntagResource,
voiceid:ListTagsForResource,
kms:CreateGrant,
kms:Decrypt,
kms:DescribeKey</pre>

### Delete
<pre>
voiceid:DeleteDomain,
voiceid:DescribeDomain,
kms:Decrypt</pre>


## Example
```sql
SELECT
region,
description,
domain_id,
name,
server_side_encryption_configuration,
tags
FROM awscc.voiceid.domain
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DomainId&gt;'
```

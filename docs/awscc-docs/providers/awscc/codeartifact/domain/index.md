---
title: domain
hide_title: false
hide_table_of_contents: false
keywords:
  - domain
  - codeartifact
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
<tr><td><b>Id</b></td><td><code>awscc.codeartifact.domain</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>The name of the domain.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the domain. This field is used for GetAtt</td></tr>
<tr><td><code>owner</code></td><td><code>string</code></td><td>The 12-digit account ID of the AWS account that owns the domain. This field is used for GetAtt</td></tr>
<tr><td><code>encryption_key</code></td><td><code>string</code></td><td>The ARN of an AWS Key Management Service (AWS KMS) key associated with a domain.</td></tr>
<tr><td><code>permissions_policy_document</code></td><td><code>object</code></td><td>The access control resource policy on the provided domain.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the domain.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>domain</code> resource, the following permissions are required:

### Read
<pre>
codeartifact:DescribeDomain,
codeartifact:GetDomainPermissionsPolicy,
codeartifact:ListTagsForResource</pre>

### Update
<pre>
codeartifact:PutDomainPermissionsPolicy,
codeartifact:DeleteDomainPermissionsPolicy,
codeartifact:GetDomainPermissionsPolicy,
codeartifact:TagResource,
codeartifact:UntagResource</pre>

### Delete
<pre>
codeartifact:DeleteDomain,
codeartifact:DescribeDomain</pre>


## Example
```sql
SELECT
region,
domain_name,
name,
owner,
encryption_key,
permissions_policy_document,
tags,
arn
FROM awscc.codeartifact.domain
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```

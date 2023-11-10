---
title: repository
hide_title: false
hide_table_of_contents: false
keywords:
  - repository
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
Gets an individual <code>repository</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>repository</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codeartifact.repository</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>repository_name</code></td><td><code>string</code></td><td>The name of the repository.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the repository. This is used for GetAtt</td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>The name of the domain that contains the repository.</td></tr>
<tr><td><code>domain_owner</code></td><td><code>string</code></td><td>The 12-digit account ID of the AWS account that owns the domain.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A text description of the repository.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the repository.</td></tr>
<tr><td><code>external_connections</code></td><td><code>array</code></td><td>A list of external connections associated with the repository.</td></tr>
<tr><td><code>upstreams</code></td><td><code>array</code></td><td>A list of upstream repositories associated with the repository.</td></tr>
<tr><td><code>permissions_policy_document</code></td><td><code>object</code></td><td>The access control resource policy on the provided repository.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
repository_name,
name,
domain_name,
domain_owner,
description,
arn,
external_connections,
upstreams,
permissions_policy_document,
tags
FROM aws.codeartifact.repository
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```

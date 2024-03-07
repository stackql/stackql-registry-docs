---
title: access_entry
hide_title: false
hide_table_of_contents: false
keywords:
  - access_entry
  - eks
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>access_entry</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_entry</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>access_entry</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.eks.access_entry</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster_name</code></td><td><code>string</code></td><td>The cluster that the access entry is created for.</td></tr>
<tr><td><code>principal_arn</code></td><td><code>string</code></td><td>The principal ARN that the access entry is created for.</td></tr>
<tr><td><code>username</code></td><td><code>string</code></td><td>The Kubernetes user that the access entry is associated with.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>access_entry_arn</code></td><td><code>string</code></td><td>The ARN of the access entry.</td></tr>
<tr><td><code>kubernetes_groups</code></td><td><code>array</code></td><td>The Kubernetes groups that the access entry is associated with.</td></tr>
<tr><td><code>access_policies</code></td><td><code>array</code></td><td>An array of access policies that are associated with the access entry.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The node type to associate with the access entry.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>access_entry</code> resource, the following permissions are required:

### Read
<pre>
eks:DescribeAccessEntry,
eks:ListAssociatedAccessPolicies</pre>

### Update
<pre>
eks:DescribeAccessEntry,
eks:ListAssociatedAccessPolicies,
eks:UpdateAccessEntry,
eks:AssociateAccessPolicy,
eks:DisassociateAccessPolicy,
eks:TagResource,
eks:UntagResource</pre>

### Delete
<pre>
eks:DeleteAccessEntry,
eks:DescribeAccessEntry</pre>


## Example
```sql
SELECT
region,
cluster_name,
principal_arn,
username,
tags,
access_entry_arn,
kubernetes_groups,
access_policies,
type
FROM awscc.eks.access_entry
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;PrincipalArn&gt;'
AND data__Identifier = '&lt;ClusterName&gt;'
```

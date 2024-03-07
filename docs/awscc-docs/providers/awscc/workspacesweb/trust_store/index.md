---
title: trust_store
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_store
  - workspacesweb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>trust_store</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_store</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>trust_store</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.workspacesweb.trust_store</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>associated_portal_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>certificate_list</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>trust_store_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>trust_store</code> resource, the following permissions are required:

### Read
<pre>
workspaces-web:GetTrustStore,
workspaces-web:GetTrustStoreCertificate,
workspaces-web:ListTagsForResource,
workspaces-web:ListTrustStoreCertificates</pre>

### Update
<pre>
workspaces-web:UpdateTrustStore,
workspaces-web:TagResource,
workspaces-web:UntagResource,
workspaces-web:GetTrustStore,
workspaces-web:GetTrustStoreCertificate,
workspaces-web:ListTagsForResource,
workspaces-web:ListTrustStoreCertificates</pre>

### Delete
<pre>
workspaces-web:GetTrustStore,
workspaces-web:GetTrustStoreCertificate,
workspaces-web:DeleteTrustStore</pre>


## Example
```sql
SELECT
region,
associated_portal_arns,
certificate_list,
tags,
trust_store_arn
FROM awscc.workspacesweb.trust_store
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;TrustStoreArn&gt;'
```

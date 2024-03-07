---
title: trust_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_stores
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
Retrieves a list of <code>trust_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>trust_stores</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.workspacesweb.trust_stores</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>trust_store_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>trust_stores</code> resource, the following permissions are required:

### Create
<pre>
workspaces-web:CreateTrustStore,
workspaces-web:GetTrustStore,
workspaces-web:GetTrustStoreCertificate,
workspaces-web:ListTrustStoreCertificates,
workspaces-web:ListTagsForResource,
workspaces-web:TagResource</pre>

### List
<pre>
workspaces-web:ListTrustStores,
workspaces-web:ListTrustStoreCertificates</pre>


## Example
```sql
SELECT
region,
trust_store_arn
FROM awscc.workspacesweb.trust_stores
WHERE region = 'us-east-1'
```

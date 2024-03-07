---
title: domain
hide_title: false
hide_table_of_contents: false
keywords:
  - domain
  - datazone
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
<tr><td><b>Id</b></td><td><code>awscc.datazone.domain</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the Amazon DataZone domain.</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The timestamp of when the Amazon DataZone domain was last updated.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the Amazon DataZone domain.</td></tr>
<tr><td><code>domain_execution_role</code></td><td><code>string</code></td><td>The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the AWS account that houses the Amazon DataZone domain.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The id of the Amazon DataZone domain.</td></tr>
<tr><td><code>kms_key_identifier</code></td><td><code>string</code></td><td>The identifier of the AWS Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.</td></tr>
<tr><td><code>last_updated_at</code></td><td><code>string</code></td><td>The timestamp of when the Amazon DataZone domain was last updated.</td></tr>
<tr><td><code>managed_account_id</code></td><td><code>string</code></td><td>The identifier of the AWS account that manages the domain.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the Amazon DataZone domain.</td></tr>
<tr><td><code>portal_url</code></td><td><code>string</code></td><td>The URL of the data portal for this Amazon DataZone domain.</td></tr>
<tr><td><code>single_sign_on</code></td><td><code>object</code></td><td>The single-sign on configuration of the Amazon DataZone domain.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the Amazon DataZone domain.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags specified for the Amazon DataZone domain.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>domain</code> resource, the following permissions are required:

### Read
<pre>
datazone:GetDomain</pre>

### Update
<pre>
datazone:UpdateDomain,
datazone:GetDomain,
datazone:TagResource,
datazone:UntagResource,
sso:CreateManagedApplicationInstance,
sso:DeleteManagedApplicationInstance,
sso:PutApplicationAssignmentConfiguration</pre>

### Delete
<pre>
datazone:DeleteDomain,
datazone:GetDomain</pre>


## Example
```sql
SELECT
region,
arn,
created_at,
description,
domain_execution_role,
id,
kms_key_identifier,
last_updated_at,
managed_account_id,
name,
portal_url,
single_sign_on,
status,
tags
FROM awscc.datazone.domain
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```

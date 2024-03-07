---
title: organization
hide_title: false
hide_table_of_contents: false
keywords:
  - organization
  - organizations
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>organization</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>organization</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.organizations.organization</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The unique identifier (ID) of an organization.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an organization.</td></tr>
<tr><td><code>feature_set</code></td><td><code>string</code></td><td>Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.</td></tr>
<tr><td><code>management_account_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the account that is designated as the management account for the organization.</td></tr>
<tr><td><code>management_account_id</code></td><td><code>string</code></td><td>The unique identifier (ID) of the management account of an organization.</td></tr>
<tr><td><code>management_account_email</code></td><td><code>string</code></td><td>The email address that is associated with the AWS account that is designated as the management account for the organization.</td></tr>
<tr><td><code>root_id</code></td><td><code>string</code></td><td>The unique identifier (ID) for the root.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>organization</code> resource, the following permissions are required:

### Read
<pre>
organizations:DescribeOrganization,
organizations:ListRoots</pre>

### Delete
<pre>
organizations:DeleteOrganization,
organizations:DescribeOrganization</pre>

### Update
<pre>
</pre>


## Example
```sql
SELECT
region,
id,
arn,
feature_set,
management_account_arn,
management_account_id,
management_account_email,
root_id
FROM awscc.organizations.organization
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```

---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - iam
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
List of policies (requires `aws` provider to be installed)

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>List of policies (requires `aws` provider to be installed)</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iam.policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>policy_name</code></td><td><code>string</code></td><td>The name for the policy</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN</td></tr>
<tr><td><code>attachment_count</code></td><td><code>number</code></td><td>The attachment count for the policy</td></tr>
<tr><td><code>create_date</code></td><td><code>string</code></td><td>The creation date for the policy</td></tr>
<tr><td><code>default_version_id</code></td><td><code>string</code></td><td>The default version id for the policy</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description for the policy</td></tr>
<tr><td><code>is_attachable</code></td><td><code>boolean</code></td><td>Is the policy attachable?</td></tr>
<tr><td><code>path</code></td><td><code>string</code></td><td>The path for the policy</td></tr>
<tr><td><code>permissions_boundary_usage_count</code></td><td><code>number</code></td><td>The permissions boundary usage count for the policy</td></tr>
<tr><td><code>policy_id</code></td><td><code>string</code></td><td>The id for the policy</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags for the policy</td></tr>
<tr><td><code>update_date</code></td><td><code>string</code></td><td>The update date for the policy</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
policy_name,
arn,
attachment_count,
create_date,
default_version_id,
description,
is_attachable,
path,
permissions_boundary_usage_count,
policy_id,
tags,
update_date,
region
FROM awscc.iam.policies

```





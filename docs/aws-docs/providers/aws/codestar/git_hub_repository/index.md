---
title: git_hub_repository
hide_title: false
hide_table_of_contents: false
keywords:
  - git_hub_repository
  - codestar
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>git_hub_repository</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>git_hub_repository</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>git_hub_repository</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codestar.git_hub_repository</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>enable_issues</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>connection_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>repository_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>repository_access_token</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>repository_owner</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>is_private</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>code</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>repository_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
enable_issues,
connection_arn,
repository_name,
repository_access_token,
id,
repository_owner,
is_private,
code,
repository_description
FROM aws.codestar.git_hub_repository
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```

---
title: repository_links
hide_title: false
hide_table_of_contents: false
keywords:
  - repository_links
  - codestarconnections
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>repository_links</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>repository_links</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.codestarconnections.repository_links</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>repository_link_arn</code></td><td><code>string</code></td><td>A unique Amazon Resource Name (ARN) to designate the repository link.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>repository_links</code> resource, the following permissions are required:

### Create
```json
codestar-connections:CreateRepositoryLink,
codestar-connections:TagResource,
codestar-connections:UseConnection,
codestar-connections:PassConnection,
codestar-connections:GetConnection,
iam:CreateServiceLinkedRole
```

### List
```json
codestar-connections:ListRepositoryLinks,
codestar-connections:ListTagsForResource
```


## Example
```sql
SELECT
region,
repository_link_arn
FROM awscc.codestarconnections.repository_links
WHERE region = 'us-east-1'
```

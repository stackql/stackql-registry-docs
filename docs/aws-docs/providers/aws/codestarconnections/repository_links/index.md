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
Used to retrieve a list of <code>repository_links</code> in a region or create a <code>repository_links</code> resource, use <code>repository_link</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for AWS::CodeStarConnections::RepositoryLink resource which is used to aggregate repository metadata relevant to synchronizing source provider content to AWS Resources.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codestarconnections.repository_links</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>repository_link_arn</code></td><td><code>string</code></td><td>A unique Amazon Resource Name (ARN) to designate the repository link.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
repository_link_arn
FROM aws.codestarconnections.repository_links
WHERE region = 'us-east-1'
```

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


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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>repository_links</code> in a region or to create or delete a <code>repository_links</code> resource, use <code>repository_link</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for AWS::CodeStarConnections::RepositoryLink resource which is used to aggregate repository metadata relevant to synchronizing source provider content to AWS Resources.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codestarconnections.repository_links" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="repository_link_arn" /></td><td><code>string</code></td><td>A unique Amazon Resource Name (ARN) to designate the repository link.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
repository_link_arn
FROM aws.codestarconnections.repository_links
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>repository_link</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- repository_link.iql (required properties only)
INSERT INTO aws.codestarconnections.repository_links (
 ConnectionArn,
 OwnerId,
 RepositoryName,
 region
)
SELECT 
'{{ ConnectionArn }}',
 '{{ OwnerId }}',
 '{{ RepositoryName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- repository_link.iql (all properties)
INSERT INTO aws.codestarconnections.repository_links (
 ConnectionArn,
 OwnerId,
 RepositoryName,
 EncryptionKeyArn,
 Tags,
 region
)
SELECT 
 '{{ ConnectionArn }}',
 '{{ OwnerId }}',
 '{{ RepositoryName }}',
 '{{ EncryptionKeyArn }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: repository_link
    props:
      - name: ConnectionArn
        value: '{{ ConnectionArn }}'
      - name: OwnerId
        value: '{{ OwnerId }}'
      - name: RepositoryName
        value: '{{ RepositoryName }}'
      - name: EncryptionKeyArn
        value: '{{ EncryptionKeyArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.codestarconnections.repository_links
WHERE data__Identifier = '<RepositoryLinkArn>'
AND region = 'us-east-1';
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

### Delete
```json
codestar-connections:GetRepositoryLink,
codestar-connections:DeleteRepositoryLink,
codestar-connections:GetConnection
```

### List
```json
codestar-connections:ListRepositoryLinks,
codestar-connections:ListTagsForResource
```


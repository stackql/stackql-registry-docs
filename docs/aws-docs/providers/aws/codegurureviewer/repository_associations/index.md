---
title: repository_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - repository_associations
  - codegurureviewer
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


Used to retrieve a list of <code>repository_associations</code> in a region or to create or delete a <code>repository_associations</code> resource, use <code>repository_association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This resource schema represents the RepositoryAssociation resource in the Amazon CodeGuru Reviewer service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codegurureviewer.repository_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="association_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the repository association.</td></tr>
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
association_arn
FROM aws.codegurureviewer.repository_associations
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>repository_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- repository_association.iql (required properties only)
INSERT INTO aws.codegurureviewer.repository_associations (
 Name,
 Type,
 region
)
SELECT 
'{{ Name }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- repository_association.iql (all properties)
INSERT INTO aws.codegurureviewer.repository_associations (
 Name,
 Type,
 Owner,
 BucketName,
 ConnectionArn,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Type }}',
 '{{ Owner }}',
 '{{ BucketName }}',
 '{{ ConnectionArn }}',
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
  - name: repository_association
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Type
        value: '{{ Type }}'
      - name: Owner
        value: '{{ Owner }}'
      - name: BucketName
        value: '{{ BucketName }}'
      - name: ConnectionArn
        value: '{{ ConnectionArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.codegurureviewer.repository_associations
WHERE data__Identifier = '<AssociationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>repository_associations</code> resource, the following permissions are required:

### Create
```json
codeguru-reviewer:DescribeRepositoryAssociation,
codeguru-reviewer:AssociateRepository,
codeguru-reviewer:TagResource,
iam:CreateServiceLinkedRole,
codecommit:TagResource,
codecommit:GitPull,
codecommit:TagResource,
events:PutRule,
events:PutTargets,
codestar-connections:ListBranches,
codestar-connections:ListRepositories,
codestar-connections:ListTagsForResource,
codestar-connections:PassConnection,
codestar-connections:TagResource,
codestar-connections:UseConnection,
s3:ListBucket
```

### Delete
```json
codeguru-reviewer:DescribeRepositoryAssociation,
codeguru-reviewer:DisassociateRepository,
codecommit:UntagResource,
events:DeleteRule,
events:RemoveTargets,
codestar-connections:UntagResource,
codestar-connections:ListTagsForResource
```

### List
```json
codeguru-reviewer:ListRepositoryAssociations
```


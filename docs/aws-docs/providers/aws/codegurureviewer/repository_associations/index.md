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

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Type": "{{ Type }}"
}
>>>
--required properties only
INSERT INTO aws.codegurureviewer.repository_associations (
 Name,
 Type,
 region
)
SELECT 
{{ Name }},
 {{ Type }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Type": "{{ Type }}",
 "Owner": "{{ Owner }}",
 "BucketName": "{{ BucketName }}",
 "ConnectionArn": "{{ ConnectionArn }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
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
 {{ Name }},
 {{ Type }},
 {{ Owner }},
 {{ BucketName }},
 {{ ConnectionArn }},
 {{ Tags }},
 'us-east-1';
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


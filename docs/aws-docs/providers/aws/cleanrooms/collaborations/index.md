---
title: collaborations
hide_title: false
hide_table_of_contents: false
keywords:
  - collaborations
  - cleanrooms
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

Creates, updates, deletes or gets a <code>collaboration</code> resource or lists <code>collaborations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collaborations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a collaboration between AWS accounts that allows for secure data collaboration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.collaborations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.</td></tr>
<tr><td><CopyableCode code="collaboration_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creator_display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creator_member_abilities" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="data_encryption_metadata" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="members" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="query_log_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creator_payment_configuration" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="CreatorDisplayName, CreatorMemberAbilities, Members, Name, Description, QueryLogStatus, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>collaborations</code> in a region.
```sql
SELECT
region,
collaboration_identifier
FROM aws.cleanrooms.collaborations
WHERE region = 'us-east-1';
```
Gets all properties from a <code>collaboration</code>.
```sql
SELECT
region,
arn,
tags,
collaboration_identifier,
creator_display_name,
creator_member_abilities,
data_encryption_metadata,
description,
members,
name,
query_log_status,
creator_payment_configuration
FROM aws.cleanrooms.collaborations
WHERE region = 'us-east-1' AND data__Identifier = '<CollaborationIdentifier>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>collaboration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
INSERT INTO aws.cleanrooms.collaborations (
 CreatorDisplayName,
 CreatorMemberAbilities,
 Description,
 Members,
 Name,
 QueryLogStatus,
 region
)
SELECT 
'{{ CreatorDisplayName }}',
 '{{ CreatorMemberAbilities }}',
 '{{ Description }}',
 '{{ Members }}',
 '{{ Name }}',
 '{{ QueryLogStatus }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cleanrooms.collaborations (
 Tags,
 CreatorDisplayName,
 CreatorMemberAbilities,
 DataEncryptionMetadata,
 Description,
 Members,
 Name,
 QueryLogStatus,
 CreatorPaymentConfiguration,
 region
)
SELECT 
 '{{ Tags }}',
 '{{ CreatorDisplayName }}',
 '{{ CreatorMemberAbilities }}',
 '{{ DataEncryptionMetadata }}',
 '{{ Description }}',
 '{{ Members }}',
 '{{ Name }}',
 '{{ QueryLogStatus }}',
 '{{ CreatorPaymentConfiguration }}',
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
  - name: collaboration
    props:
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: CreatorDisplayName
        value: '{{ CreatorDisplayName }}'
      - name: CreatorMemberAbilities
        value:
          - '{{ CreatorMemberAbilities[0] }}'
      - name: DataEncryptionMetadata
        value:
          AllowCleartext: '{{ AllowCleartext }}'
          AllowDuplicates: '{{ AllowDuplicates }}'
          AllowJoinsOnColumnsWithDifferentNames: '{{ AllowJoinsOnColumnsWithDifferentNames }}'
          PreserveNulls: '{{ PreserveNulls }}'
      - name: Description
        value: '{{ Description }}'
      - name: Members
        value:
          - AccountId: '{{ AccountId }}'
            MemberAbilities: null
            DisplayName: null
            PaymentConfiguration:
              QueryCompute:
                IsResponsible: '{{ IsResponsible }}'
      - name: Name
        value: '{{ Name }}'
      - name: QueryLogStatus
        value: '{{ QueryLogStatus }}'
      - name: CreatorPaymentConfiguration
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cleanrooms.collaborations
WHERE data__Identifier = '<CollaborationIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>collaborations</code> resource, the following permissions are required:

### Create
```json
cleanrooms:CreateCollaboration,
cleanrooms:GetCollaboration,
cleanrooms:ListMembers,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:GetCollaboration,
cleanrooms:ListCollaborations
```

### Read
```json
cleanrooms:GetCollaboration,
cleanrooms:ListMembers,
cleanrooms:ListTagsForResource
```

### Update
```json
cleanrooms:UpdateCollaboration,
cleanrooms:GetCollaboration,
cleanrooms:ListMembers,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:UntagResource
```

### Delete
```json
cleanrooms:DeleteCollaboration,
cleanrooms:GetCollaboration,
cleanrooms:ListTagsForResource,
cleanrooms:UntagResource,
cleanrooms:ListMembers,
cleanrooms:ListCollaborations
```

### List
```json
cleanrooms:ListCollaborations
```


---
title: id_mapping_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - id_mapping_tables
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

Creates, updates, deletes or gets an <code>id_mapping_table</code> resource or lists <code>id_mapping_tables</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>id_mapping_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents an association between an ID mapping workflow and a collaboration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.id_mapping_tables" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id_mapping_table_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="input_reference_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="membership_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="membership_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collaboration_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collaboration_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="input_reference_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idmappingtable.html"><code>AWS::CleanRooms::IdMappingTable</code></a>.

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
    <td><CopyableCode code="MembershipIdentifier, Name, InputReferenceConfig, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>id_mapping_tables</code> in a region.
```sql
SELECT
region,
id_mapping_table_identifier,
arn,
input_reference_config,
membership_identifier,
membership_arn,
collaboration_identifier,
collaboration_arn,
description,
name,
input_reference_properties,
kms_key_arn,
tags
FROM aws.cleanrooms.id_mapping_tables
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>id_mapping_table</code>.
```sql
SELECT
region,
id_mapping_table_identifier,
arn,
input_reference_config,
membership_identifier,
membership_arn,
collaboration_identifier,
collaboration_arn,
description,
name,
input_reference_properties,
kms_key_arn,
tags
FROM aws.cleanrooms.id_mapping_tables
WHERE region = 'us-east-1' AND data__Identifier = '<IdMappingTableIdentifier>|<MembershipIdentifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>id_mapping_table</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cleanrooms.id_mapping_tables (
 InputReferenceConfig,
 MembershipIdentifier,
 Name,
 region
)
SELECT 
'{{ InputReferenceConfig }}',
 '{{ MembershipIdentifier }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cleanrooms.id_mapping_tables (
 InputReferenceConfig,
 MembershipIdentifier,
 Description,
 Name,
 KmsKeyArn,
 Tags,
 region
)
SELECT 
 '{{ InputReferenceConfig }}',
 '{{ MembershipIdentifier }}',
 '{{ Description }}',
 '{{ Name }}',
 '{{ KmsKeyArn }}',
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
  - name: id_mapping_table
    props:
      - name: InputReferenceConfig
        value:
          InputReferenceArn: '{{ InputReferenceArn }}'
          ManageResourcePolicies: '{{ ManageResourcePolicies }}'
      - name: MembershipIdentifier
        value: '{{ MembershipIdentifier }}'
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: KmsKeyArn
        value: '{{ KmsKeyArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cleanrooms.id_mapping_tables
WHERE data__Identifier = '<IdMappingTableIdentifier|MembershipIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>id_mapping_tables</code> resource, the following permissions are required:

### Create
```json
cleanrooms:CreateIdMappingTable,
cleanrooms:GetIdMappingTable,
cleanrooms:ListIdMappingTables,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:GetMembership,
cleanrooms:GetCollaboration,
entityresolution:GetIdMappingWorkflow,
entityresolution:AddPolicyStatement
```

### Read
```json
cleanrooms:GetIdMappingTable,
cleanrooms:ListTagsForResource,
cleanrooms:GetMembership,
cleanrooms:GetCollaboration
```

### Update
```json
cleanrooms:UpdateIdMappingTable,
cleanrooms:GetIdMappingTable,
cleanrooms:GetMembership,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:UntagResource,
entityresolution:GetIdMappingWorkflow,
entityresolution:AddPolicyStatement
```

### Delete
```json
cleanrooms:DeleteIdMappingTable,
cleanrooms:GetIdMappingTable,
cleanrooms:ListIdMappingTables,
cleanrooms:GetMembership,
cleanrooms:ListTagsForResource,
cleanrooms:UntagResource,
entityresolution:GetIdMappingWorkflow,
entityresolution:AddPolicyStatement,
entityresolution:DeletePolicyStatement
```

### List
```json
cleanrooms:ListIdMappingTables,
cleanrooms:GetMembership,
cleanrooms:GetCollaboration
```

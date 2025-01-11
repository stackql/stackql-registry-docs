---
title: configured_table_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - configured_table_associations
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

Creates, updates, deletes or gets a <code>configured_table_association</code> resource or lists <code>configured_table_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configured_table_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a table that can be queried within a collaboration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.configured_table_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.</td></tr>
<tr><td><CopyableCode code="configured_table_association_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="configured_table_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="membership_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="configured_table_association_analysis_rules" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html"><code>AWS::CleanRooms::ConfiguredTableAssociation</code></a>.

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
    <td><CopyableCode code="ConfiguredTableIdentifier, Name, RoleArn, MembershipIdentifier, region" /></td>
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
Gets all <code>configured_table_associations</code> in a region.
```sql
SELECT
region,
arn,
tags,
configured_table_association_identifier,
configured_table_identifier,
description,
membership_identifier,
name,
role_arn,
configured_table_association_analysis_rules
FROM aws.cleanrooms.configured_table_associations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>configured_table_association</code>.
```sql
SELECT
region,
arn,
tags,
configured_table_association_identifier,
configured_table_identifier,
description,
membership_identifier,
name,
role_arn,
configured_table_association_analysis_rules
FROM aws.cleanrooms.configured_table_associations
WHERE region = 'us-east-1' AND data__Identifier = '<ConfiguredTableAssociationIdentifier>|<MembershipIdentifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configured_table_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cleanrooms.configured_table_associations (
 ConfiguredTableIdentifier,
 MembershipIdentifier,
 Name,
 RoleArn,
 region
)
SELECT 
'{{ ConfiguredTableIdentifier }}',
 '{{ MembershipIdentifier }}',
 '{{ Name }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cleanrooms.configured_table_associations (
 Tags,
 ConfiguredTableIdentifier,
 Description,
 MembershipIdentifier,
 Name,
 RoleArn,
 ConfiguredTableAssociationAnalysisRules,
 region
)
SELECT 
 '{{ Tags }}',
 '{{ ConfiguredTableIdentifier }}',
 '{{ Description }}',
 '{{ MembershipIdentifier }}',
 '{{ Name }}',
 '{{ RoleArn }}',
 '{{ ConfiguredTableAssociationAnalysisRules }}',
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
  - name: configured_table_association
    props:
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: ConfiguredTableIdentifier
        value: '{{ ConfiguredTableIdentifier }}'
      - name: Description
        value: '{{ Description }}'
      - name: MembershipIdentifier
        value: '{{ MembershipIdentifier }}'
      - name: Name
        value: '{{ Name }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: ConfiguredTableAssociationAnalysisRules
        value:
          - Type: '{{ Type }}'
            Policy:
              V1: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cleanrooms.configured_table_associations
WHERE data__Identifier = '<ConfiguredTableAssociationIdentifier|MembershipIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>configured_table_associations</code> resource, the following permissions are required:

### Create
```json
cleanrooms:CreateConfiguredTableAssociation,
iam:PassRole,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:GetConfiguredTableAssociation,
cleanrooms:ListConfiguredTableAssociations,
cleanrooms:DeleteConfiguredTableAssociation,
cleanrooms:DeleteConfiguredTableAssociationAnalysisRule,
cleanrooms:CreateConfiguredTableAssociationAnalysisRule,
cleanrooms:GetConfiguredTableAssociationAnalysisRule
```

### Read
```json
cleanrooms:GetConfiguredTableAssociation,
cleanrooms:ListTagsForResource,
cleanrooms:GetConfiguredTableAssociationAnalysisRule
```

### Update
```json
cleanrooms:UpdateConfiguredTableAssociation,
cleanrooms:GetConfiguredTableAssociation,
iam:PassRole,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:UntagResource,
cleanrooms:DeleteConfiguredTableAssociationAnalysisRule,
cleanrooms:CreateConfiguredTableAssociationAnalysisRule,
cleanrooms:GetConfiguredTableAssociationAnalysisRule,
cleanrooms:UpdateConfiguredTableAssociationAnalysisRule
```

### Delete
```json
cleanrooms:DeleteConfiguredTableAssociation,
cleanrooms:GetConfiguredTableAssociation,
cleanrooms:ListConfiguredTableAssociations,
cleanrooms:ListTagsForResource,
cleanrooms:UntagResource,
cleanrooms:DeleteConfiguredTableAssociationAnalysisRule,
cleanrooms:GetConfiguredTableAssociationAnalysisRule
```

### List
```json
cleanrooms:ListConfiguredTableAssociations
```

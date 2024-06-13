---
title: indices
hide_title: false
hide_table_of_contents: false
keywords:
  - indices
  - kendra
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

Creates, updates, deletes or gets an <code>index</code> resource or lists <code>indices</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>indices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A Kendra index</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kendra.indices" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Unique ID of index</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the index</td></tr>
<tr><td><CopyableCode code="server_side_encryption_configuration" /></td><td><code>object</code></td><td>Server side encryption configuration</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags for labeling the index</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of index</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>Role Arn</td></tr>
<tr><td><CopyableCode code="edition" /></td><td><code>string</code></td><td>Edition of index</td></tr>
<tr><td><CopyableCode code="document_metadata_configurations" /></td><td><code>array</code></td><td>Document metadata configurations</td></tr>
<tr><td><CopyableCode code="capacity_units" /></td><td><code>object</code></td><td>Capacity units</td></tr>
<tr><td><CopyableCode code="user_context_policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="user_token_configurations" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, RoleArn, Edition, region" /></td>
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
List all <code>indices</code> in a region.
```sql
SELECT
region,
id
FROM aws.kendra.indices
WHERE region = 'us-east-1';
```
Gets all properties from an <code>index</code>.
```sql
SELECT
region,
id,
arn,
description,
server_side_encryption_configuration,
tags,
name,
role_arn,
edition,
document_metadata_configurations,
capacity_units,
user_context_policy,
user_token_configurations
FROM aws.kendra.indices
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>index</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.kendra.indices (
 Name,
 RoleArn,
 Edition,
 region
)
SELECT 
'{{ Name }}',
 '{{ RoleArn }}',
 '{{ Edition }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.kendra.indices (
 Description,
 ServerSideEncryptionConfiguration,
 Tags,
 Name,
 RoleArn,
 Edition,
 DocumentMetadataConfigurations,
 CapacityUnits,
 UserContextPolicy,
 UserTokenConfigurations,
 region
)
SELECT 
 '{{ Description }}',
 '{{ ServerSideEncryptionConfiguration }}',
 '{{ Tags }}',
 '{{ Name }}',
 '{{ RoleArn }}',
 '{{ Edition }}',
 '{{ DocumentMetadataConfigurations }}',
 '{{ CapacityUnits }}',
 '{{ UserContextPolicy }}',
 '{{ UserTokenConfigurations }}',
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
  - name: index
    props:
      - name: Description
        value: '{{ Description }}'
      - name: ServerSideEncryptionConfiguration
        value:
          KmsKeyId: '{{ KmsKeyId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Name
        value: '{{ Name }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Edition
        value: '{{ Edition }}'
      - name: DocumentMetadataConfigurations
        value:
          - Name: '{{ Name }}'
            Type: '{{ Type }}'
            Relevance:
              Freshness: '{{ Freshness }}'
              Importance: '{{ Importance }}'
              Duration: '{{ Duration }}'
              RankOrder: '{{ RankOrder }}'
              ValueImportanceItems:
                - Key: '{{ Key }}'
                  Value: null
            Search:
              Facetable: '{{ Facetable }}'
              Searchable: '{{ Searchable }}'
              Displayable: '{{ Displayable }}'
              Sortable: '{{ Sortable }}'
      - name: CapacityUnits
        value:
          StorageCapacityUnits: '{{ StorageCapacityUnits }}'
          QueryCapacityUnits: '{{ QueryCapacityUnits }}'
      - name: UserContextPolicy
        value: '{{ UserContextPolicy }}'
      - name: UserTokenConfigurations
        value:
          - JwtTokenTypeConfiguration:
              KeyLocation: '{{ KeyLocation }}'
              URL: '{{ URL }}'
              SecretManagerArn: null
              UserNameAttributeField: '{{ UserNameAttributeField }}'
              GroupAttributeField: '{{ GroupAttributeField }}'
              Issuer: '{{ Issuer }}'
              ClaimRegex: '{{ ClaimRegex }}'
            JsonTokenTypeConfiguration:
              UserNameAttributeField: null
              GroupAttributeField: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.kendra.indices
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>indices</code> resource, the following permissions are required:

### Create
```json
kendra:CreateIndex,
kendra:DescribeIndex,
kendra:UpdateIndex,
kendra:ListTagsForResource,
iam:PassRole,
kendra:TagResource
```

### Read
```json
kendra:DescribeIndex,
kendra:ListTagsForResource
```

### Update
```json
kendra:DescribeIndex,
kendra:UpdateIndex,
kendra:ListTagsForResource,
kendra:TagResource,
kendra:UntagResource,
iam:PassRole
```

### Delete
```json
kendra:DescribeIndex,
kendra:DeleteIndex
```

### List
```json
kendra:ListIndices
```


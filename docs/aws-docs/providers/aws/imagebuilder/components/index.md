---
title: components
hide_title: false
hide_table_of_contents: false
keywords:
  - components
  - imagebuilder
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

Creates, updates, deletes or gets a <code>component</code> resource or lists <code>components</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::Component</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.components" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the component.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the component.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version of the component.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the component.</td></tr>
<tr><td><CopyableCode code="change_description" /></td><td><code>string</code></td><td>The change description of the component.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the component denotes whether the component is used to build the image or only to test it.</td></tr>
<tr><td><CopyableCode code="platform" /></td><td><code>string</code></td><td>The platform of the component.</td></tr>
<tr><td><CopyableCode code="data" /></td><td><code>string</code></td><td>The data of the component.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The KMS key identifier used to encrypt the component.</td></tr>
<tr><td><CopyableCode code="encrypted" /></td><td><code>boolean</code></td><td>The encryption status of the component.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The tags associated with the component.</td></tr>
<tr><td><CopyableCode code="uri" /></td><td><code>string</code></td><td>The uri of the component.</td></tr>
<tr><td><CopyableCode code="supported_os_versions" /></td><td><code>array</code></td><td>The operating system (OS) version supported by the component.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html"><code>AWS::ImageBuilder::Component</code></a>.

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
    <td><CopyableCode code="Name, Platform, Version, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>components</code> in a region.
```sql
SELECT
region,
arn,
name,
version,
description,
change_description,
type,
platform,
data,
kms_key_id,
encrypted,
tags,
uri,
supported_os_versions
FROM aws.imagebuilder.components
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>component</code>.
```sql
SELECT
region,
arn,
name,
version,
description,
change_description,
type,
platform,
data,
kms_key_id,
encrypted,
tags,
uri,
supported_os_versions
FROM aws.imagebuilder.components
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>component</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.imagebuilder.components (
 Name,
 Version,
 Platform,
 region
)
SELECT 
'{{ Name }}',
 '{{ Version }}',
 '{{ Platform }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.imagebuilder.components (
 Name,
 Version,
 Description,
 ChangeDescription,
 Platform,
 Data,
 KmsKeyId,
 Tags,
 Uri,
 SupportedOsVersions,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Version }}',
 '{{ Description }}',
 '{{ ChangeDescription }}',
 '{{ Platform }}',
 '{{ Data }}',
 '{{ KmsKeyId }}',
 '{{ Tags }}',
 '{{ Uri }}',
 '{{ SupportedOsVersions }}',
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
  - name: component
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Version
        value: '{{ Version }}'
      - name: Description
        value: '{{ Description }}'
      - name: ChangeDescription
        value: '{{ ChangeDescription }}'
      - name: Platform
        value: '{{ Platform }}'
      - name: Data
        value: '{{ Data }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: Tags
        value: {}
      - name: Uri
        value: '{{ Uri }}'
      - name: SupportedOsVersions
        value:
          - '{{ SupportedOsVersions[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.imagebuilder.components
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>components</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
iam:GetRole,
kms:GenerateDataKey,
kms:GenerateDataKeyPair,
kms:GenerateDataKeyPairWithoutPlaintext,
kms:GenerateDataKeyWithoutPlaintext,
kms:Encrypt,
kms:Decrypt,
s3:GetObject,
s3:HeadBucket,
s3:GetBucketLocation,
imagebuilder:TagResource,
imagebuilder:GetComponent,
imagebuilder:CreateComponent
```

### Read
```json
imagebuilder:GetComponent,
kms:Decrypt
```

### Delete
```json
imagebuilder:GetComponent,
imagebuilder:UnTagResource,
imagebuilder:DeleteComponent
```

### List
```json
imagebuilder:ListComponents,
imagebuilder:ListComponentBuildVersions
```

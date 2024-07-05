---
title: public_type_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - public_type_versions
  - cloudformation
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

Creates, updates, deletes or gets a <code>public_type_version</code> resource or lists <code>public_type_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_type_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Test and Publish a resource that has been registered in the CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.public_type_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the extension.</td></tr>
<tr><td><CopyableCode code="type_version_arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the extension with the versionId.</td></tr>
<tr><td><CopyableCode code="public_version_number" /></td><td><code>string</code></td><td>The version number of a public third-party extension</td></tr>
<tr><td><CopyableCode code="publisher_id" /></td><td><code>string</code></td><td>The publisher id assigned by CloudFormation for publishing in this region.</td></tr>
<tr><td><CopyableCode code="public_type_arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) assigned to the public extension upon publication</td></tr>
<tr><td><CopyableCode code="type_name" /></td><td><code>string</code></td><td>The name of the type being registered.<br />We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
<tr><td><CopyableCode code="log_delivery_bucket" /></td><td><code>string</code></td><td>A url to the S3 bucket where logs for the testType run will be available</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The kind of extension</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>public_type_versions</code> in a region.
```sql
SELECT
region,
arn,
type_version_arn,
public_version_number,
publisher_id,
public_type_arn,
type_name,
log_delivery_bucket,
type
FROM aws.cloudformation.public_type_versions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>public_type_version</code>.
```sql
SELECT
region,
arn,
type_version_arn,
public_version_number,
publisher_id,
public_type_arn,
type_name,
log_delivery_bucket,
type
FROM aws.cloudformation.public_type_versions
WHERE region = 'us-east-1' AND data__Identifier = '<PublicTypeArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>public_type_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudformation.public_type_versions (
 Arn,
 PublicVersionNumber,
 TypeName,
 LogDeliveryBucket,
 Type,
 region
)
SELECT 
'{{ Arn }}',
 '{{ PublicVersionNumber }}',
 '{{ TypeName }}',
 '{{ LogDeliveryBucket }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudformation.public_type_versions (
 Arn,
 PublicVersionNumber,
 TypeName,
 LogDeliveryBucket,
 Type,
 region
)
SELECT 
 '{{ Arn }}',
 '{{ PublicVersionNumber }}',
 '{{ TypeName }}',
 '{{ LogDeliveryBucket }}',
 '{{ Type }}',
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
  - name: public_type_version
    props:
      - name: Arn
        value: '{{ Arn }}'
      - name: PublicVersionNumber
        value: '{{ PublicVersionNumber }}'
      - name: TypeName
        value: '{{ TypeName }}'
      - name: LogDeliveryBucket
        value: '{{ LogDeliveryBucket }}'
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## Permissions

To operate on the <code>public_type_versions</code> resource, the following permissions are required:

### Create
```json
cloudformation:TestType,
cloudformation:DescribeType,
cloudformation:PublishType,
cloudformation:DescribePublisher,
s3:GetObject,
s3:PutObject
```

### Read
```json
cloudformation:DescribeType,
cloudformation:DescribePublisher
```

### List
```json
cloudformation:ListTypes
```


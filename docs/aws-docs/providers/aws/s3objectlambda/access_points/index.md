---
title: access_points
hide_title: false
hide_table_of_contents: false
keywords:
  - access_points
  - s3objectlambda
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

Creates, updates, deletes or gets an <code>access_point</code> resource or lists <code>access_points</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::S3ObjectLambda::AccessPoint resource is an Amazon S3ObjectLambda resource type that you can use to add computation to S3 actions</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3objectlambda.access_points" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name you want to assign to this Object lambda Access Point.</td></tr>
<tr><td><CopyableCode code="alias" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_date" /></td><td><code>string</code></td><td>The date and time when the Object lambda Access Point was created.</td></tr>
<tr><td><CopyableCode code="public_access_block_configuration" /></td><td><code>object</code></td><td>The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.</td></tr>
<tr><td><CopyableCode code="policy_status" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="object_lambda_configuration" /></td><td><code>object</code></td><td>The Object lambda Access Point Configuration that configures transformations to be applied on the objects on specified S3 Actions</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3objectlambda-accesspoint.html"><code>AWS::S3ObjectLambda::AccessPoint</code></a>.

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
    <td><CopyableCode code="ObjectLambdaConfiguration, region" /></td>
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
Gets all <code>access_points</code> in a region.
```sql
SELECT
region,
name,
alias,
arn,
creation_date,
public_access_block_configuration,
policy_status,
object_lambda_configuration
FROM aws.s3objectlambda.access_points
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>access_point</code>.
```sql
SELECT
region,
name,
alias,
arn,
creation_date,
public_access_block_configuration,
policy_status,
object_lambda_configuration
FROM aws.s3objectlambda.access_points
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_point</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.s3objectlambda.access_points (
 ObjectLambdaConfiguration,
 region
)
SELECT 
'{{ ObjectLambdaConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.s3objectlambda.access_points (
 Name,
 ObjectLambdaConfiguration,
 region
)
SELECT 
 '{{ Name }}',
 '{{ ObjectLambdaConfiguration }}',
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
  - name: access_point
    props:
      - name: Name
        value: '{{ Name }}'
      - name: ObjectLambdaConfiguration
        value:
          SupportingAccessPoint: '{{ SupportingAccessPoint }}'
          AllowedFeatures:
            - '{{ AllowedFeatures[0] }}'
          CloudWatchMetricsEnabled: '{{ CloudWatchMetricsEnabled }}'
          TransformationConfigurations:
            - Actions:
                - '{{ Actions[0] }}'
              ContentTransformation: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.s3objectlambda.access_points
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>access_points</code> resource, the following permissions are required:

### Create
```json
s3:CreateAccessPointForObjectLambda,
s3:PutAccessPointConfigurationForObjectLambda,
s3:GetAccessPointForObjectLambda,
s3:GetAccessPointPolicyStatusForObjectLambda,
s3:GetAccessPointConfigurationForObjectLambda
```

### Read
```json
s3:GetAccessPointForObjectLambda,
s3:GetAccessPointPolicyStatusForObjectLambda,
s3:GetAccessPointConfigurationForObjectLambda
```

### Update
```json
s3:PutAccessPointConfigurationForObjectLambda,
s3:GetAccessPointForObjectLambda,
s3:GetAccessPointPolicyStatusForObjectLambda,
s3:GetAccessPointConfigurationForObjectLambda
```

### Delete
```json
s3:DeleteAccessPointForObjectLambda
```

### List
```json
s3:ListAccessPointsForObjectLambda
```

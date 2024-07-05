---
title: verified_access_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_access_instances
  - ec2
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

Creates, updates, deletes or gets a <code>verified_access_instance</code> resource or lists <code>verified_access_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_access_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::VerifiedAccessInstance resource creates an AWS EC2 Verified Access Instance.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.verified_access_instances" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="verified_access_instance_id" /></td><td><code>string</code></td><td>The ID of the AWS Verified Access instance.</td></tr>
<tr><td><CopyableCode code="verified_access_trust_providers" /></td><td><code>array</code></td><td>AWS Verified Access trust providers.</td></tr>
<tr><td><CopyableCode code="verified_access_trust_provider_ids" /></td><td><code>array</code></td><td>The IDs of the AWS Verified Access trust providers.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>Time this Verified Access Instance was created.</td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td>Time this Verified Access Instance was last updated.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the AWS Verified Access instance.</td></tr>
<tr><td><CopyableCode code="logging_configurations" /></td><td><code>object</code></td><td>The configuration options for AWS Verified Access instances.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="fips_enabled" /></td><td><code>boolean</code></td><td>Indicates whether FIPS is enabled</td></tr>
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
Gets all <code>verified_access_instances</code> in a region.
```sql
SELECT
region,
verified_access_instance_id,
verified_access_trust_providers,
verified_access_trust_provider_ids,
creation_time,
last_updated_time,
description,
logging_configurations,
tags,
fips_enabled
FROM aws.ec2.verified_access_instances
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>verified_access_instance</code>.
```sql
SELECT
region,
verified_access_instance_id,
verified_access_trust_providers,
verified_access_trust_provider_ids,
creation_time,
last_updated_time,
description,
logging_configurations,
tags,
fips_enabled
FROM aws.ec2.verified_access_instances
WHERE region = 'us-east-1' AND data__Identifier = '<VerifiedAccessInstanceId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>verified_access_instance</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.verified_access_instances (
 VerifiedAccessTrustProviders,
 VerifiedAccessTrustProviderIds,
 Description,
 LoggingConfigurations,
 Tags,
 FipsEnabled,
 region
)
SELECT 
'{{ VerifiedAccessTrustProviders }}',
 '{{ VerifiedAccessTrustProviderIds }}',
 '{{ Description }}',
 '{{ LoggingConfigurations }}',
 '{{ Tags }}',
 '{{ FipsEnabled }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.verified_access_instances (
 VerifiedAccessTrustProviders,
 VerifiedAccessTrustProviderIds,
 Description,
 LoggingConfigurations,
 Tags,
 FipsEnabled,
 region
)
SELECT 
 '{{ VerifiedAccessTrustProviders }}',
 '{{ VerifiedAccessTrustProviderIds }}',
 '{{ Description }}',
 '{{ LoggingConfigurations }}',
 '{{ Tags }}',
 '{{ FipsEnabled }}',
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
  - name: verified_access_instance
    props:
      - name: VerifiedAccessTrustProviders
        value:
          - TrustProviderType: '{{ TrustProviderType }}'
            DeviceTrustProviderType: '{{ DeviceTrustProviderType }}'
            UserTrustProviderType: '{{ UserTrustProviderType }}'
            OidcOptions:
              Issuer: '{{ Issuer }}'
              AuthorizationEndpoint: '{{ AuthorizationEndpoint }}'
              TokenEndpoint: '{{ TokenEndpoint }}'
              UserInfoEndpoint: '{{ UserInfoEndpoint }}'
              ClientId: '{{ ClientId }}'
              ClientSecret: '{{ ClientSecret }}'
              Scope: '{{ Scope }}'
            DeviceOptions:
              TenantId: '{{ TenantId }}'
              PublicSigningKeyUrl: '{{ PublicSigningKeyUrl }}'
            PolicyReferenceName: '{{ PolicyReferenceName }}'
            Description: '{{ Description }}'
            Tags:
              - Key: '{{ Key }}'
                Value: '{{ Value }}'
            SseSpecification:
              KmsKeyArn: '{{ KmsKeyArn }}'
              CustomerManagedKeyEnabled: '{{ CustomerManagedKeyEnabled }}'
      - name: VerifiedAccessTrustProviderIds
        value:
          - '{{ VerifiedAccessTrustProviderIds[0] }}'
      - name: Description
        value: '{{ Description }}'
      - name: LoggingConfigurations
        value:
          LogVersion: '{{ LogVersion }}'
          IncludeTrustContext: '{{ IncludeTrustContext }}'
          CloudWatchLogs:
            Enabled: '{{ Enabled }}'
            LogGroup: '{{ LogGroup }}'
          KinesisDataFirehose:
            Enabled: '{{ Enabled }}'
            DeliveryStream: '{{ DeliveryStream }}'
          S3:
            Enabled: '{{ Enabled }}'
            BucketName: '{{ BucketName }}'
            BucketOwner: '{{ BucketOwner }}'
            Prefix: '{{ Prefix }}'
      - name: Tags
        value:
          - null
      - name: FipsEnabled
        value: '{{ FipsEnabled }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.verified_access_instances
WHERE data__Identifier = '<VerifiedAccessInstanceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>verified_access_instances</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVerifiedAccessInstance,
ec2:AttachVerifiedAccessTrustProvider,
ec2:ModifyVerifiedAccessInstanceLoggingConfiguration,
ec2:DescribeVerifiedAccessInstances,
ec2:DescribeVerifiedAccessInstanceLoggingConfigurations,
ec2:CreateTags,
ec2:DescribeTags,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:PutDestination,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
logs:PutLogEvents,
logs:DescribeLogStreams,
s3:listBuckets,
s3:PutObject,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
logs:DescribeLogGroups,
logs:PutResourcePolicy,
firehose:TagDeliveryStream,
logs:DescribeResourcePolicies,
iam:CreateServiceLinkedRole,
verified-access:AllowVerifiedAccess
```

### Read
```json
ec2:DescribeVerifiedAccessInstances,
ec2:DescribeVerifiedAccessInstanceLoggingConfigurations,
ec2:DescribeTags,
logs:GetLogDelivery,
logs:ListLogDeliveries
```

### Update
```json
ec2:ModifyVerifiedAccessInstance,
ec2:ModifyVerifiedAccessInstanceLoggingConfiguration,
ec2:DescribeVerifiedAccessInstances,
ec2:DescribeVerifiedAccessInstanceLoggingConfigurations,
ec2:DescribeTags,
ec2:AttachVerifiedAccessTrustProvider,
ec2:DetachVerifiedAccessTrustProvider,
ec2:DeleteTags,
ec2:CreateTags,
ec2:DescribeTags,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:PutDestination,
logs:PutLogEvents,
logs:DescribeLogStreams,
s3:listBuckets,
s3:PutObject,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
logs:DescribeLogGroups,
logs:PutResourcePolicy,
firehose:TagDeliveryStream,
iam:CreateServiceLinkedRole,
logs:DescribeResourcePolicies
```

### Delete
```json
ec2:DeleteVerifiedAccessInstance,
ec2:DeleteTags,
ec2:DescribeVerifiedAccessInstances,
ec2:DescribeVerifiedAccessInstanceLoggingConfigurations,
ec2:DetachVerifiedAccessTrustProvider,
ec2:GetVerifiedAccessGroupPolicy,
ec2:DescribeTags,
logs:ListLogDeliveries,
logs:GetLogDelivery,
logs:DeleteLogDelivery
```

### List
```json
ec2:DescribeVerifiedAccessInstances,
ec2:DescribeTags,
logs:ListLogDeliveries,
logs:GetLogDelivery
```


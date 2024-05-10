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


Used to retrieve a list of <code>verified_access_instances</code> in a region or to create or delete a <code>verified_access_instances</code> resource, use <code>verified_access_instance</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_access_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::VerifiedAccessInstance resource creates an AWS EC2 Verified Access Instance.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.verified_access_instances" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="verified_access_instance_id" /></td><td><code>string</code></td><td>The ID of the AWS Verified Access instance.</td></tr>
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
verified_access_instance_id
FROM aws.ec2.verified_access_instances
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>verified_access_instance</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- verified_access_instance.iql (required properties only)
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
-- verified_access_instance.iql (all properties)
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

## `DELETE` Example

```sql
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


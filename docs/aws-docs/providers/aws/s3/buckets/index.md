---
title: buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets
  - s3
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


Used to retrieve a list of <code>buckets</code> in a region or to create or delete a <code>buckets</code> resource, use <code>bucket</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::S3::Bucket`` resource creates an Amazon S3 bucket in the same AWS Region where you create the AWS CloudFormation stack.&lt;br&#x2F;&gt; To control how AWS CloudFormation handles the bucket when the stack is deleted, you can set a deletion policy for your bucket. You can choose to *retain* the bucket or to *delete* the bucket. For more information, see &#91;DeletionPolicy Attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-attribute-deletionpolicy.html).&lt;br&#x2F;&gt;  You can only delete empty buckets. Deletion fails for buckets that have contents.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.buckets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td>A name for the bucket. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-) and must follow &#91;Amazon S3 bucket restrictions and limitations&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;BucketRestrictions.html). For more information, see &#91;Rules for naming Amazon S3 buckets&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;BucketRestrictions.html#bucketnamingrules) in the *Amazon S3 User Guide*. &lt;br&#x2F;&gt;  If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.</td></tr>
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
bucket_name
FROM aws.s3.buckets
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>bucket</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- bucket.iql (required properties only)
INSERT INTO aws.s3.buckets (
 BucketName,
 region
)
SELECT 
'{{ BucketName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- bucket.iql (all properties)
INSERT INTO aws.s3.buckets (
 AccelerateConfiguration,
 AccessControl,
 AnalyticsConfigurations,
 BucketEncryption,
 BucketName,
 CorsConfiguration,
 IntelligentTieringConfigurations,
 InventoryConfigurations,
 LifecycleConfiguration,
 LoggingConfiguration,
 MetricsConfigurations,
 NotificationConfiguration,
 ObjectLockConfiguration,
 ObjectLockEnabled,
 OwnershipControls,
 PublicAccessBlockConfiguration,
 ReplicationConfiguration,
 Tags,
 VersioningConfiguration,
 WebsiteConfiguration,
 region
)
SELECT 
 '{{ AccelerateConfiguration }}',
 '{{ AccessControl }}',
 '{{ AnalyticsConfigurations }}',
 '{{ BucketEncryption }}',
 '{{ BucketName }}',
 '{{ CorsConfiguration }}',
 '{{ IntelligentTieringConfigurations }}',
 '{{ InventoryConfigurations }}',
 '{{ LifecycleConfiguration }}',
 '{{ LoggingConfiguration }}',
 '{{ MetricsConfigurations }}',
 '{{ NotificationConfiguration }}',
 '{{ ObjectLockConfiguration }}',
 '{{ ObjectLockEnabled }}',
 '{{ OwnershipControls }}',
 '{{ PublicAccessBlockConfiguration }}',
 '{{ ReplicationConfiguration }}',
 '{{ Tags }}',
 '{{ VersioningConfiguration }}',
 '{{ WebsiteConfiguration }}',
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
  - name: bucket
    props:
      - name: AccelerateConfiguration
        value:
          AccelerationStatus: '{{ AccelerationStatus }}'
      - name: AccessControl
        value: '{{ AccessControl }}'
      - name: AnalyticsConfigurations
        value:
          - TagFilters:
              - Value: '{{ Value }}'
                Key: '{{ Key }}'
            StorageClassAnalysis:
              DataExport:
                S3BucketDestination:
                  OutputSchemaVersion: '{{ OutputSchemaVersion }}'
                  Format: '{{ Format }}'
                  AccountId: '{{ AccountId }}'
                  Arn: '{{ Arn }}'
                  Prefix: '{{ Prefix }}'
                  Encryption: {}
                CloudWatchMetrics:
                  IsEnabled: '{{ IsEnabled }}'
            Id: '{{ Id }}'
            Prefix: '{{ Prefix }}'
      - name: BucketEncryption
        value:
          ServerSideEncryptionConfiguration:
            - BucketKeyEnabled: '{{ BucketKeyEnabled }}'
              ServerSideEncryptionByDefault:
                KMSMasterKeyID: '{{ KMSMasterKeyID }}'
                SSEAlgorithm: '{{ SSEAlgorithm }}'
      - name: BucketName
        value: '{{ BucketName }}'
      - name: CorsConfiguration
        value:
          CorsRules:
            - AllowedHeaders:
                - '{{ AllowedHeaders[0] }}'
              AllowedMethods:
                - '{{ AllowedMethods[0] }}'
              AllowedOrigins:
                - '{{ AllowedOrigins[0] }}'
              ExposedHeaders:
                - '{{ ExposedHeaders[0] }}'
              Id: '{{ Id }}'
              MaxAge: '{{ MaxAge }}'
      - name: IntelligentTieringConfigurations
        value:
          - Id: '{{ Id }}'
            Prefix: '{{ Prefix }}'
            Status: '{{ Status }}'
            TagFilters:
              - null
            Tierings:
              - AccessTier: '{{ AccessTier }}'
                Days: '{{ Days }}'
      - name: InventoryConfigurations
        value:
          - Destination:
              BucketArn: '{{ BucketArn }}'
              BucketAccountId: '{{ BucketAccountId }}'
              Format: '{{ Format }}'
              Prefix: '{{ Prefix }}'
            Enabled: '{{ Enabled }}'
            Id: '{{ Id }}'
            IncludedObjectVersions: '{{ IncludedObjectVersions }}'
            OptionalFields:
              - '{{ OptionalFields[0] }}'
            Prefix: '{{ Prefix }}'
            ScheduleFrequency: '{{ ScheduleFrequency }}'
      - name: LifecycleConfiguration
        value:
          Rules:
            - AbortIncompleteMultipartUpload:
                DaysAfterInitiation: '{{ DaysAfterInitiation }}'
              ExpirationDate: '{{ ExpirationDate }}'
              ExpirationInDays: '{{ ExpirationInDays }}'
              ExpiredObjectDeleteMarker: '{{ ExpiredObjectDeleteMarker }}'
              Id: '{{ Id }}'
              NoncurrentVersionExpirationInDays: '{{ NoncurrentVersionExpirationInDays }}'
              NoncurrentVersionExpiration:
                NoncurrentDays: '{{ NoncurrentDays }}'
                NewerNoncurrentVersions: '{{ NewerNoncurrentVersions }}'
              NoncurrentVersionTransition:
                StorageClass: '{{ StorageClass }}'
                TransitionInDays: '{{ TransitionInDays }}'
                NewerNoncurrentVersions: '{{ NewerNoncurrentVersions }}'
              NoncurrentVersionTransitions:
                - null
              Prefix: '{{ Prefix }}'
              Status: '{{ Status }}'
              TagFilters:
                - null
              ObjectSizeGreaterThan: '{{ ObjectSizeGreaterThan }}'
              ObjectSizeLessThan: '{{ ObjectSizeLessThan }}'
              Transition:
                StorageClass: '{{ StorageClass }}'
                TransitionDate: null
                TransitionInDays: '{{ TransitionInDays }}'
              Transitions:
                - null
      - name: LoggingConfiguration
        value:
          DestinationBucketName: '{{ DestinationBucketName }}'
          LogFilePrefix: '{{ LogFilePrefix }}'
          TargetObjectKeyFormat: {}
      - name: MetricsConfigurations
        value:
          - AccessPointArn: '{{ AccessPointArn }}'
            Id: '{{ Id }}'
            Prefix: '{{ Prefix }}'
            TagFilters:
              - null
      - name: NotificationConfiguration
        value:
          EventBridgeConfiguration:
            EventBridgeEnabled: '{{ EventBridgeEnabled }}'
          LambdaConfigurations:
            - Event: '{{ Event }}'
              Filter:
                S3Key:
                  Rules:
                    - Name: '{{ Name }}'
                      Value: '{{ Value }}'
              Function: '{{ Function }}'
          QueueConfigurations:
            - Event: '{{ Event }}'
              Filter: null
              Queue: '{{ Queue }}'
          TopicConfigurations:
            - Event: '{{ Event }}'
              Filter: null
              Topic: '{{ Topic }}'
      - name: ObjectLockConfiguration
        value:
          ObjectLockEnabled: '{{ ObjectLockEnabled }}'
          Rule:
            DefaultRetention:
              Years: '{{ Years }}'
              Days: '{{ Days }}'
              Mode: '{{ Mode }}'
      - name: ObjectLockEnabled
        value: '{{ ObjectLockEnabled }}'
      - name: OwnershipControls
        value:
          Rules:
            - ObjectOwnership: '{{ ObjectOwnership }}'
      - name: PublicAccessBlockConfiguration
        value:
          BlockPublicAcls: '{{ BlockPublicAcls }}'
          IgnorePublicAcls: '{{ IgnorePublicAcls }}'
          BlockPublicPolicy: '{{ BlockPublicPolicy }}'
          RestrictPublicBuckets: '{{ RestrictPublicBuckets }}'
      - name: ReplicationConfiguration
        value:
          Role: '{{ Role }}'
          Rules:
            - DeleteMarkerReplication:
                Status: '{{ Status }}'
              Destination:
                AccessControlTranslation:
                  Owner: '{{ Owner }}'
                Account: '{{ Account }}'
                Bucket: '{{ Bucket }}'
                EncryptionConfiguration:
                  ReplicaKmsKeyID: '{{ ReplicaKmsKeyID }}'
                Metrics:
                  EventThreshold:
                    Minutes: '{{ Minutes }}'
                  Status: '{{ Status }}'
                ReplicationTime:
                  Status: '{{ Status }}'
                  Time: null
                StorageClass: '{{ StorageClass }}'
              Filter:
                And:
                  Prefix: '{{ Prefix }}'
                  TagFilters:
                    - null
                Prefix: '{{ Prefix }}'
                TagFilter: null
              Id: '{{ Id }}'
              Prefix: '{{ Prefix }}'
              Priority: '{{ Priority }}'
              SourceSelectionCriteria:
                ReplicaModifications:
                  Status: '{{ Status }}'
                SseKmsEncryptedObjects:
                  Status: '{{ Status }}'
              Status: '{{ Status }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: VersioningConfiguration
        value:
          Status: '{{ Status }}'
      - name: WebsiteConfiguration
        value:
          ErrorDocument: '{{ ErrorDocument }}'
          IndexDocument: '{{ IndexDocument }}'
          RoutingRules:
            - RedirectRule:
                HostName: '{{ HostName }}'
                HttpRedirectCode: '{{ HttpRedirectCode }}'
                Protocol: '{{ Protocol }}'
                ReplaceKeyPrefixWith: '{{ ReplaceKeyPrefixWith }}'
                ReplaceKeyWith: '{{ ReplaceKeyWith }}'
              RoutingRuleCondition:
                KeyPrefixEquals: '{{ KeyPrefixEquals }}'
                HttpErrorCodeReturnedEquals: '{{ HttpErrorCodeReturnedEquals }}'
          RedirectAllRequestsTo:
            HostName: '{{ HostName }}'
            Protocol: '{{ Protocol }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.s3.buckets
WHERE data__Identifier = '<BucketName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>buckets</code> resource, the following permissions are required:

### Create
```json
s3:CreateBucket,
s3:PutBucketTagging,
s3:PutAnalyticsConfiguration,
s3:PutEncryptionConfiguration,
s3:PutBucketCORS,
s3:PutInventoryConfiguration,
s3:PutLifecycleConfiguration,
s3:PutMetricsConfiguration,
s3:PutBucketNotification,
s3:PutBucketReplication,
s3:PutBucketWebsite,
s3:PutAccelerateConfiguration,
s3:PutBucketPublicAccessBlock,
s3:PutReplicationConfiguration,
s3:PutObjectAcl,
s3:PutBucketObjectLockConfiguration,
s3:GetBucketAcl,
s3:ListBucket,
iam:PassRole,
s3:DeleteObject,
s3:PutBucketLogging,
s3:PutBucketVersioning,
s3:PutObjectLockConfiguration,
s3:PutBucketOwnershipControls,
s3:PutIntelligentTieringConfiguration
```

### Delete
```json
s3:DeleteBucket,
s3:ListBucket
```

### List
```json
s3:ListAllMyBuckets
```


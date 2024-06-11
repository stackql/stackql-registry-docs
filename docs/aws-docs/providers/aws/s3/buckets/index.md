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

Creates, updates, deletes or gets a <code>bucket</code> resource or lists <code>buckets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::S3::Bucket</code> resource creates an Amazon S3 bucket in the same AWS Region where you create the AWS CloudFormation stack.<br/> To control how AWS CloudFormation handles the bucket when the stack is deleted, you can set a deletion policy for your bucket. You can choose to *retain* the bucket or to *delete* the bucket. For more information, see &#91;DeletionPolicy Attribute&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).<br/>  You can only delete empty buckets. Deletion fails for buckets that have contents.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.buckets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="accelerate_configuration" /></td><td><code>object</code></td><td>Configures the transfer acceleration state for an Amazon S3 bucket. For more information, see &#91;Amazon S3 Transfer Acceleration&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html) in the *Amazon S3 User Guide*.</td></tr>
<tr><td><CopyableCode code="access_control" /></td><td><code>string</code></td><td>This is a legacy property, and it is not recommended for most use cases. A majority of modern use cases in Amazon S3 no longer require the use of ACLs, and we recommend that you keep ACLs disabled. For more information, see &#91;Controlling object ownership&#93;(https://docs.aws.amazon.com//AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon S3 User Guide*.<br/>  A canned access control list (ACL) that grants predefined permissions to the bucket. For more information about canned ACLs, see &#91;Canned ACL&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) in the *Amazon S3 User Guide*.<br/>  S3 buckets are created with ACLs disabled by default. Therefore, unless you explicitly set the &#91;AWS::S3::OwnershipControls&#93;(https://docs.aws.amazon.com//AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ownershipcontrols.html) property to enable ACLs, your resource will fail to deploy with any value other than Private. Use cases requiring ACLs are uncommon.<br/>  The majority of access control configurations can be successfully and more easily achieved with bucket policies. For more information, see &#91;AWS::S3::BucketPolicy&#93;(https://docs.aws.amazon.com//AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html). For examples of common policy configurations, including S3 Server Access Logs buckets and more, see &#91;Bucket policy examples&#93;(https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html) in the *Amazon S3 User Guide*.</td></tr>
<tr><td><CopyableCode code="analytics_configurations" /></td><td><code>array</code></td><td>Specifies the configuration and any analyses for the analytics filter of an Amazon S3 bucket.</td></tr>
<tr><td><CopyableCode code="bucket_encryption" /></td><td><code>object</code></td><td>Specifies default encryption for a bucket using server-side encryption with Amazon S3-managed keys (SSE-S3), AWS KMS-managed keys (SSE-KMS), or dual-layer server-side encryption with KMS-managed keys (DSSE-KMS). For information about the Amazon S3 default encryption feature, see &#91;Amazon S3 Default Encryption for S3 Buckets&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) in the *Amazon S3 User Guide*.</td></tr>
<tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td>A name for the bucket. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-) and must follow &#91;Amazon S3 bucket restrictions and limitations&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html). For more information, see &#91;Rules for naming Amazon S3 buckets&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html#bucketnamingrules) in the *Amazon S3 User Guide*. <br/>  If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="cors_configuration" /></td><td><code>object</code></td><td>Describes the cross-origin access configuration for objects in an Amazon S3 bucket. For more information, see &#91;Enabling Cross-Origin Resource Sharing&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) in the *Amazon S3 User Guide*.</td></tr>
<tr><td><CopyableCode code="intelligent_tiering_configurations" /></td><td><code>array</code></td><td>Defines how Amazon S3 handles Intelligent-Tiering storage.</td></tr>
<tr><td><CopyableCode code="inventory_configurations" /></td><td><code>array</code></td><td>Specifies the inventory configuration for an Amazon S3 bucket. For more information, see &#91;GET Bucket inventory&#93;(https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketGETInventoryConfig.html) in the *Amazon S3 API Reference*.</td></tr>
<tr><td><CopyableCode code="lifecycle_configuration" /></td><td><code>object</code></td><td>Specifies the lifecycle configuration for objects in an Amazon S3 bucket. For more information, see &#91;Object Lifecycle Management&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) in the *Amazon S3 User Guide*.</td></tr>
<tr><td><CopyableCode code="logging_configuration" /></td><td><code>object</code></td><td>Settings that define where logs are stored.</td></tr>
<tr><td><CopyableCode code="metrics_configurations" /></td><td><code>array</code></td><td>Specifies a metrics configuration for the CloudWatch request metrics (specified by the metrics configuration ID) from an Amazon S3 bucket. If you're updating an existing metrics configuration, note that this is a full replacement of the existing metrics configuration. If you don't include the elements you want to keep, they are erased. For more information, see &#91;PutBucketMetricsConfiguration&#93;(https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTMetricConfiguration.html).</td></tr>
<tr><td><CopyableCode code="notification_configuration" /></td><td><code>object</code></td><td>Configuration that defines how Amazon S3 handles bucket notifications.</td></tr>
<tr><td><CopyableCode code="object_lock_configuration" /></td><td><code>object</code></td><td>This operation is not supported by directory buckets.<br/>  Places an Object Lock configuration on the specified bucket. The rule specified in the Object Lock configuration will be applied by default to every new object placed in the specified bucket. For more information, see &#91;Locking Objects&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html). <br/>   +  The <code>DefaultRetention</code> settings require both a mode and a period.<br/>  +  The <code>DefaultRetention</code> period can be either <code>Days</code> or <code>Years</code> but you must select one. You cannot specify <code>Days</code> and <code>Years</code> at the same time.<br/>  +  You can enable Object Lock for new or existing buckets. For more information, see &#91;Configuring Object Lock&#93;(https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-configure.html).</td></tr>
<tr><td><CopyableCode code="object_lock_enabled" /></td><td><code>boolean</code></td><td>Indicates whether this bucket has an Object Lock configuration enabled. Enable <code>ObjectLockEnabled</code> when you apply <code>ObjectLockConfiguration</code> to a bucket.</td></tr>
<tr><td><CopyableCode code="ownership_controls" /></td><td><code>object</code></td><td>Configuration that defines how Amazon S3 handles Object Ownership rules.</td></tr>
<tr><td><CopyableCode code="public_access_block_configuration" /></td><td><code>object</code></td><td>Configuration that defines how Amazon S3 handles public access.</td></tr>
<tr><td><CopyableCode code="replication_configuration" /></td><td><code>object</code></td><td>Configuration for replicating objects in an S3 bucket. To enable replication, you must also enable versioning by using the <code>VersioningConfiguration</code> property.<br/> Amazon S3 can store replicated objects in a single destination bucket or multiple destination buckets. The destination bucket or buckets must already exist.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this S3 bucket.</td></tr>
<tr><td><CopyableCode code="versioning_configuration" /></td><td><code>object</code></td><td>Enables multiple versions of all objects in this bucket. You might enable versioning to prevent objects from being deleted or overwritten by mistake or to archive objects so that you can retrieve previous versions of them.</td></tr>
<tr><td><CopyableCode code="website_configuration" /></td><td><code>object</code></td><td>Information used to configure the bucket as a static website. For more information, see &#91;Hosting Websites on Amazon S3&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html).</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>The Amazon Resource Name (ARN) of the specified resource.</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dual_stack_domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="regional_domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="website_url" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="BucketName, region" /></td>
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
List all <code>buckets</code> in a region.
```sql
SELECT
region,
bucket_name
FROM aws.s3.buckets
WHERE region = 'us-east-1';
```
Gets all properties from a <code>bucket</code>.
```sql
SELECT
region,
accelerate_configuration,
access_control,
analytics_configurations,
bucket_encryption,
bucket_name,
cors_configuration,
intelligent_tiering_configurations,
inventory_configurations,
lifecycle_configuration,
logging_configuration,
metrics_configurations,
notification_configuration,
object_lock_configuration,
object_lock_enabled,
ownership_controls,
public_access_block_configuration,
replication_configuration,
tags,
versioning_configuration,
website_configuration,
arn,
domain_name,
dual_stack_domain_name,
regional_domain_name,
website_url
FROM aws.s3.buckets
WHERE region = 'us-east-1' AND data__Identifier = '<BucketName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bucket</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
s3:GetAccelerateConfiguration,
s3:GetLifecycleConfiguration,
s3:GetBucketPublicAccessBlock,
s3:GetAnalyticsConfiguration,
s3:GetBucketCORS,
s3:GetEncryptionConfiguration,
s3:GetInventoryConfiguration,
s3:GetBucketLogging,
s3:GetMetricsConfiguration,
s3:GetBucketNotification,
s3:GetBucketVersioning,
s3:GetReplicationConfiguration,
S3:GetBucketWebsite,
s3:GetBucketPublicAccessBlock,
s3:GetBucketObjectLockConfiguration,
s3:GetBucketTagging,
s3:GetBucketOwnershipControls,
s3:GetIntelligentTieringConfiguration,
s3:ListBucket
```

### Update
```json
s3:PutBucketAcl,
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
s3:PutBucketOwnershipControls,
s3:PutIntelligentTieringConfiguration,
s3:DeleteBucketWebsite,
s3:PutBucketLogging,
s3:PutBucketVersioning,
s3:PutObjectLockConfiguration,
s3:PutBucketObjectLockConfiguration,
s3:DeleteBucketAnalyticsConfiguration,
s3:DeleteBucketCors,
s3:DeleteBucketMetricsConfiguration,
s3:DeleteBucketEncryption,
s3:DeleteBucketLifecycle,
s3:DeleteBucketReplication,
iam:PassRole,
s3:ListBucket
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


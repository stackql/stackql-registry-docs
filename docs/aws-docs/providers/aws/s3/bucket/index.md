---
title: bucket
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket
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
Gets or operates on an individual <code>bucket</code> resource, use <code>buckets</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bucket</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::S3::Bucket`` resource creates an Amazon S3 bucket in the same AWS Region where you create the AWS CloudFormation stack.&lt;br&#x2F;&gt; To control how AWS CloudFormation handles the bucket when the stack is deleted, you can set a deletion policy for your bucket. You can choose to *retain* the bucket or to *delete* the bucket. For more information, see &#91;DeletionPolicy Attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-attribute-deletionpolicy.html).&lt;br&#x2F;&gt;  You can only delete empty buckets. Deletion fails for buckets that have contents.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.bucket</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>accelerate_configuration</code></td><td><code>object</code></td><td>Configures the transfer acceleration state for an Amazon S3 bucket. For more information, see &#91;Amazon S3 Transfer Acceleration&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;transfer-acceleration.html) in the *Amazon S3 User Guide*.</td></tr>
<tr><td><code>access_control</code></td><td><code>string</code></td><td>This is a legacy property, and it is not recommended for most use cases. A majority of modern use cases in Amazon S3 no longer require the use of ACLs, and we recommend that you keep ACLs disabled. For more information, see &#91;Controlling object ownership&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;&#x2F;AmazonS3&#x2F;latest&#x2F;userguide&#x2F;about-object-ownership.html) in the *Amazon S3 User Guide*.&lt;br&#x2F;&gt;  A canned access control list (ACL) that grants predefined permissions to the bucket. For more information about canned ACLs, see &#91;Canned ACL&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;acl-overview.html#canned-acl) in the *Amazon S3 User Guide*.&lt;br&#x2F;&gt;  S3 buckets are created with ACLs disabled by default. Therefore, unless you explicitly set the &#91;AWS::S3::OwnershipControls&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-s3-bucket-ownershipcontrols.html) property to enable ACLs, your resource will fail to deploy with any value other than Private. Use cases requiring ACLs are uncommon.&lt;br&#x2F;&gt;  The majority of access control configurations can be successfully and more easily achieved with bucket policies. For more information, see &#91;AWS::S3::BucketPolicy&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-s3-policy.html). For examples of common policy configurations, including S3 Server Access Logs buckets and more, see &#91;Bucket policy examples&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;userguide&#x2F;example-bucket-policies.html) in the *Amazon S3 User Guide*.</td></tr>
<tr><td><code>analytics_configurations</code></td><td><code>array</code></td><td>Specifies the configuration and any analyses for the analytics filter of an Amazon S3 bucket.</td></tr>
<tr><td><code>bucket_encryption</code></td><td><code>object</code></td><td>Specifies default encryption for a bucket using server-side encryption with Amazon S3-managed keys (SSE-S3), AWS KMS-managed keys (SSE-KMS), or dual-layer server-side encryption with KMS-managed keys (DSSE-KMS). For information about the Amazon S3 default encryption feature, see &#91;Amazon S3 Default Encryption for S3 Buckets&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;bucket-encryption.html) in the *Amazon S3 User Guide*.</td></tr>
<tr><td><code>bucket_name</code></td><td><code>string</code></td><td>A name for the bucket. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-) and must follow &#91;Amazon S3 bucket restrictions and limitations&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;BucketRestrictions.html). For more information, see &#91;Rules for naming Amazon S3 buckets&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;BucketRestrictions.html#bucketnamingrules) in the *Amazon S3 User Guide*. &lt;br&#x2F;&gt;  If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.</td></tr>
<tr><td><code>cors_configuration</code></td><td><code>object</code></td><td>Describes the cross-origin access configuration for objects in an Amazon S3 bucket. For more information, see &#91;Enabling Cross-Origin Resource Sharing&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;cors.html) in the *Amazon S3 User Guide*.</td></tr>
<tr><td><code>intelligent_tiering_configurations</code></td><td><code>array</code></td><td>Defines how Amazon S3 handles Intelligent-Tiering storage.</td></tr>
<tr><td><code>inventory_configurations</code></td><td><code>array</code></td><td>Specifies the inventory configuration for an Amazon S3 bucket. For more information, see &#91;GET Bucket inventory&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;API&#x2F;RESTBucketGETInventoryConfig.html) in the *Amazon S3 API Reference*.</td></tr>
<tr><td><code>lifecycle_configuration</code></td><td><code>object</code></td><td>Specifies the lifecycle configuration for objects in an Amazon S3 bucket. For more information, see &#91;Object Lifecycle Management&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;object-lifecycle-mgmt.html) in the *Amazon S3 User Guide*.</td></tr>
<tr><td><code>logging_configuration</code></td><td><code>object</code></td><td>Settings that define where logs are stored.</td></tr>
<tr><td><code>metrics_configurations</code></td><td><code>array</code></td><td>Specifies a metrics configuration for the CloudWatch request metrics (specified by the metrics configuration ID) from an Amazon S3 bucket. If you're updating an existing metrics configuration, note that this is a full replacement of the existing metrics configuration. If you don't include the elements you want to keep, they are erased. For more information, see &#91;PutBucketMetricsConfiguration&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;API&#x2F;RESTBucketPUTMetricConfiguration.html).</td></tr>
<tr><td><code>notification_configuration</code></td><td><code>object</code></td><td>Configuration that defines how Amazon S3 handles bucket notifications.</td></tr>
<tr><td><code>object_lock_configuration</code></td><td><code>object</code></td><td>This operation is not supported by directory buckets.&lt;br&#x2F;&gt;  Places an Object Lock configuration on the specified bucket. The rule specified in the Object Lock configuration will be applied by default to every new object placed in the specified bucket. For more information, see &#91;Locking Objects&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;object-lock.html). &lt;br&#x2F;&gt;   +  The ``DefaultRetention`` settings require both a mode and a period.&lt;br&#x2F;&gt;  +  The ``DefaultRetention`` period can be either ``Days`` or ``Years`` but you must select one. You cannot specify ``Days`` and ``Years`` at the same time.&lt;br&#x2F;&gt;  +  You can enable Object Lock for new or existing buckets. For more information, see &#91;Configuring Object Lock&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;userguide&#x2F;object-lock-configure.html).</td></tr>
<tr><td><code>object_lock_enabled</code></td><td><code>boolean</code></td><td>Indicates whether this bucket has an Object Lock configuration enabled. Enable ``ObjectLockEnabled`` when you apply ``ObjectLockConfiguration`` to a bucket.</td></tr>
<tr><td><code>ownership_controls</code></td><td><code>object</code></td><td>Configuration that defines how Amazon S3 handles Object Ownership rules.</td></tr>
<tr><td><code>public_access_block_configuration</code></td><td><code>object</code></td><td>Configuration that defines how Amazon S3 handles public access.</td></tr>
<tr><td><code>replication_configuration</code></td><td><code>object</code></td><td>Configuration for replicating objects in an S3 bucket. To enable replication, you must also enable versioning by using the ``VersioningConfiguration`` property.&lt;br&#x2F;&gt; Amazon S3 can store replicated objects in a single destination bucket or multiple destination buckets. The destination bucket or buckets must already exist.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this S3 bucket.</td></tr>
<tr><td><code>versioning_configuration</code></td><td><code>object</code></td><td>Enables multiple versions of all objects in this bucket. You might enable versioning to prevent objects from being deleted or overwritten by mistake or to archive objects so that you can retrieve previous versions of them.</td></tr>
<tr><td><code>website_configuration</code></td><td><code>object</code></td><td>Information used to configure the bucket as a static website. For more information, see &#91;Hosting Websites on Amazon S3&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;WebsiteHosting.html).</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dual_stack_domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>regional_domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>website_url</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.s3.bucket
WHERE data__Identifier = '<BucketName>';
```

## Permissions

To operate on the <code>bucket</code> resource, the following permissions are required:

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


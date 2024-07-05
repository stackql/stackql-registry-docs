---
title: bucket_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_tags
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

Expands all tag keys and values for <code>buckets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bucket_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::S3::Bucket</code> resource creates an Amazon S3 bucket in the same AWS Region where you create the AWS CloudFormation stack.<br />To control how AWS CloudFormation handles the bucket when the stack is deleted, you can set a deletion policy for your bucket. You can choose to *retain* the bucket or to *delete* the bucket. For more information, see &#91;DeletionPolicy Attribute&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).<br />You can only delete empty buckets. Deletion fails for buckets that have contents.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.bucket_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="accelerate_configuration" /></td><td><code>object</code></td><td>Configures the transfer acceleration state for an Amazon S3 bucket. For more information, see &#91;Amazon S3 Transfer Acceleration&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html) in the *Amazon S3 User Guide*.</td></tr>
<tr><td><CopyableCode code="access_control" /></td><td><code>string</code></td><td>This is a legacy property, and it is not recommended for most use cases. A majority of modern use cases in Amazon S3 no longer require the use of ACLs, and we recommend that you keep ACLs disabled. For more information, see &#91;Controlling object ownership&#93;(https://docs.aws.amazon.com//AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon S3 User Guide*.<br />A canned access control list (ACL) that grants predefined permissions to the bucket. For more information about canned ACLs, see &#91;Canned ACL&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) in the *Amazon S3 User Guide*.<br />S3 buckets are created with ACLs disabled by default. Therefore, unless you explicitly set the &#91;AWS::S3::OwnershipControls&#93;(https://docs.aws.amazon.com//AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-ownershipcontrols.html) property to enable ACLs, your resource will fail to deploy with any value other than Private. Use cases requiring ACLs are uncommon.<br />The majority of access control configurations can be successfully and more easily achieved with bucket policies. For more information, see &#91;AWS::S3::BucketPolicy&#93;(https://docs.aws.amazon.com//AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html). For examples of common policy configurations, including S3 Server Access Logs buckets and more, see &#91;Bucket policy examples&#93;(https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html) in the *Amazon S3 User Guide*.</td></tr>
<tr><td><CopyableCode code="analytics_configurations" /></td><td><code>array</code></td><td>Specifies the configuration and any analyses for the analytics filter of an Amazon S3 bucket.</td></tr>
<tr><td><CopyableCode code="bucket_encryption" /></td><td><code>object</code></td><td>Specifies default encryption for a bucket using server-side encryption with Amazon S3-managed keys (SSE-S3), AWS KMS-managed keys (SSE-KMS), or dual-layer server-side encryption with KMS-managed keys (DSSE-KMS). For information about the Amazon S3 default encryption feature, see &#91;Amazon S3 Default Encryption for S3 Buckets&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) in the *Amazon S3 User Guide*.</td></tr>
<tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td>A name for the bucket. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. The bucket name must contain only lowercase letters, numbers, periods (.), and dashes (-) and must follow &#91;Amazon S3 bucket restrictions and limitations&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html). For more information, see &#91;Rules for naming Amazon S3 buckets&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html#bucketnamingrules) in the *Amazon S3 User Guide*. <br />If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="cors_configuration" /></td><td><code>object</code></td><td>Describes the cross-origin access configuration for objects in an Amazon S3 bucket. For more information, see &#91;Enabling Cross-Origin Resource Sharing&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html) in the *Amazon S3 User Guide*.</td></tr>
<tr><td><CopyableCode code="intelligent_tiering_configurations" /></td><td><code>array</code></td><td>Defines how Amazon S3 handles Intelligent-Tiering storage.</td></tr>
<tr><td><CopyableCode code="inventory_configurations" /></td><td><code>array</code></td><td>Specifies the inventory configuration for an Amazon S3 bucket. For more information, see &#91;GET Bucket inventory&#93;(https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketGETInventoryConfig.html) in the *Amazon S3 API Reference*.</td></tr>
<tr><td><CopyableCode code="lifecycle_configuration" /></td><td><code>object</code></td><td>Specifies the lifecycle configuration for objects in an Amazon S3 bucket. For more information, see &#91;Object Lifecycle Management&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) in the *Amazon S3 User Guide*.</td></tr>
<tr><td><CopyableCode code="logging_configuration" /></td><td><code>object</code></td><td>Settings that define where logs are stored.</td></tr>
<tr><td><CopyableCode code="metrics_configurations" /></td><td><code>array</code></td><td>Specifies a metrics configuration for the CloudWatch request metrics (specified by the metrics configuration ID) from an Amazon S3 bucket. If you're updating an existing metrics configuration, note that this is a full replacement of the existing metrics configuration. If you don't include the elements you want to keep, they are erased. For more information, see &#91;PutBucketMetricsConfiguration&#93;(https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTMetricConfiguration.html).</td></tr>
<tr><td><CopyableCode code="notification_configuration" /></td><td><code>object</code></td><td>Configuration that defines how Amazon S3 handles bucket notifications.</td></tr>
<tr><td><CopyableCode code="object_lock_configuration" /></td><td><code>object</code></td><td>This operation is not supported by directory buckets.<br />Places an Object Lock configuration on the specified bucket. The rule specified in the Object Lock configuration will be applied by default to every new object placed in the specified bucket. For more information, see &#91;Locking Objects&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html). <br />+ The <code>DefaultRetention</code> settings require both a mode and a period.<br />+ The <code>DefaultRetention</code> period can be either <code>Days</code> or <code>Years</code> but you must select one. You cannot specify <code>Days</code> and <code>Years</code> at the same time.<br />+ You can enable Object Lock for new or existing buckets. For more information, see &#91;Configuring Object Lock&#93;(https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-configure.html).</td></tr>
<tr><td><CopyableCode code="object_lock_enabled" /></td><td><code>boolean</code></td><td>Indicates whether this bucket has an Object Lock configuration enabled. Enable <code>ObjectLockEnabled</code> when you apply <code>ObjectLockConfiguration</code> to a bucket.</td></tr>
<tr><td><CopyableCode code="ownership_controls" /></td><td><code>object</code></td><td>Configuration that defines how Amazon S3 handles Object Ownership rules.</td></tr>
<tr><td><CopyableCode code="public_access_block_configuration" /></td><td><code>object</code></td><td>Configuration that defines how Amazon S3 handles public access.</td></tr>
<tr><td><CopyableCode code="replication_configuration" /></td><td><code>object</code></td><td>Configuration for replicating objects in an S3 bucket. To enable replication, you must also enable versioning by using the <code>VersioningConfiguration</code> property.<br />Amazon S3 can store replicated objects in a single destination bucket or multiple destination buckets. The destination bucket or buckets must already exist.</td></tr>
<tr><td><CopyableCode code="versioning_configuration" /></td><td><code>object</code></td><td>Enables multiple versions of all objects in this bucket. You might enable versioning to prevent objects from being deleted or overwritten by mistake or to archive objects so that you can retrieve previous versions of them.</td></tr>
<tr><td><CopyableCode code="website_configuration" /></td><td><code>object</code></td><td>Information used to configure the bucket as a static website. For more information, see &#91;Hosting Websites on Amazon S3&#93;(https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html).</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified resource.</td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dual_stack_domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="regional_domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="website_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>buckets</code> in a region.
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
versioning_configuration,
website_configuration,
arn,
domain_name,
dual_stack_domain_name,
regional_domain_name,
website_url,
tag_key,
tag_value
FROM aws.s3.bucket_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>bucket_tags</code> resource, see <a href="/providers/aws/s3/buckets/#permissions"><code>buckets</code></a>



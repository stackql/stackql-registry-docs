---
title: bucket_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_policies
  - s3_api
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bucket_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3_api.bucket_policies" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="bucket_policies_Get" /> | `SELECT` | <CopyableCode code="bucket, region" /> | &lt;p&gt;Returns the policy of a specified bucket. If you are using an identity other than the root user of the Amazon Web Services account that owns the bucket, the calling identity must have the &lt;code&gt;GetBucketPolicy&lt;/code&gt; permissions on the specified bucket and belong to the bucket owner's account in order to use this operation.&lt;/p&gt; &lt;p&gt;If you don't have &lt;code&gt;GetBucketPolicy&lt;/code&gt; permissions, Amazon S3 returns a &lt;code&gt;403 Access Denied&lt;/code&gt; error. If you have the correct permissions, but you're not using an identity that belongs to the bucket owner's account, Amazon S3 returns a &lt;code&gt;405 Method Not Allowed&lt;/code&gt; error.&lt;/p&gt; &lt;important&gt; &lt;p&gt;As a security precaution, the root user of the Amazon Web Services account that owns a bucket can always use this operation, even if the policy explicitly denies the root user the ability to perform this action.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about bucket policies, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html"&gt;Using Bucket Policies and User Policies&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The following action is related to &lt;code&gt;GetBucketPolicy&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html"&gt;GetObject&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| <CopyableCode code="bucket_policies_Delete" /> | `DELETE` | <CopyableCode code="bucket, region" /> | &lt;p&gt;This implementation of the DELETE action uses the policy subresource to delete the policy of a specified bucket. If you are using an identity other than the root user of the Amazon Web Services account that owns the bucket, the calling identity must have the &lt;code&gt;DeleteBucketPolicy&lt;/code&gt; permissions on the specified bucket and belong to the bucket owner's account to use this operation. &lt;/p&gt; &lt;p&gt;If you don't have &lt;code&gt;DeleteBucketPolicy&lt;/code&gt; permissions, Amazon S3 returns a &lt;code&gt;403 Access Denied&lt;/code&gt; error. If you have the correct permissions, but you're not using an identity that belongs to the bucket owner's account, Amazon S3 returns a &lt;code&gt;405 Method Not Allowed&lt;/code&gt; error. &lt;/p&gt; &lt;important&gt; &lt;p&gt;As a security precaution, the root user of the Amazon Web Services account that owns a bucket can always use this operation, even if the policy explicitly denies the root user the ability to perform this action.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about bucket policies, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html"&gt;Using Bucket Policies and UserPolicies&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;DeleteBucketPolicy&lt;/code&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html"&gt;CreateBucket&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html"&gt;DeleteObject&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| <CopyableCode code="bucket_policies_Put" /> | `EXEC` | <CopyableCode code="bucket, region" /> | &lt;p&gt;Applies an Amazon S3 bucket policy to an Amazon S3 bucket. If you are using an identity other than the root user of the Amazon Web Services account that owns the bucket, the calling identity must have the &lt;code&gt;PutBucketPolicy&lt;/code&gt; permissions on the specified bucket and belong to the bucket owner's account in order to use this operation.&lt;/p&gt; &lt;p&gt;If you don't have &lt;code&gt;PutBucketPolicy&lt;/code&gt; permissions, Amazon S3 returns a &lt;code&gt;403 Access Denied&lt;/code&gt; error. If you have the correct permissions, but you're not using an identity that belongs to the bucket owner's account, Amazon S3 returns a &lt;code&gt;405 Method Not Allowed&lt;/code&gt; error.&lt;/p&gt; &lt;important&gt; &lt;p&gt; As a security precaution, the root user of the Amazon Web Services account that owns a bucket can always use this operation, even if the policy explicitly denies the root user the ability to perform this action. &lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html"&gt;Bucket policy examples&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;PutBucketPolicy&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html"&gt;CreateBucket&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html"&gt;DeleteBucket&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |

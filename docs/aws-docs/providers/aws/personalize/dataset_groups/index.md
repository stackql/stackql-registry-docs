---
title: dataset_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset_groups
  - personalize
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>dataset_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.personalize.dataset_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DatasetGroupArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the dataset group.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name for the new dataset group.</td></tr>
<tr><td><code>KmsKeyArn</code></td><td><code>string</code></td><td>The Amazon Resource Name(ARN) of a AWS Key Management Service (KMS) key used to encrypt the datasets.</td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td>The ARN of the AWS Identity and Access Management (IAM) role that has permissions to access the AWS Key Management Service (KMS) key. Supplying an IAM role is only valid when also specifying a KMS key.</td></tr>
<tr><td><code>Domain</code></td><td><code>string</code></td><td>The domain of a Domain dataset group.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.personalize.dataset_groups
WHERE region = 'us-east-1'
</pre>

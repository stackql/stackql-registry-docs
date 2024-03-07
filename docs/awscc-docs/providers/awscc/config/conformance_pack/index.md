---
title: conformance_pack
hide_title: false
hide_table_of_contents: false
keywords:
  - conformance_pack
  - config
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>conformance_pack</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>conformance_pack</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>conformance_pack</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.config.conformance_pack</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>conformance_pack_name</code></td><td><code>string</code></td><td>Name of the conformance pack which will be assigned as the unique identifier.</td></tr>
<tr><td><code>delivery_s3_bucket</code></td><td><code>string</code></td><td>AWS Config stores intermediate files while processing conformance pack template.</td></tr>
<tr><td><code>delivery_s3_key_prefix</code></td><td><code>string</code></td><td>The prefix for delivery S3 bucket.</td></tr>
<tr><td><code>template_body</code></td><td><code>string</code></td><td>A string containing full conformance pack template body. You can only specify one of the template body or template S3Uri fields.</td></tr>
<tr><td><code>template_s3_uri</code></td><td><code>string</code></td><td>Location of file containing the template body which points to the conformance pack template that is located in an Amazon S3 bucket. You can only specify one of the template body or template S3Uri fields.</td></tr>
<tr><td><code>template_ss_mdocument_details</code></td><td><code>object</code></td><td>The TemplateSSMDocumentDetails object contains the name of the SSM document and the version of the SSM document.</td></tr>
<tr><td><code>conformance_pack_input_parameters</code></td><td><code>array</code></td><td>A list of ConformancePackInputParameter objects.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
conformance_pack_name,
delivery_s3_bucket,
delivery_s3_key_prefix,
template_body,
template_s3_uri,
template_ss_mdocument_details,
conformance_pack_input_parameters
FROM awscc.config.conformance_pack
WHERE region = 'us-east-1'
AND data__Identifier = '{ConformancePackName}';
```

## Permissions

To operate on the <code>conformance_pack</code> resource, the following permissions are required:

### Read
```json
config:DescribeConformancePacks
```

### Update
```json
config:PutConformancePack,
config:DescribeConformancePackStatus,
s3:GetObject,
s3:GetBucketAcl,
iam:CreateServiceLinkedRole,
iam:PassRole
```

### Delete
```json
config:DeleteConformancePack,
config:DescribeConformancePackStatus
```


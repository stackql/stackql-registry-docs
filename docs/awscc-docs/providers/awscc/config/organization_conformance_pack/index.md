---
title: organization_conformance_pack
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_conformance_pack
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
Gets an individual <code>organization_conformance_pack</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_conformance_pack</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>organization_conformance_pack</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.config.organization_conformance_pack</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>organization_conformance_pack_name</code></td><td><code>string</code></td><td>The name of the organization conformance pack.</td></tr>
<tr><td><code>template_s3_uri</code></td><td><code>string</code></td><td>Location of file containing the template body.</td></tr>
<tr><td><code>template_body</code></td><td><code>string</code></td><td>A string containing full conformance pack template body.</td></tr>
<tr><td><code>delivery_s3_bucket</code></td><td><code>string</code></td><td>AWS Config stores intermediate files while processing conformance pack template.</td></tr>
<tr><td><code>delivery_s3_key_prefix</code></td><td><code>string</code></td><td>The prefix for the delivery S3 bucket.</td></tr>
<tr><td><code>conformance_pack_input_parameters</code></td><td><code>array</code></td><td>A list of ConformancePackInputParameter objects.</td></tr>
<tr><td><code>excluded_accounts</code></td><td><code>array</code></td><td>A list of AWS accounts to be excluded from an organization conformance pack while deploying a conformance pack.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>organization_conformance_pack</code> resource, the following permissions are required:

### Read
<pre>
config:DescribeOrganizationConformancePacks</pre>

### Delete
<pre>
config:DeleteOrganizationConformancePack,
config:DescribeOrganizationConformancePackStatuses,
config:GetOrganizationConformancePackDetailedStatus,
organizations:ListDelegatedAdministrators</pre>

### Update
<pre>
config:PutOrganizationConformancePack,
config:DescribeOrganizationConformancePackStatuses,
config:GetOrganizationConformancePackDetailedStatus,
s3:GetObject,
s3:GetBucketAcl,
iam:CreateServiceLinkedRole,
iam:PassRole,
organizations:ListDelegatedAdministrators,
organizations:EnableAWSServiceAccess</pre>


## Example
```sql
SELECT
region,
organization_conformance_pack_name,
template_s3_uri,
template_body,
delivery_s3_bucket,
delivery_s3_key_prefix,
conformance_pack_input_parameters,
excluded_accounts
FROM awscc.config.organization_conformance_pack
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;OrganizationConformancePackName&gt;'
```

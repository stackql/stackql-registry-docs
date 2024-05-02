---
title: license_endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - license_endpoint
  - deadline
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>license_endpoint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>license_endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::LicenseEndpoint Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.deadline.license_endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>dns_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>license_endpoint_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status_message</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
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
dns_name,
license_endpoint_id,
security_group_ids,
status,
status_message,
subnet_ids,
vpc_id,
arn
FROM aws.deadline.license_endpoint
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>license_endpoint</code> resource, the following permissions are required:

### Read
```json
deadline:GetLicenseEndpoint
```

### Delete
```json
deadline:GetLicenseEndpoint,
deadline:DeleteLicenseEndpoint,
ec2:DeleteVpcEndpoints,
ec2:DescribeVpcEndpoints
```


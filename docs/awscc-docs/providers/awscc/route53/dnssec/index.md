---
title: dnssec
hide_title: false
hide_table_of_contents: false
keywords:
  - dnssec
  - route53
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>dnssec</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dnssec</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>dnssec</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53.dnssec</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>hosted_zone_id</code></td><td><code>string</code></td><td>The unique string (ID) used to identify a hosted zone.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
hosted_zone_id
FROM awscc.route53.dnssec
WHERE data__Identifier = '{HostedZoneId}';
```

## Permissions

To operate on the <code>dnssec</code> resource, the following permissions are required:

### Read
```json
route53:GetDNSSEC
```

### Delete
```json
route53:GetDNSSEC,
route53:DisableHostedZoneDNSSEC,
kms:DescribeKey,
kms:GetPublicKey,
kms:Sign,
kms:CreateGrant
```


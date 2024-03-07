---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
  - pcaconnectorad
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>connectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>connectors</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.pcaconnectorad.connectors</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>connector_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
connector_arn
FROM awscc.pcaconnectorad.connectors
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>connectors</code> resource, the following permissions are required:

### Create
```json
acm-pca:DescribeCertificateAuthority,
acm-pca:GetCertificateAuthorityCertificate,
acm-pca:GetCertificate,
acm-pca:IssueCertificate,
ds:DescribeDirectories,
ec2:CreateTags,
ec2:CreateVpcEndpoint,
ec2:DescribeVpcEndpoints,
pca-connector-ad:CreateConnector,
pca-connector-ad:GetConnector
```

### List
```json
pca-connector-ad:ListConnectors
```


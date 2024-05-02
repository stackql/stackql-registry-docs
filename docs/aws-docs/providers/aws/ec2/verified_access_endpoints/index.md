---
title: verified_access_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_access_endpoints
  - ec2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Used to retrieve a list of <code>verified_access_endpoints</code> in a region or create a <code>verified_access_endpoints</code> resource, use <code>verified_access_endpoint</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_access_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::VerifiedAccessEndpoint resource creates an AWS EC2 Verified Access Endpoint.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.verified_access_endpoints</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>verified_access_endpoint_id</code></td><td><code>string</code></td><td>The ID of the AWS Verified Access endpoint.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
verified_access_endpoint_id
FROM aws.ec2.verified_access_endpoints
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>verified_access_endpoints</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVerifiedAccessEndpoint,
ec2:DescribeVerifiedAccessEndpoints,
ec2:CreateTags,
ec2:DescribeTags,
iam:CreateServiceLinkedRole,
iam:ListRoles,
acm:GetCertificateWithPK,
acm:DescribeCertificate,
acm:CreateCertificateRelation,
sso:GetManagedApplicationInstance,
sso:GetPeregrineStatus,
sso:GetSharedSsoConfiguration,
sso:CreateManagedApplicationInstance,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups,
ec2:DescribeNetworkInterfaces,
ec2:DescribeAccountAttributes,
elasticloadbalancing:DescribeLoadBalancers,
elasticloadbalancing:DescribeListeners,
elasticloadbalancing:DescribeListenerCertificates,
acm:DeleteCertificateRelation,
ec2:DeleteTags,
ec2:DeleteVerifiedAccessEndpoint,
ec2:GetVerifiedAccessEndpointPolicy,
ec2:ModifyVerifiedAccessEndpoint,
ec2:ModifyVerifiedAccessEndpointPolicy,
sso:DeleteManagedApplicationInstance,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

### List
```json
ec2:DescribeVerifiedAccessEndpoints,
ec2:DescribeTags,
acm:CreateCertificateRelation,
acm:DeleteCertificateRelation,
acm:DescribeCertificate,
acm:GetCertificateWithPK,
ec2:CreateTags,
ec2:CreateVerifiedAccessEndpoint,
ec2:DeleteTags,
ec2:DeleteVerifiedAccessEndpoint,
ec2:DescribeAccountAttributes,
ec2:DescribeNetworkInterfaces,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:GetVerifiedAccessEndpointPolicy,
ec2:ModifyVerifiedAccessEndpoint,
ec2:ModifyVerifiedAccessEndpointPolicy,
elasticloadbalancing:DescribeListenerCertificates,
elasticloadbalancing:DescribeListeners,
elasticloadbalancing:DescribeLoadBalancers,
iam:CreateServiceLinkedRole,
iam:ListRoles,
sso:CreateManagedApplicationInstance,
sso:DeleteManagedApplicationInstance,
sso:GetManagedApplicationInstance,
sso:GetPeregrineStatus,
sso:GetSharedSsoConfiguration,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```


---
title: verified_access_endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_access_endpoint
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
Gets an individual <code>verified_access_endpoint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_access_endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>verified_access_endpoint</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.verified_access_endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>verified_access_endpoint_id</code></td><td><code>string</code></td><td>The ID of the AWS Verified Access endpoint.</td></tr>
<tr><td><code>verified_access_group_id</code></td><td><code>string</code></td><td>The ID of the AWS Verified Access group.</td></tr>
<tr><td><code>verified_access_instance_id</code></td><td><code>string</code></td><td>The ID of the AWS Verified Access instance.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The endpoint status.</td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td>The IDs of the security groups for the endpoint.</td></tr>
<tr><td><code>network_interface_options</code></td><td><code>object</code></td><td>The options for network-interface type endpoint.</td></tr>
<tr><td><code>load_balancer_options</code></td><td><code>object</code></td><td>The load balancer details if creating the AWS Verified Access endpoint as load-balancer type.</td></tr>
<tr><td><code>endpoint_type</code></td><td><code>string</code></td><td>The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.</td></tr>
<tr><td><code>endpoint_domain</code></td><td><code>string</code></td><td>A DNS name that is generated for the endpoint.</td></tr>
<tr><td><code>endpoint_domain_prefix</code></td><td><code>string</code></td><td>A custom identifier that gets prepended to a DNS name that is generated for the endpoint.</td></tr>
<tr><td><code>device_validation_domain</code></td><td><code>string</code></td><td>Returned if endpoint has a device trust provider attached.</td></tr>
<tr><td><code>domain_certificate_arn</code></td><td><code>string</code></td><td>The ARN of a public TLS&#x2F;SSL certificate imported into or created with ACM.</td></tr>
<tr><td><code>attachment_type</code></td><td><code>string</code></td><td>The type of attachment used to provide connectivity between the AWS Verified Access endpoint and the application.</td></tr>
<tr><td><code>application_domain</code></td><td><code>string</code></td><td>The DNS name for users to reach your application.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>The creation time.</td></tr>
<tr><td><code>last_updated_time</code></td><td><code>string</code></td><td>The last updated time.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description for the AWS Verified Access endpoint.</td></tr>
<tr><td><code>policy_document</code></td><td><code>string</code></td><td>The AWS Verified Access policy document.</td></tr>
<tr><td><code>policy_enabled</code></td><td><code>boolean</code></td><td>The status of the Verified Access policy.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>sse_specification</code></td><td><code>object</code></td><td>The configuration options for customer provided KMS encryption.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
verified_access_endpoint_id,
verified_access_group_id,
verified_access_instance_id,
status,
security_group_ids,
network_interface_options,
load_balancer_options,
endpoint_type,
endpoint_domain,
endpoint_domain_prefix,
device_validation_domain,
domain_certificate_arn,
attachment_type,
application_domain,
creation_time,
last_updated_time,
description,
policy_document,
policy_enabled,
tags,
sse_specification
FROM awscc.ec2.verified_access_endpoint
WHERE data__Identifier = '<VerifiedAccessEndpointId>';
```

## Permissions

To operate on the <code>verified_access_endpoint</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeVerifiedAccessEndpoints,
ec2:GetVerifiedAccessEndpointPolicy,
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

### Update
```json
ec2:ModifyVerifiedAccessEndpoint,
ec2:ModifyVerifiedAccessEndpointPolicy,
ec2:DescribeVerifiedAccessEndpoints,
ec2:GetVerifiedAccessEndpointPolicy,
ec2:DescribeTags,
ec2:DeleteTags,
ec2:CreateTags,
acm:GetCertificateWithPK,
acm:DescribeCertificate,
acm:CreateCertificateRelation,
acm:DeleteCertificateRelation,
sso:GetManagedApplicationInstance,
sso:GetPeregrineStatus,
sso:GetSharedSsoConfiguration,
sso:CreateManagedApplicationInstance,
sso:DeleteManagedApplicationInstance,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups,
ec2:DescribeNetworkInterfaces,
ec2:DescribeAccountAttributes,
elasticloadbalancing:DescribeLoadBalancers,
elasticloadbalancing:DescribeListeners,
elasticloadbalancing:DescribeListenerCertificates,
ec2:CreateVerifiedAccessEndpoint,
ec2:DeleteVerifiedAccessEndpoint,
iam:CreateServiceLinkedRole,
iam:ListRoles,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
ec2:DescribeVerifiedAccessEndpoints,
ec2:DescribeTags,
ec2:DeleteVerifiedAccessEndpoint,
ec2:DeleteTags,
sso:DeleteManagedApplicationInstance,
acm:DeleteCertificateRelation,
acm:DescribeCertificate,
acm:CreateCertificateRelation,
acm:GetCertificateWithPK,
ec2:CreateTags,
ec2:CreateVerifiedAccessEndpoint,
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
sso:GetManagedApplicationInstance,
sso:GetPeregrineStatus,
sso:GetSharedSsoConfiguration,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```


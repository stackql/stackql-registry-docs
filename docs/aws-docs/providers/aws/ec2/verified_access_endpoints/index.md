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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>verified_access_endpoint</code> resource or lists <code>verified_access_endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_access_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::VerifiedAccessEndpoint resource creates an AWS EC2 Verified Access Endpoint.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.verified_access_endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="verified_access_endpoint_id" /></td><td><code>string</code></td><td>The ID of the AWS Verified Access endpoint.</td></tr>
<tr><td><CopyableCode code="verified_access_group_id" /></td><td><code>string</code></td><td>The ID of the AWS Verified Access group.</td></tr>
<tr><td><CopyableCode code="verified_access_instance_id" /></td><td><code>string</code></td><td>The ID of the AWS Verified Access instance.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The endpoint status.</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>The IDs of the security groups for the endpoint.</td></tr>
<tr><td><CopyableCode code="network_interface_options" /></td><td><code>object</code></td><td>The options for network-interface type endpoint.</td></tr>
<tr><td><CopyableCode code="load_balancer_options" /></td><td><code>object</code></td><td>The load balancer details if creating the AWS Verified Access endpoint as load-balancer type.</td></tr>
<tr><td><CopyableCode code="endpoint_type" /></td><td><code>string</code></td><td>The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.</td></tr>
<tr><td><CopyableCode code="endpoint_domain" /></td><td><code>string</code></td><td>A DNS name that is generated for the endpoint.</td></tr>
<tr><td><CopyableCode code="endpoint_domain_prefix" /></td><td><code>string</code></td><td>A custom identifier that gets prepended to a DNS name that is generated for the endpoint.</td></tr>
<tr><td><CopyableCode code="device_validation_domain" /></td><td><code>string</code></td><td>Returned if endpoint has a device trust provider attached.</td></tr>
<tr><td><CopyableCode code="domain_certificate_arn" /></td><td><code>string</code></td><td>The ARN of a public TLS/SSL certificate imported into or created with ACM.</td></tr>
<tr><td><CopyableCode code="attachment_type" /></td><td><code>string</code></td><td>The type of attachment used to provide connectivity between the AWS Verified Access endpoint and the application.</td></tr>
<tr><td><CopyableCode code="application_domain" /></td><td><code>string</code></td><td>The DNS name for users to reach your application.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The creation time.</td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td>The last updated time.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the AWS Verified Access endpoint.</td></tr>
<tr><td><CopyableCode code="policy_document" /></td><td><code>string</code></td><td>The AWS Verified Access policy document.</td></tr>
<tr><td><CopyableCode code="policy_enabled" /></td><td><code>boolean</code></td><td>The status of the Verified Access policy.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="sse_specification" /></td><td><code>object</code></td><td>The configuration options for customer provided KMS encryption.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-verifiedaccessendpoint.html"><code>AWS::EC2::VerifiedAccessEndpoint</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="ApplicationDomain, AttachmentType, DomainCertificateArn, EndpointType, VerifiedAccessGroupId, EndpointDomainPrefix, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>verified_access_endpoints</code> in a region.
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
FROM aws.ec2.verified_access_endpoints
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>verified_access_endpoint</code>.
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
FROM aws.ec2.verified_access_endpoints
WHERE region = 'us-east-1' AND data__Identifier = '<VerifiedAccessEndpointId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>verified_access_endpoint</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.ec2.verified_access_endpoints (
 VerifiedAccessGroupId,
 EndpointType,
 EndpointDomainPrefix,
 DomainCertificateArn,
 AttachmentType,
 ApplicationDomain,
 region
)
SELECT 
'{{ VerifiedAccessGroupId }}',
 '{{ EndpointType }}',
 '{{ EndpointDomainPrefix }}',
 '{{ DomainCertificateArn }}',
 '{{ AttachmentType }}',
 '{{ ApplicationDomain }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.verified_access_endpoints (
 VerifiedAccessGroupId,
 SecurityGroupIds,
 NetworkInterfaceOptions,
 LoadBalancerOptions,
 EndpointType,
 EndpointDomainPrefix,
 DomainCertificateArn,
 AttachmentType,
 ApplicationDomain,
 Description,
 PolicyDocument,
 PolicyEnabled,
 Tags,
 SseSpecification,
 region
)
SELECT 
 '{{ VerifiedAccessGroupId }}',
 '{{ SecurityGroupIds }}',
 '{{ NetworkInterfaceOptions }}',
 '{{ LoadBalancerOptions }}',
 '{{ EndpointType }}',
 '{{ EndpointDomainPrefix }}',
 '{{ DomainCertificateArn }}',
 '{{ AttachmentType }}',
 '{{ ApplicationDomain }}',
 '{{ Description }}',
 '{{ PolicyDocument }}',
 '{{ PolicyEnabled }}',
 '{{ Tags }}',
 '{{ SseSpecification }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: verified_access_endpoint
    props:
      - name: VerifiedAccessGroupId
        value: '{{ VerifiedAccessGroupId }}'
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: NetworkInterfaceOptions
        value:
          NetworkInterfaceId: '{{ NetworkInterfaceId }}'
          Port: '{{ Port }}'
          Protocol: '{{ Protocol }}'
      - name: LoadBalancerOptions
        value:
          LoadBalancerArn: '{{ LoadBalancerArn }}'
          Port: '{{ Port }}'
          Protocol: '{{ Protocol }}'
          SubnetIds:
            - '{{ SubnetIds[0] }}'
      - name: EndpointType
        value: '{{ EndpointType }}'
      - name: EndpointDomainPrefix
        value: '{{ EndpointDomainPrefix }}'
      - name: DomainCertificateArn
        value: '{{ DomainCertificateArn }}'
      - name: AttachmentType
        value: '{{ AttachmentType }}'
      - name: ApplicationDomain
        value: '{{ ApplicationDomain }}'
      - name: Description
        value: '{{ Description }}'
      - name: PolicyDocument
        value: '{{ PolicyDocument }}'
      - name: PolicyEnabled
        value: '{{ PolicyEnabled }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: SseSpecification
        value:
          KmsKeyArn: '{{ KmsKeyArn }}'
          CustomerManagedKeyEnabled: '{{ CustomerManagedKeyEnabled }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.verified_access_endpoints
WHERE data__Identifier = '<VerifiedAccessEndpointId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>verified_access_endpoints</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVerifiedAccessEndpoint,
ec2:DescribeVerifiedAccessEndpoints,
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
ec2:CreateTags,
ec2:DescribeTags,
acm:DeleteCertificateRelation,
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

### Read
```json
ec2:DescribeVerifiedAccessEndpoints,
ec2:GetVerifiedAccessEndpointPolicy,
ec2:DescribeTags,
acm:CreateCertificateRelation,
acm:DeleteCertificateRelation,
acm:DescribeCertificate,
acm:GetCertificateWithPK,
ec2:CreateVerifiedAccessEndpoint,
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
ec2:DescribeTags,
ec2:DeleteTags,
ec2:CreateTags,
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
ec2:DeleteVerifiedAccessEndpoint,
ec2:DescribeTags,
ec2:DeleteTags,
sso:DeleteManagedApplicationInstance,
acm:DeleteCertificateRelation,
acm:DescribeCertificate,
acm:CreateCertificateRelation,
acm:GetCertificateWithPK,
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

### List
```json
ec2:DescribeVerifiedAccessEndpoints,
ec2:DescribeTags,
acm:CreateCertificateRelation,
acm:DeleteCertificateRelation,
acm:DescribeCertificate,
acm:GetCertificateWithPK,
ec2:CreateVerifiedAccessEndpoint,
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

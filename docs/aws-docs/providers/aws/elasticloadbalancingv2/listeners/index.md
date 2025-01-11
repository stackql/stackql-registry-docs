---
title: listeners
hide_title: false
hide_table_of_contents: false
keywords:
  - listeners
  - elasticloadbalancingv2
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

Creates, updates, deletes or gets a <code>listener</code> resource or lists <code>listeners</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listeners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a listener for an Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticloadbalancingv2.listeners" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="listener_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="mutual_authentication" /></td><td><code>object</code></td><td>The mutual authentication configuration information.</td></tr>
<tr><td><CopyableCode code="listener_attributes" /></td><td><code>array</code></td><td>The listener attributes.</td></tr>
<tr><td><CopyableCode code="alpn_policy" /></td><td><code>array</code></td><td>&#91;TLS listener&#93; The name of the Application-Layer Protocol Negotiation (ALPN) policy.</td></tr>
<tr><td><CopyableCode code="ssl_policy" /></td><td><code>string</code></td><td>&#91;HTTPS and TLS listeners&#93; The security policy that defines which protocols and ciphers are supported.<br />Updating the security policy can result in interruptions if the load balancer is handling a high volume of traffic.<br />For more information, see &#91;Security policies&#93;(https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies) in the *Application Load Balancers Guide* and &#91;Security policies&#93;(https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html#describe-ssl-policies) in the *Network Load Balancers Guide*.</td></tr>
<tr><td><CopyableCode code="load_balancer_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the load balancer.</td></tr>
<tr><td><CopyableCode code="default_actions" /></td><td><code>array</code></td><td>The actions for the default rule. You cannot define a condition for a default rule.<br />To create additional rules for an Application Load Balancer, use &#91;AWS::ElasticLoadBalancingV2::ListenerRule&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.html).</td></tr>
<tr><td><CopyableCode code="port" /></td><td><code>integer</code></td><td>The port on which the load balancer is listening. You can't specify a port for a Gateway Load Balancer.</td></tr>
<tr><td><CopyableCode code="certificates" /></td><td><code>array</code></td><td>The default SSL server certificate for a secure listener. You must provide exactly one certificate if the listener protocol is HTTPS or TLS.<br />To create a certificate list for a secure listener, use &#91;AWS::ElasticLoadBalancingV2::ListenerCertificate&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenercertificate.html).</td></tr>
<tr><td><CopyableCode code="protocol" /></td><td><code>string</code></td><td>The protocol for connections from clients to the load balancer. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are TCP, TLS, UDP, and TCP_UDP. You can’t specify the UDP or TCP_UDP protocol if dual-stack mode is enabled. You can't specify a protocol for a Gateway Load Balancer.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.html"><code>AWS::ElasticLoadBalancingV2::Listener</code></a>.

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
    <td><CopyableCode code="LoadBalancerArn, DefaultActions, region" /></td>
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
Gets all <code>listeners</code> in a region.
```sql
SELECT
region,
listener_arn,
mutual_authentication,
listener_attributes,
alpn_policy,
ssl_policy,
load_balancer_arn,
default_actions,
port,
certificates,
protocol
FROM aws.elasticloadbalancingv2.listeners
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>listener</code>.
```sql
SELECT
region,
listener_arn,
mutual_authentication,
listener_attributes,
alpn_policy,
ssl_policy,
load_balancer_arn,
default_actions,
port,
certificates,
protocol
FROM aws.elasticloadbalancingv2.listeners
WHERE region = 'us-east-1' AND data__Identifier = '<ListenerArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>listener</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.elasticloadbalancingv2.listeners (
 LoadBalancerArn,
 DefaultActions,
 region
)
SELECT 
'{{ LoadBalancerArn }}',
 '{{ DefaultActions }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.elasticloadbalancingv2.listeners (
 MutualAuthentication,
 ListenerAttributes,
 AlpnPolicy,
 SslPolicy,
 LoadBalancerArn,
 DefaultActions,
 Port,
 Certificates,
 Protocol,
 region
)
SELECT 
 '{{ MutualAuthentication }}',
 '{{ ListenerAttributes }}',
 '{{ AlpnPolicy }}',
 '{{ SslPolicy }}',
 '{{ LoadBalancerArn }}',
 '{{ DefaultActions }}',
 '{{ Port }}',
 '{{ Certificates }}',
 '{{ Protocol }}',
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
  - name: listener
    props:
      - name: MutualAuthentication
        value:
          IgnoreClientCertificateExpiry: '{{ IgnoreClientCertificateExpiry }}'
          Mode: '{{ Mode }}'
          TrustStoreArn: '{{ TrustStoreArn }}'
          AdvertiseTrustStoreCaNames: '{{ AdvertiseTrustStoreCaNames }}'
      - name: ListenerAttributes
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: AlpnPolicy
        value:
          - '{{ AlpnPolicy[0] }}'
      - name: SslPolicy
        value: '{{ SslPolicy }}'
      - name: LoadBalancerArn
        value: '{{ LoadBalancerArn }}'
      - name: DefaultActions
        value:
          - Order: '{{ Order }}'
            TargetGroupArn: '{{ TargetGroupArn }}'
            FixedResponseConfig:
              ContentType: '{{ ContentType }}'
              StatusCode: '{{ StatusCode }}'
              MessageBody: '{{ MessageBody }}'
            AuthenticateCognitoConfig:
              OnUnauthenticatedRequest: '{{ OnUnauthenticatedRequest }}'
              UserPoolClientId: '{{ UserPoolClientId }}'
              UserPoolDomain: '{{ UserPoolDomain }}'
              SessionTimeout: '{{ SessionTimeout }}'
              Scope: '{{ Scope }}'
              SessionCookieName: '{{ SessionCookieName }}'
              UserPoolArn: '{{ UserPoolArn }}'
              AuthenticationRequestExtraParams: {}
            Type: '{{ Type }}'
            RedirectConfig:
              Path: '{{ Path }}'
              Query: '{{ Query }}'
              Port: '{{ Port }}'
              Host: '{{ Host }}'
              Protocol: '{{ Protocol }}'
              StatusCode: '{{ StatusCode }}'
            ForwardConfig:
              TargetGroupStickinessConfig:
                Enabled: '{{ Enabled }}'
                DurationSeconds: '{{ DurationSeconds }}'
              TargetGroups:
                - TargetGroupArn: '{{ TargetGroupArn }}'
                  Weight: '{{ Weight }}'
            AuthenticateOidcConfig:
              OnUnauthenticatedRequest: '{{ OnUnauthenticatedRequest }}'
              TokenEndpoint: '{{ TokenEndpoint }}'
              SessionTimeout: '{{ SessionTimeout }}'
              Scope: '{{ Scope }}'
              Issuer: '{{ Issuer }}'
              ClientSecret: '{{ ClientSecret }}'
              UserInfoEndpoint: '{{ UserInfoEndpoint }}'
              ClientId: '{{ ClientId }}'
              AuthorizationEndpoint: '{{ AuthorizationEndpoint }}'
              SessionCookieName: '{{ SessionCookieName }}'
              UseExistingClientSecret: '{{ UseExistingClientSecret }}'
              AuthenticationRequestExtraParams: {}
      - name: Port
        value: '{{ Port }}'
      - name: Certificates
        value:
          - CertificateArn: '{{ CertificateArn }}'
      - name: Protocol
        value: '{{ Protocol }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.elasticloadbalancingv2.listeners
WHERE data__Identifier = '<ListenerArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>listeners</code> resource, the following permissions are required:

### Read
```json
elasticloadbalancing:DescribeListeners,
elasticloadbalancing:DescribeListenerAttributes
```

### Create
```json
elasticloadbalancing:CreateListener,
elasticloadbalancing:DescribeListeners,
cognito-idp:DescribeUserPoolClient,
elasticloadbalancing:ModifyListenerAttributes
```

### Update
```json
elasticloadbalancing:ModifyListener,
elasticloadbalancing:DescribeListeners,
cognito-idp:DescribeUserPoolClient,
elasticloadbalancing:ModifyListenerAttributes
```

### List
```json
elasticloadbalancing:DescribeListeners
```

### Delete
```json
elasticloadbalancing:DeleteListener,
elasticloadbalancing:DescribeListeners
```

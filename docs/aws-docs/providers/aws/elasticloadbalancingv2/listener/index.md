---
title: listener
hide_title: false
hide_table_of_contents: false
keywords:
  - listener
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
Gets an individual <code>listener</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listener</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a listener for an Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.elasticloadbalancingv2.listener</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ssl_policy</code></td><td><code>string</code></td><td>&#91;HTTPS and TLS listeners&#93; The security policy that defines which protocols and ciphers are supported.&lt;br&#x2F;&gt; Updating the security policy can result in interruptions if the load balancer is handling a high volume of traffic.&lt;br&#x2F;&gt; For more information, see &#91;Security policies&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;elasticloadbalancing&#x2F;latest&#x2F;application&#x2F;create-https-listener.html#describe-ssl-policies) in the *Application Load Balancers Guide* and &#91;Security policies&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;elasticloadbalancing&#x2F;latest&#x2F;network&#x2F;create-tls-listener.html#describe-ssl-policies) in the *Network Load Balancers Guide*.</td></tr>
<tr><td><code>load_balancer_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the load balancer.</td></tr>
<tr><td><code>default_actions</code></td><td><code>array</code></td><td>The actions for the default rule. You cannot define a condition for a default rule.&lt;br&#x2F;&gt; To create additional rules for an Application Load Balancer, use &#91;AWS::ElasticLoadBalancingV2::ListenerRule&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-elasticloadbalancingv2-listenerrule.html).</td></tr>
<tr><td><code>port</code></td><td><code>integer</code></td><td>The port on which the load balancer is listening. You cannot specify a port for a Gateway Load Balancer.</td></tr>
<tr><td><code>certificates</code></td><td><code>array</code></td><td>The default SSL server certificate for a secure listener. You must provide exactly one certificate if the listener protocol is HTTPS or TLS.&lt;br&#x2F;&gt; To create a certificate list for a secure listener, use &#91;AWS::ElasticLoadBalancingV2::ListenerCertificate&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-elasticloadbalancingv2-listenercertificate.html).</td></tr>
<tr><td><code>protocol</code></td><td><code>string</code></td><td>The protocol for connections from clients to the load balancer. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are TCP, TLS, UDP, and TCP_UDP. You can’t specify the UDP or TCP_UDP protocol if dual-stack mode is enabled. You cannot specify a protocol for a Gateway Load Balancer.</td></tr>
<tr><td><code>listener_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>alpn_policy</code></td><td><code>array</code></td><td>&#91;TLS listener&#93; The name of the Application-Layer Protocol Negotiation (ALPN) policy.</td></tr>
<tr><td><code>mutual_authentication</code></td><td><code>object</code></td><td>The mutual authentication configuration information.</td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
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
ssl_policy,
load_balancer_arn,
default_actions,
port,
certificates,
protocol,
listener_arn,
alpn_policy,
mutual_authentication
FROM aws.elasticloadbalancingv2.listener
WHERE data__Identifier = '<ListenerArn>';
```

## Permissions

To operate on the <code>listener</code> resource, the following permissions are required:

### Delete
```json
elasticloadbalancing:DeleteListener,
elasticloadbalancing:DescribeListeners
```

### Read
```json
elasticloadbalancing:DescribeListeners
```

### Update
```json
elasticloadbalancing:ModifyListener,
elasticloadbalancing:DescribeListeners,
cognito-idp:DescribeUserPoolClient
```


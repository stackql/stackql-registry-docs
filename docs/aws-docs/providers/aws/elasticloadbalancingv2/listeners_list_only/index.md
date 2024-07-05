---
title: listeners_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - listeners_list_only
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

Lists <code>listeners</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/listeners/"><code>listeners</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listeners_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a listener for an Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticloadbalancingv2.listeners_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="listener_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="mutual_authentication" /></td><td><code>object</code></td><td>The mutual authentication configuration information.</td></tr>
<tr><td><CopyableCode code="alpn_policy" /></td><td><code>array</code></td><td>&#91;TLS listener&#93; The name of the Application-Layer Protocol Negotiation (ALPN) policy.</td></tr>
<tr><td><CopyableCode code="ssl_policy" /></td><td><code>string</code></td><td>&#91;HTTPS and TLS listeners&#93; The security policy that defines which protocols and ciphers are supported.<br />Updating the security policy can result in interruptions if the load balancer is handling a high volume of traffic.<br />For more information, see &#91;Security policies&#93;(https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies) in the *Application Load Balancers Guide* and &#91;Security policies&#93;(https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html#describe-ssl-policies) in the *Network Load Balancers Guide*.</td></tr>
<tr><td><CopyableCode code="load_balancer_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the load balancer.</td></tr>
<tr><td><CopyableCode code="default_actions" /></td><td><code>array</code></td><td>The actions for the default rule. You cannot define a condition for a default rule.<br />To create additional rules for an Application Load Balancer, use &#91;AWS::ElasticLoadBalancingV2::ListenerRule&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.html).</td></tr>
<tr><td><CopyableCode code="port" /></td><td><code>integer</code></td><td>The port on which the load balancer is listening. You cannot specify a port for a Gateway Load Balancer.</td></tr>
<tr><td><CopyableCode code="certificates" /></td><td><code>array</code></td><td>The default SSL server certificate for a secure listener. You must provide exactly one certificate if the listener protocol is HTTPS or TLS.<br />To create a certificate list for a secure listener, use &#91;AWS::ElasticLoadBalancingV2::ListenerCertificate&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenercertificate.html).</td></tr>
<tr><td><CopyableCode code="protocol" /></td><td><code>string</code></td><td>The protocol for connections from clients to the load balancer. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are TCP, TLS, UDP, and TCP_UDP. You can’t specify the UDP or TCP_UDP protocol if dual-stack mode is enabled. You cannot specify a protocol for a Gateway Load Balancer.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>listeners</code> in a region.
```sql
SELECT
region,
listener_arn
FROM aws.elasticloadbalancingv2.listeners_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>listeners_list_only</code> resource, see <a href="/providers/aws/elasticloadbalancingv2/listeners/#permissions"><code>listeners</code></a>



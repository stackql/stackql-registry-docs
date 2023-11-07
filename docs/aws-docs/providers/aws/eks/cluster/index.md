---
title: cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster
  - eks
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>cluster</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cluster</td></tr>
<tr><td><b>Id</b></td><td><code>aws.eks.cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>EncryptionConfig</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>KubernetesNetworkConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Logging</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The unique name to give to your cluster.</td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>The unique ID given to your cluster.</td></tr>
<tr><td><code>ResourcesVpcConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>OutpostConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.</td></tr>
<tr><td><code>Version</code></td><td><code>string</code></td><td>The desired Kubernetes version for your cluster. If you don't specify a value here, the latest version available in Amazon EKS is used.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The ARN of the cluster, such as arn:aws:eks:us-west-2:666666666666:cluster&#x2F;prod.</td></tr>
<tr><td><code>Endpoint</code></td><td><code>string</code></td><td>The endpoint for your Kubernetes API server, such as https:&#x2F;&#x2F;5E1D0CEXAMPLEA591B746AFC5AB30262.yl4.us-west-2.eks.amazonaws.com.</td></tr>
<tr><td><code>CertificateAuthorityData</code></td><td><code>string</code></td><td>The certificate-authority-data for your cluster.</td></tr>
<tr><td><code>ClusterSecurityGroupId</code></td><td><code>string</code></td><td>The cluster security group that was created by Amazon EKS for the cluster. Managed node groups use this security group for control plane to data plane communication.</td></tr>
<tr><td><code>EncryptionConfigKeyArn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) or alias of the customer master key (CMK).</td></tr>
<tr><td><code>OpenIdConnectIssuerUrl</code></td><td><code>string</code></td><td>The issuer URL for the cluster's OIDC identity provider, such as https:&#x2F;&#x2F;oidc.eks.us-west-2.amazonaws.com&#x2F;id&#x2F;EXAMPLED539D4633E53DE1B716D3041E. If you need to remove https:&#x2F;&#x2F; from this output value, you can include the following code in your template.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.eks.cluster<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Name&gt;'
</pre>

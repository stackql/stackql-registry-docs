---
title: cluster_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An object representing an Amazon EKS cluster.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.cluster_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="logging" /></td><td><code>object</code></td><td>Enable exporting the Kubernetes control plane logs for your cluster to CloudWatch Logs based on log types. By default, cluster control plane logs aren't exported to CloudWatch Logs.</td></tr>
<tr><td><CopyableCode code="encryption_config_key_arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) or alias of the customer master key (CMK).</td></tr>
<tr><td><CopyableCode code="access_config" /></td><td><code>object</code></td><td>An object representing the Access Config to use for the cluster.</td></tr>
<tr><td><CopyableCode code="certificate_authority_data" /></td><td><code>string</code></td><td>The certificate-authority-data for your cluster.</td></tr>
<tr><td><CopyableCode code="encryption_config" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="kubernetes_network_config" /></td><td><code>object</code></td><td>The Kubernetes network configuration for the cluster.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The unique name to give to your cluster.</td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td>The endpoint for your Kubernetes API server, such as https://5E1D0CEXAMPLEA591B746AFC5AB30262.yl4.us-west-2.eks.amazonaws.com.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The desired Kubernetes version for your cluster. If you don't specify a value here, the latest version available in Amazon EKS is used.</td></tr>
<tr><td><CopyableCode code="cluster_security_group_id" /></td><td><code>string</code></td><td>The cluster security group that was created by Amazon EKS for the cluster. Managed node groups use this security group for control plane to data plane communication.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique ID given to your cluster.</td></tr>
<tr><td><CopyableCode code="outpost_config" /></td><td><code>object</code></td><td>An object representing the Outpost configuration to use for AWS EKS outpost cluster.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the cluster, such as arn:aws:eks:us-west-2:666666666666:cluster/prod.</td></tr>
<tr><td><CopyableCode code="resources_vpc_config" /></td><td><code>object</code></td><td>An object representing the VPC configuration to use for an Amazon EKS cluster.</td></tr>
<tr><td><CopyableCode code="open_id_connect_issuer_url" /></td><td><code>string</code></td><td>The issuer URL for the cluster's OIDC identity provider, such as https://oidc.eks.us-west-2.amazonaws.com/id/EXAMPLED539D4633E53DE1B716D3041E. If you need to remove https:// from this output value, you can include the following code in your template.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>clusters</code> in a region.
```sql
SELECT
region,
logging,
encryption_config_key_arn,
access_config,
certificate_authority_data,
encryption_config,
kubernetes_network_config,
role_arn,
name,
endpoint,
version,
cluster_security_group_id,
id,
outpost_config,
arn,
resources_vpc_config,
open_id_connect_issuer_url,
tag_key,
tag_value
FROM aws.eks.cluster_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>cluster_tags</code> resource, see <a href="/providers/aws/eks/clusters/#permissions"><code>clusters</code></a>



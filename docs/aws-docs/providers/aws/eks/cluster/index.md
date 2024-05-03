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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>cluster</code> resource, use <code>clusters</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An object representing an Amazon EKS cluster.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eks.cluster" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="encryption_config" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="kubernetes_network_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="logging" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The unique name to give to your cluster.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique ID given to your cluster.</td></tr>
<tr><td><CopyableCode code="resources_vpc_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="outpost_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="access_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The desired Kubernetes version for your cluster. If you don't specify a value here, the latest version available in Amazon EKS is used.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the cluster, such as arn:aws:eks:us-west-2:666666666666:cluster&#x2F;prod.</td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td>The endpoint for your Kubernetes API server, such as https:&#x2F;&#x2F;5E1D0CEXAMPLEA591B746AFC5AB30262.yl4.us-west-2.eks.amazonaws.com.</td></tr>
<tr><td><CopyableCode code="certificate_authority_data" /></td><td><code>string</code></td><td>The certificate-authority-data for your cluster.</td></tr>
<tr><td><CopyableCode code="cluster_security_group_id" /></td><td><code>string</code></td><td>The cluster security group that was created by Amazon EKS for the cluster. Managed node groups use this security group for control plane to data plane communication.</td></tr>
<tr><td><CopyableCode code="encryption_config_key_arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) or alias of the customer master key (CMK).</td></tr>
<tr><td><CopyableCode code="open_id_connect_issuer_url" /></td><td><code>string</code></td><td>The issuer URL for the cluster's OIDC identity provider, such as https:&#x2F;&#x2F;oidc.eks.us-west-2.amazonaws.com&#x2F;id&#x2F;EXAMPLED539D4633E53DE1B716D3041E. If you need to remove https:&#x2F;&#x2F; from this output value, you can include the following code in your template.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
encryption_config,
kubernetes_network_config,
logging,
name,
id,
resources_vpc_config,
outpost_config,
access_config,
role_arn,
version,
tags,
arn,
endpoint,
certificate_authority_data,
cluster_security_group_id,
encryption_config_key_arn,
open_id_connect_issuer_url
FROM aws.eks.cluster
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>cluster</code> resource, the following permissions are required:

### Read
```json
eks:DescribeCluster
```

### Update
```json
iam:PassRole,
eks:UpdateClusterConfig,
eks:UpdateClusterVersion,
eks:DescribeCluster,
eks:DescribeUpdate,
eks:TagResource,
eks:UntagResource
```

### Delete
```json
eks:DeleteCluster,
eks:DescribeCluster
```


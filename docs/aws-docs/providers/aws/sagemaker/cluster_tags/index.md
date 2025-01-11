---
title: cluster_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_tags
  - sagemaker
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
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::Cluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.cluster_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the HyperPod Cluster.</td></tr>
<tr><td><CopyableCode code="vpc_config" /></td><td><code>object</code></td><td>Specifies a VPC that your training jobs and hosted models have access to. Control access to and from your training and model containers by configuring the VPC.</td></tr>
<tr><td><CopyableCode code="node_recovery" /></td><td><code>string</code></td><td>If node auto-recovery is set to true, faulty nodes will be replaced or rebooted when a failure is detected. If set to false, nodes will be labelled when a fault is detected.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time at which the HyperPod cluster was created.</td></tr>
<tr><td><CopyableCode code="instance_groups" /></td><td><code>array</code></td><td>The instance groups of the SageMaker HyperPod cluster.</td></tr>
<tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>The name of the HyperPod Cluster.</td></tr>
<tr><td><CopyableCode code="failure_message" /></td><td><code>string</code></td><td>The failure message of the HyperPod Cluster.</td></tr>
<tr><td><CopyableCode code="orchestrator" /></td><td><code>object</code></td><td>Specifies parameter(s) specific to the orchestrator, e.g. specify the EKS cluster.</td></tr>
<tr><td><CopyableCode code="cluster_status" /></td><td><code>string</code></td><td>The status of the HyperPod Cluster.</td></tr>
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
cluster_arn,
vpc_config,
node_recovery,
creation_time,
instance_groups,
cluster_name,
failure_message,
orchestrator,
cluster_status,
tag_key,
tag_value
FROM aws.sagemaker.cluster_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>cluster_tags</code> resource, see <a href="/providers/aws/sagemaker/clusters/#permissions"><code>clusters</code></a>


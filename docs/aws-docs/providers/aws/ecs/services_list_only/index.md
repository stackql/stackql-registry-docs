---
title: services_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - services_list_only
  - ecs
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

Lists <code>services</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/services/"><code>services</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ECS::Service</code> resource creates an Amazon Elastic Container Service (Amazon ECS) service that runs and maintains the requested number of tasks and associated load balancers.<br />The stack update fails if you change any properties that require replacement and at least one ECS Service Connect <code>ServiceConnectConfiguration</code> property the is configured. This is because AWS CloudFormation creates the replacement service first, but each <code>ServiceConnectService</code> must have a name that is unique in the namespace.<br />Starting April 15, 2023, AWS; will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. After April 15, 2023, new customers will not be able to launch instances with Amazon EI accelerators in Amazon SageMaker, ECS, or EC2. However, customers who have used Amazon EI at least once during the past 30-day period are considered current customers and will be able to continue using the service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecs.services_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="service_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="cluster" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the cluster that you run your service on. If you do not specify a cluster, the default cluster is assumed.</td></tr>
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
Lists all <code>services</code> in a region.
```sql
SELECT
region,
service_arn,
cluster
FROM aws.ecs.services_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>services_list_only</code> resource, see <a href="/providers/aws/ecs/services/#permissions"><code>services</code></a>


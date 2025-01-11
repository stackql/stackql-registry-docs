---
title: continuous_deployment_policies_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - continuous_deployment_policies_list_only
  - cloudfront
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

Lists <code>continuous_deployment_policies</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/continuous_deployment_policies/"><code>continuous_deployment_policies</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>continuous_deployment_policies_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a continuous deployment policy that routes a subset of production traffic from a primary distribution to a staging distribution.<br />After you create and update a staging distribution, you can use a continuous deployment policy to incrementally move traffic to the staging distribution. This enables you to test changes to a distribution's configuration before moving all of your production traffic to the new configuration.<br />For more information, see &#91;Using CloudFront continuous deployment to safely test CDN configuration changes&#93;(https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/continuous-deployment.html) in the *Amazon CloudFront Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.continuous_deployment_policies_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>continuous_deployment_policies</code> in a region.
```sql
SELECT
region,
id
FROM aws.cloudfront.continuous_deployment_policies_list_only
;
```


## Permissions

For permissions required to operate on the <code>continuous_deployment_policies_list_only</code> resource, see <a href="/providers/aws/cloudfront/continuous_deployment_policies/#permissions"><code>continuous_deployment_policies</code></a>


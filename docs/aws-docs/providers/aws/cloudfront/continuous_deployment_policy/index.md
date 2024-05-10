---
title: continuous_deployment_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - continuous_deployment_policy
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


Gets or updates an individual <code>continuous_deployment_policy</code> resource, use <code>continuous_deployment_policies</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>continuous_deployment_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CloudFront::ContinuousDeploymentPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.continuous_deployment_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="continuous_deployment_policy_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
continuous_deployment_policy_config,
id,
last_modified_time
FROM aws.cloudfront.continuous_deployment_policy
WHERE data__Identifier = '<Id>';
```


## Permissions

To operate on the <code>continuous_deployment_policy</code> resource, the following permissions are required:

### Read
```json
cloudfront:GetContinuousDeploymentPolicy
```

### Update
```json
cloudfront:UpdateContinuousDeploymentPolicy,
cloudfront:GetContinuousDeploymentPolicy
```


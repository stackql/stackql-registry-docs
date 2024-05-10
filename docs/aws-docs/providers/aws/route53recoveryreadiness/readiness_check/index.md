---
title: readiness_check
hide_title: false
hide_table_of_contents: false
keywords:
  - readiness_check
  - route53recoveryreadiness
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


Gets or updates an individual <code>readiness_check</code> resource, use <code>readiness_checks</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>readiness_check</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Aws Route53 Recovery Readiness Check Schema and API specification.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoveryreadiness.readiness_check" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="resource_set_name" /></td><td><code>string</code></td><td>The name of the resource set to check.</td></tr>
<tr><td><CopyableCode code="readiness_check_name" /></td><td><code>string</code></td><td>Name of the ReadinessCheck to create.</td></tr>
<tr><td><CopyableCode code="readiness_check_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the readiness check.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource.</td></tr>
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
resource_set_name,
readiness_check_name,
readiness_check_arn,
tags
FROM aws.route53recoveryreadiness.readiness_check
WHERE region = 'us-east-1' AND data__Identifier = '<ReadinessCheckName>';
```


## Permissions

To operate on the <code>readiness_check</code> resource, the following permissions are required:

### Read
```json
route53-recovery-readiness:GetReadinessCheck,
route53-recovery-readiness:ListTagsForResources
```

### Update
```json
route53-recovery-readiness:UpdateReadinessCheck,
route53-recovery-readiness:GetResourceSet,
route53-recovery-readiness:GetReadinessCheck,
route53-recovery-readiness:ListTagsForResources,
route53-recovery-readiness:TagResource,
route53-recovery-readiness:UntagResource
```


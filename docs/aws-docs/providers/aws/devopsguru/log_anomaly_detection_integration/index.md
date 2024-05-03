---
title: log_anomaly_detection_integration
hide_title: false
hide_table_of_contents: false
keywords:
  - log_anomaly_detection_integration
  - devopsguru
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

Gets or operates on an individual <code>log_anomaly_detection_integration</code> resource, use <code>log_anomaly_detection_integrations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_anomaly_detection_integration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This resource schema represents the LogAnomalyDetectionIntegration resource in the Amazon DevOps Guru.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.devopsguru.log_anomaly_detection_integration" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td></td></tr>
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
account_id
FROM aws.devopsguru.log_anomaly_detection_integration
WHERE data__Identifier = '<AccountId>';
```

## Permissions

To operate on the <code>log_anomaly_detection_integration</code> resource, the following permissions are required:

### Read
```json
devops-guru:DescribeServiceIntegration
```

### Update
```json
devops-guru:UpdateServiceIntegration,
logs:TagLogGroup,
logs:UntagLogGroup
```

### Delete
```json
devops-guru:DescribeServiceIntegration,
devops-guru:UpdateServiceIntegration,
logs:TagLogGroup,
logs:UntagLogGroup
```


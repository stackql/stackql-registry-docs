---
title: log_anomaly_detection_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - log_anomaly_detection_integrations
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>log_anomaly_detection_integration</code> resource or lists <code>log_anomaly_detection_integrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_anomaly_detection_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This resource schema represents the LogAnomalyDetectionIntegration resource in the Amazon DevOps Guru.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.devopsguru.log_anomaly_detection_integrations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>User account id, used as the primary identifier for the resource</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>log_anomaly_detection_integrations</code> in a region.
```sql
SELECT
region,
account_id
FROM aws.devopsguru.log_anomaly_detection_integrations
WHERE region = 'us-east-1';
```
Gets all properties from a <code>log_anomaly_detection_integration</code>.
```sql
SELECT
region,
account_id
FROM aws.devopsguru.log_anomaly_detection_integrations
WHERE region = 'us-east-1' AND data__Identifier = '<AccountId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>log_anomaly_detection_integration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.devopsguru.log_anomaly_detection_integrations (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.devopsguru.log_anomaly_detection_integrations (
 ,
 region
)
SELECT 
 '{{  }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: log_anomaly_detection_integration
    props: []

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.devopsguru.log_anomaly_detection_integrations
WHERE data__Identifier = '<AccountId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>log_anomaly_detection_integrations</code> resource, the following permissions are required:

### Create
```json
devops-guru:DescribeServiceIntegration,
devops-guru:UpdateServiceIntegration,
logs:TagLogGroup,
logs:UntagLogGroup
```

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

### List
```json
devops-guru:DescribeServiceIntegration
```


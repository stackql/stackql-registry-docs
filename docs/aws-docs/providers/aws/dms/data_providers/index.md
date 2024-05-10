---
title: data_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - data_providers
  - dms
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


Used to retrieve a list of <code>data_providers</code> in a region or to create or delete a <code>data_providers</code> resource, use <code>data_provider</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DMS::DataProvider</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dms.data_providers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="data_provider_arn" /></td><td><code>string</code></td><td>The data provider ARN.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
data_provider_arn
FROM aws.dms.data_providers
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>data_provider</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- data_provider.iql (required properties only)
INSERT INTO aws.dms.data_providers (
 Engine,
 region
)
SELECT 
'{{ Engine }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- data_provider.iql (all properties)
INSERT INTO aws.dms.data_providers (
 DataProviderName,
 DataProviderIdentifier,
 Description,
 Engine,
 ExactSettings,
 Settings,
 Tags,
 region
)
SELECT 
 '{{ DataProviderName }}',
 '{{ DataProviderIdentifier }}',
 '{{ Description }}',
 '{{ Engine }}',
 '{{ ExactSettings }}',
 '{{ Settings }}',
 '{{ Tags }}',
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
  - name: data_provider
    props:
      - name: DataProviderName
        value: '{{ DataProviderName }}'
      - name: DataProviderIdentifier
        value: '{{ DataProviderIdentifier }}'
      - name: Description
        value: '{{ Description }}'
      - name: Engine
        value: '{{ Engine }}'
      - name: ExactSettings
        value: '{{ ExactSettings }}'
      - name: Settings
        value: {}
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.dms.data_providers
WHERE data__Identifier = '<DataProviderArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_providers</code> resource, the following permissions are required:

### Create
```json
dms:CreateDataProvider,
dms:ListDataProviders,
dms:DescribeDataProviders,
dms:AddTagsToResource,
dms:ListTagsForResource
```

### Delete
```json
dms:DeleteDataProvider
```

### List
```json
dms:ListDataProviders,
dms:DescribeDataProviders,
dms:ListTagsForResource
```


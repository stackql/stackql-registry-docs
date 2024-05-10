---
title: service_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - service_actions
  - servicecatalog
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


Used to retrieve a list of <code>service_actions</code> in a region or to create or delete a <code>service_actions</code> resource, use <code>service_action</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::ServiceCatalog::ServiceAction</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.servicecatalog.service_actions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
id
FROM aws.servicecatalog.service_actions
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>service_action</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- service_action.iql (required properties only)
INSERT INTO aws.servicecatalog.service_actions (
 Name,
 DefinitionType,
 Definition,
 region
)
SELECT 
'{{ Name }}',
 '{{ DefinitionType }}',
 '{{ Definition }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- service_action.iql (all properties)
INSERT INTO aws.servicecatalog.service_actions (
 AcceptLanguage,
 Name,
 DefinitionType,
 Definition,
 Description,
 region
)
SELECT 
 '{{ AcceptLanguage }}',
 '{{ Name }}',
 '{{ DefinitionType }}',
 '{{ Definition }}',
 '{{ Description }}',
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
  - name: service_action
    props:
      - name: AcceptLanguage
        value: '{{ AcceptLanguage }}'
      - name: Name
        value: '{{ Name }}'
      - name: DefinitionType
        value: '{{ DefinitionType }}'
      - name: Definition
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Description
        value: '{{ Description }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.servicecatalog.service_actions
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>service_actions</code> resource, the following permissions are required:

### Create
```json
servicecatalog:CreateServiceAction,
ssm:DescribeDocument,
iam:GetRole
```

### Delete
```json
servicecatalog:DeleteServiceAction
```

### List
```json
servicecatalog:ListServiceActions
```


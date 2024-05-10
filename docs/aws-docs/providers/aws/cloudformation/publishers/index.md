---
title: publishers
hide_title: false
hide_table_of_contents: false
keywords:
  - publishers
  - cloudformation
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


Used to retrieve a list of <code>publishers</code> in a region or to create or delete a <code>publishers</code> resource, use <code>publisher</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>publishers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Register as a publisher in the CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudformation.publishers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="publisher_id" /></td><td><code>string</code></td><td>The publisher id assigned by CloudFormation for publishing in this region.</td></tr>
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
publisher_id
FROM aws.cloudformation.publishers
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>publisher</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- publisher.iql (required properties only)
INSERT INTO aws.cloudformation.publishers (
 AcceptTermsAndConditions,
 region
)
SELECT 
'{{ AcceptTermsAndConditions }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- publisher.iql (all properties)
INSERT INTO aws.cloudformation.publishers (
 AcceptTermsAndConditions,
 ConnectionArn,
 region
)
SELECT 
 '{{ AcceptTermsAndConditions }}',
 '{{ ConnectionArn }}',
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
  - name: publisher
    props:
      - name: AcceptTermsAndConditions
        value: '{{ AcceptTermsAndConditions }}'
      - name: ConnectionArn
        value: '{{ ConnectionArn }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cloudformation.publishers
WHERE data__Identifier = '<PublisherId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>publishers</code> resource, the following permissions are required:

### Create
```json
cloudformation:RegisterPublisher,
cloudformation:DescribePublisher,
codestar-connections:GetConnection,
codestar-connections:UseConnection
```

### List
```json
cloudformation:DescribePublisher
```


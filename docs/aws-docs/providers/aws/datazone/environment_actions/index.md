---
title: environment_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_actions
  - datazone
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

Creates, updates, deletes or gets an <code>environment_action</code> resource or lists <code>environment_actions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::DataZone::EnvironmentActions Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.environment_actions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the Amazon DataZone environment action.</td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The identifier of the Amazon DataZone domain in which the environment is created.</td></tr>
<tr><td><CopyableCode code="domain_identifier" /></td><td><code>string</code></td><td>The identifier of the Amazon DataZone domain in which the environment would be created.</td></tr>
<tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The identifier of the Amazon DataZone environment in which the action is taking place</td></tr>
<tr><td><CopyableCode code="environment_identifier" /></td><td><code>string</code></td><td>The identifier of the Amazon DataZone environment in which the action is taking place</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone environment action.</td></tr>
<tr><td><CopyableCode code="identifier" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone environment action.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the environment action.</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>The parameters of the environment action.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentaction.html"><code>AWS::DataZone::EnvironmentActions</code></a>.

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
    <td><CopyableCode code="Name, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>environment_actions</code> in a region.
```sql
SELECT
region,
description,
domain_id,
domain_identifier,
environment_id,
environment_identifier,
id,
identifier,
name,
parameters
FROM aws.datazone.environment_actions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>environment_action</code>.
```sql
SELECT
region,
description,
domain_id,
domain_identifier,
environment_id,
environment_identifier,
id,
identifier,
name,
parameters
FROM aws.datazone.environment_actions
WHERE region = 'us-east-1' AND data__Identifier = '<DomainId>|<EnvironmentId>|<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environment_action</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.datazone.environment_actions (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datazone.environment_actions (
 Description,
 DomainIdentifier,
 EnvironmentIdentifier,
 Identifier,
 Name,
 Parameters,
 region
)
SELECT 
 '{{ Description }}',
 '{{ DomainIdentifier }}',
 '{{ EnvironmentIdentifier }}',
 '{{ Identifier }}',
 '{{ Name }}',
 '{{ Parameters }}',
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
  - name: environment_action
    props:
      - name: Description
        value: '{{ Description }}'
      - name: DomainIdentifier
        value: '{{ DomainIdentifier }}'
      - name: EnvironmentIdentifier
        value: '{{ EnvironmentIdentifier }}'
      - name: Identifier
        value: '{{ Identifier }}'
      - name: Name
        value: '{{ Name }}'
      - name: Parameters
        value:
          Uri: '{{ Uri }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.datazone.environment_actions
WHERE data__Identifier = '<DomainId|EnvironmentId|Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>environment_actions</code> resource, the following permissions are required:

### Create
```json
datazone:CreateEnvironmentAction,
datazone:GetEnvironmentAction,
datazone:DeleteEnvironmentAction
```

### Read
```json
datazone:GetEnvironmentAction
```

### Update
```json
datazone:UpdateEnvironmentAction,
datazone:GetEnvironmentAction,
datazone:DeleteEnvironmentAction
```

### Delete
```json
datazone:DeleteEnvironmentAction,
datazone:GetEnvironmentAction
```

### List
```json
datazone:ListEnvironmentActions
```

---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - vpclattice
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

Creates, updates, deletes or gets a <code>rule</code> resource or lists <code>rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="action" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="listener_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="match" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="priority" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="service_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-rule.html"><code>AWS::VpcLattice::Rule</code></a>.

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
    <td><CopyableCode code="Action, Match, Priority, region" /></td>
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
Gets all <code>rules</code> in a region.
```sql
SELECT
region,
action,
arn,
id,
listener_identifier,
match,
name,
priority,
service_identifier,
tags
FROM aws.vpclattice.rules
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>rule</code>.
```sql
SELECT
region,
action,
arn,
id,
listener_identifier,
match,
name,
priority,
service_identifier,
tags
FROM aws.vpclattice.rules
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rule</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.vpclattice.rules (
 Action,
 Match,
 Priority,
 region
)
SELECT 
'{{ Action }}',
 '{{ Match }}',
 '{{ Priority }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.vpclattice.rules (
 Action,
 ListenerIdentifier,
 Match,
 Name,
 Priority,
 ServiceIdentifier,
 Tags,
 region
)
SELECT 
 '{{ Action }}',
 '{{ ListenerIdentifier }}',
 '{{ Match }}',
 '{{ Name }}',
 '{{ Priority }}',
 '{{ ServiceIdentifier }}',
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
  - name: rule
    props:
      - name: Action
        value:
          Forward:
            TargetGroups:
              - TargetGroupIdentifier: '{{ TargetGroupIdentifier }}'
                Weight: '{{ Weight }}'
          FixedResponse:
            StatusCode: '{{ StatusCode }}'
      - name: ListenerIdentifier
        value: '{{ ListenerIdentifier }}'
      - name: Match
        value:
          HttpMatch:
            Method: '{{ Method }}'
            PathMatch:
              Match:
                Exact: '{{ Exact }}'
                Prefix: '{{ Prefix }}'
              CaseSensitive: '{{ CaseSensitive }}'
            HeaderMatches:
              - Name: '{{ Name }}'
                Match:
                  Exact: '{{ Exact }}'
                  Prefix: '{{ Prefix }}'
                  Contains: '{{ Contains }}'
                CaseSensitive: '{{ CaseSensitive }}'
      - name: Name
        value: '{{ Name }}'
      - name: Priority
        value: '{{ Priority }}'
      - name: ServiceIdentifier
        value: '{{ ServiceIdentifier }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.vpclattice.rules
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>rules</code> resource, the following permissions are required:

### Create
```json
vpc-lattice:CreateRule,
vpc-lattice:GetRule,
vpc-lattice:ListTagsForResource,
vpc-lattice:TagResource
```

### Read
```json
vpc-lattice:GetRule,
vpc-lattice:ListTagsForResource
```

### Update
```json
vpc-lattice:UpdateRule,
vpc-lattice:GetRule,
vpc-lattice:TagResource,
vpc-lattice:UntagResource,
vpc-lattice:ListTagsForResource
```

### Delete
```json
vpc-lattice:DeleteRule,
vpc-lattice:UntagResource
```

### List
```json
vpc-lattice:ListRules
```

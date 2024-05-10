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


Used to retrieve a list of <code>rules</code> in a region or to create or delete a <code>rules</code> resource, use <code>rule</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
arn
FROM aws.vpclattice.rules
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Action": {
  "Forward": {
   "TargetGroups": [
    {
     "TargetGroupIdentifier": "{{ TargetGroupIdentifier }}",
     "Weight": "{{ Weight }}"
    }
   ]
  },
  "FixedResponse": {
   "StatusCode": "{{ StatusCode }}"
  }
 },
 "Match": {
  "HttpMatch": {
   "Method": "{{ Method }}",
   "PathMatch": {
    "Match": {
     "Exact": "{{ Exact }}",
     "Prefix": "{{ Prefix }}"
    },
    "CaseSensitive": "{{ CaseSensitive }}"
   },
   "HeaderMatches": [
    {
     "Name": "{{ Name }}",
     "Match": {
      "Exact": "{{ Exact }}",
      "Prefix": "{{ Prefix }}",
      "Contains": "{{ Contains }}"
     },
     "CaseSensitive": "{{ CaseSensitive }}"
    }
   ]
  }
 },
 "Priority": "{{ Priority }}"
}
>>>
--required properties only
INSERT INTO aws.vpclattice.rules (
 Action,
 Match,
 Priority,
 region
)
SELECT 
{{ .Action }},
 {{ .Match }},
 {{ .Priority }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Action": {
  "Forward": {
   "TargetGroups": [
    {
     "TargetGroupIdentifier": "{{ TargetGroupIdentifier }}",
     "Weight": "{{ Weight }}"
    }
   ]
  },
  "FixedResponse": {
   "StatusCode": "{{ StatusCode }}"
  }
 },
 "ListenerIdentifier": "{{ ListenerIdentifier }}",
 "Match": {
  "HttpMatch": {
   "Method": "{{ Method }}",
   "PathMatch": {
    "Match": {
     "Exact": "{{ Exact }}",
     "Prefix": "{{ Prefix }}"
    },
    "CaseSensitive": "{{ CaseSensitive }}"
   },
   "HeaderMatches": [
    {
     "Name": "{{ Name }}",
     "Match": {
      "Exact": "{{ Exact }}",
      "Prefix": "{{ Prefix }}",
      "Contains": "{{ Contains }}"
     },
     "CaseSensitive": "{{ CaseSensitive }}"
    }
   ]
  }
 },
 "Name": "{{ Name }}",
 "Priority": "{{ Priority }}",
 "ServiceIdentifier": "{{ ServiceIdentifier }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
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
 {{ .Action }},
 {{ .ListenerIdentifier }},
 {{ .Match }},
 {{ .Name }},
 {{ .Priority }},
 {{ .ServiceIdentifier }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
vpc-lattice:DeleteRule
```

### List
```json
vpc-lattice:ListRules
```


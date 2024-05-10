---
title: run_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - run_groups
  - omics
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


Used to retrieve a list of <code>run_groups</code> in a region or to create or delete a <code>run_groups</code> resource, use <code>run_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>run_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Omics::RunGroup Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.omics.run_groups" /></td></tr>
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
FROM aws.omics.run_groups
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
 "MaxCpus": null,
 "MaxGpus": null,
 "MaxDuration": null,
 "MaxRuns": null,
 "Name": "{{ Name }}",
 "Tags": {}
}
>>>
--required properties only
INSERT INTO aws.omics.run_groups (
 MaxCpus,
 MaxGpus,
 MaxDuration,
 MaxRuns,
 Name,
 Tags,
 region
)
SELECT 
{{ MaxCpus }},
 {{ MaxGpus }},
 {{ MaxDuration }},
 {{ MaxRuns }},
 {{ Name }},
 {{ Tags }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "MaxCpus": null,
 "MaxGpus": null,
 "MaxDuration": null,
 "MaxRuns": null,
 "Name": "{{ Name }}",
 "Tags": {}
}
>>>
--all properties
INSERT INTO aws.omics.run_groups (
 MaxCpus,
 MaxGpus,
 MaxDuration,
 MaxRuns,
 Name,
 Tags,
 region
)
SELECT 
 {{ MaxCpus }},
 {{ MaxGpus }},
 {{ MaxDuration }},
 {{ MaxRuns }},
 {{ Name }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.omics.run_groups
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>run_groups</code> resource, the following permissions are required:

### Create
```json
omics:CreateRunGroup,
omics:TagResource
```

### Delete
```json
omics:DeleteRunGroup,
omics:GetRunGroup
```

### List
```json
omics:ListRunGroups
```


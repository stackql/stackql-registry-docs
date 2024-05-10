---
title: readiness_checks
hide_title: false
hide_table_of_contents: false
keywords:
  - readiness_checks
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


Used to retrieve a list of <code>readiness_checks</code> in a region or to create or delete a <code>readiness_checks</code> resource, use <code>readiness_check</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>readiness_checks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Aws Route53 Recovery Readiness Check Schema and API specification.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoveryreadiness.readiness_checks" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="readiness_check_name" /></td><td><code>string</code></td><td>Name of the ReadinessCheck to create.</td></tr>
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
readiness_check_name
FROM aws.route53recoveryreadiness.readiness_checks
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
 "ResourceSetName": "{{ ResourceSetName }}",
 "ReadinessCheckName": "{{ ReadinessCheckName }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.route53recoveryreadiness.readiness_checks (
 ResourceSetName,
 ReadinessCheckName,
 Tags,
 region
)
SELECT 
{{ ResourceSetName }},
 {{ ReadinessCheckName }},
 {{ Tags }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ResourceSetName": "{{ ResourceSetName }}",
 "ReadinessCheckName": "{{ ReadinessCheckName }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.route53recoveryreadiness.readiness_checks (
 ResourceSetName,
 ReadinessCheckName,
 Tags,
 region
)
SELECT 
 {{ ResourceSetName }},
 {{ ReadinessCheckName }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.route53recoveryreadiness.readiness_checks
WHERE data__Identifier = '<ReadinessCheckName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>readiness_checks</code> resource, the following permissions are required:

### Create
```json
route53-recovery-readiness:CreateReadinessCheck,
route53-recovery-readiness:GetResourceSet,
route53-recovery-readiness:GetReadinessCheck,
route53-recovery-readiness:ListTagsForResources,
route53-recovery-readiness:TagResource
```

### Delete
```json
route53-recovery-readiness:DeleteReadinessCheck,
route53-recovery-readiness:GetReadinessCheck
```

### List
```json
route53-recovery-readiness:ListReadinessChecks,
route53-recovery-readiness:GetReadinessChecks
```


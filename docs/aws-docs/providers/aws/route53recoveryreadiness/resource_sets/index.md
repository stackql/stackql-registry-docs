---
title: resource_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_sets
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


Used to retrieve a list of <code>resource_sets</code> in a region or to create or delete a <code>resource_sets</code> resource, use <code>resource_set</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for the AWS Route53 Recovery Readiness ResourceSet Resource and API.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoveryreadiness.resource_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="resource_set_name" /></td><td><code>string</code></td><td>The name of the resource set to create.</td></tr>
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
resource_set_name
FROM aws.route53recoveryreadiness.resource_sets
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
 "Resources": [
  {
   "ResourceArn": "{{ ResourceArn }}",
   "ComponentId": "{{ ComponentId }}",
   "DnsTargetResource": {
    "DomainName": "{{ DomainName }}",
    "RecordSetId": "{{ RecordSetId }}",
    "HostedZoneArn": "{{ HostedZoneArn }}",
    "RecordType": "{{ RecordType }}",
    "TargetResource": {
     "NLBResource": {
      "Arn": "{{ Arn }}"
     },
     "R53Resource": {
      "DomainName": "{{ DomainName }}",
      "RecordSetId": "{{ RecordSetId }}"
     }
    }
   },
   "ReadinessScopes": [
    "{{ ReadinessScopes[0] }}"
   ]
  }
 ],
 "ResourceSetType": "{{ ResourceSetType }}"
}
>>>
--required properties only
INSERT INTO aws.route53recoveryreadiness.resource_sets (
 Resources,
 ResourceSetType,
 region
)
SELECT 
{{ Resources }},
 {{ ResourceSetType }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ResourceSetName": "{{ ResourceSetName }}",
 "Resources": [
  {
   "ResourceArn": "{{ ResourceArn }}",
   "ComponentId": "{{ ComponentId }}",
   "DnsTargetResource": {
    "DomainName": "{{ DomainName }}",
    "RecordSetId": "{{ RecordSetId }}",
    "HostedZoneArn": "{{ HostedZoneArn }}",
    "RecordType": "{{ RecordType }}",
    "TargetResource": {
     "NLBResource": {
      "Arn": "{{ Arn }}"
     },
     "R53Resource": {
      "DomainName": "{{ DomainName }}",
      "RecordSetId": "{{ RecordSetId }}"
     }
    }
   },
   "ReadinessScopes": [
    "{{ ReadinessScopes[0] }}"
   ]
  }
 ],
 "ResourceSetType": "{{ ResourceSetType }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.route53recoveryreadiness.resource_sets (
 ResourceSetName,
 Resources,
 ResourceSetType,
 Tags,
 region
)
SELECT 
 {{ ResourceSetName }},
 {{ Resources }},
 {{ ResourceSetType }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.route53recoveryreadiness.resource_sets
WHERE data__Identifier = '<ResourceSetName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resource_sets</code> resource, the following permissions are required:

### Create
```json
route53-recovery-readiness:CreateResourceSet,
route53-recovery-readiness:GetResourceSet,
route53-recovery-readiness:GetRecoveryGroup,
route53-recovery-readiness:GetCell,
route53-recovery-readiness:ListTagsForResources,
route53-recovery-readiness:TagResource
```

### Delete
```json
route53-recovery-readiness:DeleteResourceSet,
route53-recovery-readiness:GetResourceSet
```

### List
```json
route53-recovery-readiness:ListResourceSets
```


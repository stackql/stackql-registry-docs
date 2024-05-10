---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - customerprofiles
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


Used to retrieve a list of <code>domains</code> in a region or to create or delete a <code>domains</code> resource, use <code>domain</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A domain defined for 3rd party data source in Profile Service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.domains" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
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
domain_name
FROM aws.customerprofiles.domains
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
 "DomainName": "{{ DomainName }}",
 "DefaultExpirationDays": "{{ DefaultExpirationDays }}"
}
>>>
--required properties only
INSERT INTO aws.customerprofiles.domains (
 DomainName,
 DefaultExpirationDays,
 region
)
SELECT 
{{ DomainName }},
 {{ DefaultExpirationDays }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DomainName": "{{ DomainName }}",
 "DeadLetterQueueUrl": "{{ DeadLetterQueueUrl }}",
 "DefaultEncryptionKey": "{{ DefaultEncryptionKey }}",
 "DefaultExpirationDays": "{{ DefaultExpirationDays }}",
 "Matching": {
  "Enabled": "{{ Enabled }}",
  "AutoMerging": {
   "Enabled": "{{ Enabled }}",
   "ConflictResolution": {
    "ConflictResolvingModel": "{{ ConflictResolvingModel }}",
    "SourceName": "{{ SourceName }}"
   },
   "Consolidation": {
    "MatchingAttributesList": [
     [
      "{{ 0[0] }}"
     ]
    ]
   },
   "MinAllowedConfidenceScoreForMerging": null
  },
  "ExportingConfig": {
   "S3Exporting": {
    "S3BucketName": "{{ S3BucketName }}",
    "S3KeyName": "{{ S3KeyName }}"
   }
  },
  "JobSchedule": {
   "DayOfTheWeek": "{{ DayOfTheWeek }}",
   "Time": "{{ Time }}"
  }
 },
 "RuleBasedMatching": {
  "Enabled": "{{ Enabled }}",
  "AttributeTypesSelector": {
   "AttributeMatchingModel": "{{ AttributeMatchingModel }}",
   "Address": [
    "{{ Address[0] }}"
   ],
   "EmailAddress": [
    "{{ EmailAddress[0] }}"
   ],
   "PhoneNumber": [
    "{{ PhoneNumber[0] }}"
   ]
  },
  "ConflictResolution": null,
  "ExportingConfig": null,
  "MatchingRules": [
   {
    "Rule": [
     "{{ Rule[0] }}"
    ]
   }
  ],
  "MaxAllowedRuleLevelForMatching": "{{ MaxAllowedRuleLevelForMatching }}",
  "MaxAllowedRuleLevelForMerging": "{{ MaxAllowedRuleLevelForMerging }}",
  "Status": "{{ Status }}"
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.customerprofiles.domains (
 DomainName,
 DeadLetterQueueUrl,
 DefaultEncryptionKey,
 DefaultExpirationDays,
 Matching,
 RuleBasedMatching,
 Tags,
 region
)
SELECT 
 {{ DomainName }},
 {{ DeadLetterQueueUrl }},
 {{ DefaultEncryptionKey }},
 {{ DefaultExpirationDays }},
 {{ Matching }},
 {{ RuleBasedMatching }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.customerprofiles.domains
WHERE data__Identifier = '<DomainName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>domains</code> resource, the following permissions are required:

### Create
```json
profile:CreateDomain,
profile:TagResource
```

### Delete
```json
profile:DeleteDomain
```

### List
```json
profile:ListDomains
```


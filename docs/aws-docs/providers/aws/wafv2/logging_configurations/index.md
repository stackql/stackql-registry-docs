---
title: logging_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - logging_configurations
  - wafv2
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


Used to retrieve a list of <code>logging_configurations</code> in a region or to create or delete a <code>logging_configurations</code> resource, use <code>logging_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logging_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A WAFv2 Logging Configuration Resource Provider</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wafv2.logging_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the web ACL that you want to associate with LogDestinationConfigs.</td></tr>
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
resource_arn
FROM aws.wafv2.logging_configurations
;
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
 "ResourceArn": "{{ ResourceArn }}",
 "LogDestinationConfigs": [
  "{{ LogDestinationConfigs[0] }}"
 ]
}
>>>
--required properties only
INSERT INTO aws.wafv2.logging_configurations (
 ResourceArn,
 LogDestinationConfigs,
 region
)
SELECT 
{{ .ResourceArn }},
 {{ .LogDestinationConfigs }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ResourceArn": "{{ ResourceArn }}",
 "LogDestinationConfigs": [
  "{{ LogDestinationConfigs[0] }}"
 ],
 "RedactedFields": [
  {
   "SingleHeader": {
    "Name": "{{ Name }}"
   },
   "SingleQueryArgument": {
    "Name": "{{ Name }}"
   },
   "AllQueryArguments": {},
   "UriPath": {},
   "QueryString": {},
   "Body": {
    "OversizeHandling": "{{ OversizeHandling }}"
   },
   "Method": {},
   "JsonBody": {
    "MatchPattern": {
     "All": {},
     "IncludedPaths": [
      "{{ IncludedPaths[0] }}"
     ]
    },
    "MatchScope": "{{ MatchScope }}",
    "InvalidFallbackBehavior": "{{ InvalidFallbackBehavior }}",
    "OversizeHandling": null
   },
   "Headers": {
    "MatchPattern": {
     "All": {},
     "IncludedHeaders": [
      "{{ IncludedHeaders[0] }}"
     ],
     "ExcludedHeaders": [
      "{{ ExcludedHeaders[0] }}"
     ]
    },
    "MatchScope": "{{ MatchScope }}",
    "OversizeHandling": null
   },
   "Cookies": {
    "MatchPattern": {
     "All": {},
     "IncludedCookies": [
      "{{ IncludedCookies[0] }}"
     ],
     "ExcludedCookies": [
      "{{ ExcludedCookies[0] }}"
     ]
    },
    "MatchScope": null,
    "OversizeHandling": null
   },
   "JA3Fingerprint": {
    "FallbackBehavior": "{{ FallbackBehavior }}"
   }
  }
 ],
 "LoggingFilter": {
  "DefaultBehavior": "{{ DefaultBehavior }}",
  "Filters": [
   {
    "Behavior": "{{ Behavior }}",
    "Conditions": [
     {
      "ActionCondition": {
       "Action": "{{ Action }}"
      },
      "LabelNameCondition": {
       "LabelName": "{{ LabelName }}"
      }
     }
    ],
    "Requirement": "{{ Requirement }}"
   }
  ]
 }
}
>>>
--all properties
INSERT INTO aws.wafv2.logging_configurations (
 ResourceArn,
 LogDestinationConfigs,
 RedactedFields,
 LoggingFilter,
 region
)
SELECT 
 {{ .ResourceArn }},
 {{ .LogDestinationConfigs }},
 {{ .RedactedFields }},
 {{ .LoggingFilter }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.wafv2.logging_configurations
WHERE data__Identifier = '<ResourceArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>logging_configurations</code> resource, the following permissions are required:

### Create
```json
wafv2:PutLoggingConfiguration,
wafv2:GetLoggingConfiguration,
firehose:ListDeliveryStreams,
iam:CreateServiceLinkedRole,
iam:DescribeOrganization,
logs:CreateLogDelivery,
s3:PutBucketPolicy,
s3:GetBucketPolicy,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups
```

### Delete
```json
wafv2:DeleteLoggingConfiguration,
wafv2:GetLoggingConfiguration,
logs:DeleteLogDelivery
```

### List
```json
wafv2:ListLoggingConfigurations
```


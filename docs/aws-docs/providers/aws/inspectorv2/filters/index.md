---
title: filters
hide_title: false
hide_table_of_contents: false
keywords:
  - filters
  - inspectorv2
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


Used to retrieve a list of <code>filters</code> in a region or to create or delete a <code>filters</code> resource, use <code>filter</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Inspector Filter resource schema</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.inspectorv2.filters" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Findings filter ARN.</td></tr>
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
FROM aws.inspectorv2.filters
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
 "Name": "{{ Name }}",
 "FilterCriteria": {
  "AwsAccountId": [
   {
    "Comparison": "{{ Comparison }}",
    "Value": "{{ Value }}"
   }
  ],
  "ComponentId": null,
  "ComponentType": null,
  "Ec2InstanceImageId": null,
  "Ec2InstanceSubnetId": null,
  "Ec2InstanceVpcId": null,
  "EcrImageArchitecture": null,
  "EcrImageHash": null,
  "EcrImageTags": null,
  "EcrImagePushedAt": [
   {
    "EndInclusive": "{{ EndInclusive }}",
    "StartInclusive": null
   }
  ],
  "EcrImageRegistry": null,
  "EcrImageRepositoryName": null,
  "FindingArn": null,
  "FindingStatus": null,
  "FindingType": null,
  "FirstObservedAt": null,
  "InspectorScore": [
   {
    "LowerInclusive": null,
    "UpperInclusive": null
   }
  ],
  "LastObservedAt": null,
  "NetworkProtocol": null,
  "PortRange": [
   {
    "BeginInclusive": "{{ BeginInclusive }}",
    "EndInclusive": null
   }
  ],
  "RelatedVulnerabilities": null,
  "ResourceId": null,
  "ResourceTags": [
   {
    "Comparison": "{{ Comparison }}",
    "Key": "{{ Key }}",
    "Value": "{{ Value }}"
   }
  ],
  "ResourceType": null,
  "Severity": null,
  "Title": null,
  "UpdatedAt": null,
  "VendorSeverity": null,
  "VulnerabilityId": null,
  "VulnerabilitySource": null,
  "VulnerablePackages": [
   {
    "Architecture": null,
    "Epoch": null,
    "Name": null,
    "Release": null,
    "SourceLayerHash": null,
    "Version": null
   }
  ]
 },
 "FilterAction": "{{ FilterAction }}"
}
>>>
--required properties only
INSERT INTO aws.inspectorv2.filters (
 Name,
 FilterCriteria,
 FilterAction,
 region
)
SELECT 
{{ .Name }},
 {{ .FilterCriteria }},
 {{ .FilterAction }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "FilterCriteria": {
  "AwsAccountId": [
   {
    "Comparison": "{{ Comparison }}",
    "Value": "{{ Value }}"
   }
  ],
  "ComponentId": null,
  "ComponentType": null,
  "Ec2InstanceImageId": null,
  "Ec2InstanceSubnetId": null,
  "Ec2InstanceVpcId": null,
  "EcrImageArchitecture": null,
  "EcrImageHash": null,
  "EcrImageTags": null,
  "EcrImagePushedAt": [
   {
    "EndInclusive": "{{ EndInclusive }}",
    "StartInclusive": null
   }
  ],
  "EcrImageRegistry": null,
  "EcrImageRepositoryName": null,
  "FindingArn": null,
  "FindingStatus": null,
  "FindingType": null,
  "FirstObservedAt": null,
  "InspectorScore": [
   {
    "LowerInclusive": null,
    "UpperInclusive": null
   }
  ],
  "LastObservedAt": null,
  "NetworkProtocol": null,
  "PortRange": [
   {
    "BeginInclusive": "{{ BeginInclusive }}",
    "EndInclusive": null
   }
  ],
  "RelatedVulnerabilities": null,
  "ResourceId": null,
  "ResourceTags": [
   {
    "Comparison": "{{ Comparison }}",
    "Key": "{{ Key }}",
    "Value": "{{ Value }}"
   }
  ],
  "ResourceType": null,
  "Severity": null,
  "Title": null,
  "UpdatedAt": null,
  "VendorSeverity": null,
  "VulnerabilityId": null,
  "VulnerabilitySource": null,
  "VulnerablePackages": [
   {
    "Architecture": null,
    "Epoch": null,
    "Name": null,
    "Release": null,
    "SourceLayerHash": null,
    "Version": null
   }
  ]
 },
 "FilterAction": "{{ FilterAction }}"
}
>>>
--all properties
INSERT INTO aws.inspectorv2.filters (
 Name,
 Description,
 FilterCriteria,
 FilterAction,
 region
)
SELECT 
 {{ .Name }},
 {{ .Description }},
 {{ .FilterCriteria }},
 {{ .FilterAction }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.inspectorv2.filters
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>filters</code> resource, the following permissions are required:

### Create
```json
inspector2:CreateFilter,
inspector2:ListFilters
```

### Delete
```json
inspector2:DeleteFilter,
inspector2:ListFilters
```

### List
```json
inspector2:ListFilters
```


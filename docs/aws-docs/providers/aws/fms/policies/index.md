---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - fms
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


Used to retrieve a list of <code>policies</code> in a region or to create or delete a <code>policies</code> resource, use <code>policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an AWS Firewall Manager policy.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.fms.policies" /></td></tr>
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
FROM aws.fms.policies
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
 "ExcludeResourceTags": "{{ ExcludeResourceTags }}",
 "PolicyName": "{{ PolicyName }}",
 "RemediationEnabled": "{{ RemediationEnabled }}",
 "SecurityServicePolicyData": {
  "ManagedServiceData": "{{ ManagedServiceData }}",
  "Type": "{{ Type }}",
  "PolicyOption": {
   "NetworkFirewallPolicy": {
    "FirewallDeploymentModel": "{{ FirewallDeploymentModel }}"
   },
   "ThirdPartyFirewallPolicy": {
    "FirewallDeploymentModel": null
   }
  }
 }
}
>>>
--required properties only
INSERT INTO aws.fms.policies (
 ExcludeResourceTags,
 PolicyName,
 RemediationEnabled,
 SecurityServicePolicyData,
 region
)
SELECT 
{{ .ExcludeResourceTags }},
 {{ .PolicyName }},
 {{ .RemediationEnabled }},
 {{ .SecurityServicePolicyData }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ExcludeMap": {
  "ACCOUNT": [
   "{{ ACCOUNT[0] }}"
  ],
  "ORGUNIT": [
   "{{ ORGUNIT[0] }}"
  ]
 },
 "ExcludeResourceTags": "{{ ExcludeResourceTags }}",
 "IncludeMap": null,
 "PolicyName": "{{ PolicyName }}",
 "PolicyDescription": "{{ PolicyDescription }}",
 "RemediationEnabled": "{{ RemediationEnabled }}",
 "ResourceTags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "ResourceType": "{{ ResourceType }}",
 "ResourceTypeList": [
  null
 ],
 "ResourceSetIds": [
  "{{ ResourceSetIds[0] }}"
 ],
 "SecurityServicePolicyData": {
  "ManagedServiceData": "{{ ManagedServiceData }}",
  "Type": "{{ Type }}",
  "PolicyOption": {
   "NetworkFirewallPolicy": {
    "FirewallDeploymentModel": "{{ FirewallDeploymentModel }}"
   },
   "ThirdPartyFirewallPolicy": {
    "FirewallDeploymentModel": null
   }
  }
 },
 "DeleteAllPolicyResources": "{{ DeleteAllPolicyResources }}",
 "ResourcesCleanUp": "{{ ResourcesCleanUp }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.fms.policies (
 ExcludeMap,
 ExcludeResourceTags,
 IncludeMap,
 PolicyName,
 PolicyDescription,
 RemediationEnabled,
 ResourceTags,
 ResourceType,
 ResourceTypeList,
 ResourceSetIds,
 SecurityServicePolicyData,
 DeleteAllPolicyResources,
 ResourcesCleanUp,
 Tags,
 region
)
SELECT 
 {{ .ExcludeMap }},
 {{ .ExcludeResourceTags }},
 {{ .IncludeMap }},
 {{ .PolicyName }},
 {{ .PolicyDescription }},
 {{ .RemediationEnabled }},
 {{ .ResourceTags }},
 {{ .ResourceType }},
 {{ .ResourceTypeList }},
 {{ .ResourceSetIds }},
 {{ .SecurityServicePolicyData }},
 {{ .DeleteAllPolicyResources }},
 {{ .ResourcesCleanUp }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.fms.policies
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>policies</code> resource, the following permissions are required:

### Create
```json
fms:PutPolicy,
fms:TagResource,
waf-regional:ListRuleGroups,
wafv2:CheckCapacity,
wafv2:ListRuleGroups,
wafv2:ListAvailableManagedRuleGroups,
wafv2:ListAvailableManagedRuleGroupVersions,
network-firewall:DescribeRuleGroup,
network-firewall:DescribeRuleGroupMetadata,
route53resolver:ListFirewallRuleGroups,
ec2:DescribeAvailabilityZones,
s3:PutBucketPolicy,
s3:GetBucketPolicy
```

### Delete
```json
fms:DeletePolicy
```

### List
```json
fms:ListPolicies,
fms:ListTagsForResource
```


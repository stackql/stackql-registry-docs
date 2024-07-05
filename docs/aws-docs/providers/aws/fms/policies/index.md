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

Creates, updates, deletes or gets a <code>policy</code> resource or lists <code>policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an AWS Firewall Manager policy.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.fms.policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="exclude_map" /></td><td><code>object</code></td><td>An FMS includeMap or excludeMap.</td></tr>
<tr><td><CopyableCode code="exclude_resource_tags" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="include_map" /></td><td><code>object</code></td><td>An FMS includeMap or excludeMap.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="remediation_enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>An AWS resource type</td></tr>
<tr><td><CopyableCode code="resource_type_list" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_set_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="security_service_policy_data" /></td><td><code>object</code></td><td>Firewall security service policy data.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>A resource ARN.</td></tr>
<tr><td><CopyableCode code="delete_all_policy_resources" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="resources_clean_up" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="ExcludeResourceTags, PolicyName, RemediationEnabled, SecurityServicePolicyData, region" /></td>
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
Gets all <code>policies</code> in a region.
```sql
SELECT
region,
exclude_map,
exclude_resource_tags,
include_map,
id,
policy_name,
policy_description,
remediation_enabled,
resource_tags,
resource_type,
resource_type_list,
resource_set_ids,
security_service_policy_data,
arn,
delete_all_policy_resources,
resources_clean_up,
tags
FROM aws.fms.policies
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>policy</code>.
```sql
SELECT
region,
exclude_map,
exclude_resource_tags,
include_map,
id,
policy_name,
policy_description,
remediation_enabled,
resource_tags,
resource_type,
resource_type_list,
resource_set_ids,
security_service_policy_data,
arn,
delete_all_policy_resources,
resources_clean_up,
tags
FROM aws.fms.policies
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.fms.policies (
 ExcludeResourceTags,
 PolicyName,
 RemediationEnabled,
 SecurityServicePolicyData,
 region
)
SELECT 
'{{ ExcludeResourceTags }}',
 '{{ PolicyName }}',
 '{{ RemediationEnabled }}',
 '{{ SecurityServicePolicyData }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ ExcludeMap }}',
 '{{ ExcludeResourceTags }}',
 '{{ IncludeMap }}',
 '{{ PolicyName }}',
 '{{ PolicyDescription }}',
 '{{ RemediationEnabled }}',
 '{{ ResourceTags }}',
 '{{ ResourceType }}',
 '{{ ResourceTypeList }}',
 '{{ ResourceSetIds }}',
 '{{ SecurityServicePolicyData }}',
 '{{ DeleteAllPolicyResources }}',
 '{{ ResourcesCleanUp }}',
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
  - name: policy
    props:
      - name: ExcludeMap
        value:
          ACCOUNT:
            - '{{ ACCOUNT[0] }}'
          ORGUNIT:
            - '{{ ORGUNIT[0] }}'
      - name: ExcludeResourceTags
        value: '{{ ExcludeResourceTags }}'
      - name: IncludeMap
        value: null
      - name: PolicyName
        value: '{{ PolicyName }}'
      - name: PolicyDescription
        value: '{{ PolicyDescription }}'
      - name: RemediationEnabled
        value: '{{ RemediationEnabled }}'
      - name: ResourceTags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: ResourceType
        value: '{{ ResourceType }}'
      - name: ResourceTypeList
        value:
          - null
      - name: ResourceSetIds
        value:
          - '{{ ResourceSetIds[0] }}'
      - name: SecurityServicePolicyData
        value:
          ManagedServiceData: '{{ ManagedServiceData }}'
          Type: '{{ Type }}'
          PolicyOption:
            NetworkFirewallPolicy:
              FirewallDeploymentModel: '{{ FirewallDeploymentModel }}'
            ThirdPartyFirewallPolicy:
              FirewallDeploymentModel: null
            NetworkAclCommonPolicy:
              NetworkAclEntrySet:
                FirstEntries:
                  - CidrBlock: '{{ CidrBlock }}'
                    Egress: '{{ Egress }}'
                    IcmpTypeCode:
                      Code: '{{ Code }}'
                      Type: '{{ Type }}'
                    Ipv6CidrBlock: '{{ Ipv6CidrBlock }}'
                    PortRange:
                      From: '{{ From }}'
                      To: '{{ To }}'
                    Protocol: '{{ Protocol }}'
                    RuleAction: '{{ RuleAction }}'
                ForceRemediateForFirstEntries: '{{ ForceRemediateForFirstEntries }}'
                LastEntries: null
                ForceRemediateForLastEntries: '{{ ForceRemediateForLastEntries }}'
      - name: DeleteAllPolicyResources
        value: '{{ DeleteAllPolicyResources }}'
      - name: ResourcesCleanUp
        value: '{{ ResourcesCleanUp }}'
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

### Update
```json
fms:PutPolicy,
fms:GetPolicy,
fms:TagResource,
fms:UntagResource,
fms:ListTagsForResource,
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

### Read
```json
fms:GetPolicy,
fms:ListTagsForResource
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


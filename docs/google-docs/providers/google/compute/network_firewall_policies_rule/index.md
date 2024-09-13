---
title: network_firewall_policies_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - network_firewall_policies_rule
  - compute
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>network_firewall_policies_rule</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_firewall_policies_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.network_firewall_policies_rule" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | An optional description for this resource. |
| <CopyableCode code="action" /> | `string` | The Action to perform when the client connection triggers the rule. Valid actions for firewall rules are: "allow", "deny", "apply_security_profile_group" and "goto_next". Valid actions for packet mirroring rules are: "mirror", "do_not_mirror" and "goto_next". |
| <CopyableCode code="direction" /> | `string` | The direction in which this rule applies. |
| <CopyableCode code="disabled" /> | `boolean` | Denotes whether the firewall policy rule is disabled. When set to true, the firewall policy rule is not enforced and traffic behaves as if it did not exist. If this is unspecified, the firewall policy rule will be enabled. |
| <CopyableCode code="enableLogging" /> | `boolean` | Denotes whether to enable logging for a particular rule. If logging is enabled, logs will be exported to the configured export destination in Stackdriver. Logs may be exported to BigQuery or Pub/Sub. Note: you cannot enable logging on "goto_next" rules. |
| <CopyableCode code="kind" /> | `string` | [Output only] Type of the resource. Returns compute#firewallPolicyRule for firewall rules and compute#packetMirroringRule for packet mirroring rules. |
| <CopyableCode code="match" /> | `object` | Represents a match condition that incoming traffic is evaluated against. Exactly one field must be specified. |
| <CopyableCode code="priority" /> | `integer` | An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest priority. |
| <CopyableCode code="ruleName" /> | `string` | An optional name for the rule. This field is not a unique identifier and can be updated. |
| <CopyableCode code="ruleTupleCount" /> | `integer` | [Output Only] Calculation of the complexity of a single firewall policy rule. |
| <CopyableCode code="securityProfileGroup" /> | `string` | A fully-qualified URL of a SecurityProfile resource instance. Example: https://networksecurity.googleapis.com/v1/projects/{project}/locations/{location}/securityProfileGroups/my-security-profile-group Must be specified if action is one of 'apply_security_profile_group' or 'mirror'. Cannot be specified for other actions. |
| <CopyableCode code="targetResources" /> | `array` | A list of network resource URLs to which this rule applies. This field allows you to control which network's VMs get this rule. If this field is left blank, all VMs within the organization will receive the rule. |
| <CopyableCode code="targetSecureTags" /> | `array` | A list of secure tags that controls which instances the firewall rule applies to. If targetSecureTag are specified, then the firewall rule applies only to instances in the VPC network that have one of those EFFECTIVE secure tags, if all the target_secure_tag are in INEFFECTIVE state, then this rule will be ignored. targetSecureTag may not be set at the same time as targetServiceAccounts. If neither targetServiceAccounts nor targetSecureTag are specified, the firewall rule applies to all instances on the specified network. Maximum number of target label tags allowed is 256. |
| <CopyableCode code="targetServiceAccounts" /> | `array` | A list of service accounts indicating the sets of instances that are applied with this rule. |
| <CopyableCode code="tlsInspect" /> | `boolean` | Boolean flag indicating if the traffic should be TLS decrypted. Can be set only if action = 'apply_security_profile_group' and cannot be set for other actions. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_rule" /> | `SELECT` | <CopyableCode code="firewallPolicy, project" /> | Gets a rule of the specified priority. |
| <CopyableCode code="add_rule" /> | `INSERT` | <CopyableCode code="firewallPolicy, project" /> | Inserts a rule into a firewall policy. |
| <CopyableCode code="remove_rule" /> | `DELETE` | <CopyableCode code="firewallPolicy, project" /> | Deletes a rule of the specified priority. |

## `SELECT` examples

Gets a rule of the specified priority.

```sql
SELECT
description,
action,
direction,
disabled,
enableLogging,
kind,
match,
priority,
ruleName,
ruleTupleCount,
securityProfileGroup,
targetResources,
targetSecureTags,
targetServiceAccounts,
tlsInspect
FROM google.compute.network_firewall_policies_rule
WHERE firewallPolicy = '{{ firewallPolicy }}'
AND project = '{{ project }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_firewall_policies_rule</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.compute.network_firewall_policies_rule (
firewallPolicy,
project,
kind,
ruleName,
description,
priority,
match,
action,
securityProfileGroup,
tlsInspect,
direction,
targetResources,
enableLogging,
ruleTupleCount,
targetServiceAccounts,
targetSecureTags,
disabled
)
SELECT 
'{{ firewallPolicy }}',
'{{ project }}',
'{{ kind }}',
'{{ ruleName }}',
'{{ description }}',
'{{ priority }}',
'{{ match }}',
'{{ action }}',
'{{ securityProfileGroup }}',
true|false,
'{{ direction }}',
'{{ targetResources }}',
true|false,
'{{ ruleTupleCount }}',
'{{ targetServiceAccounts }}',
'{{ targetSecureTags }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: kind
        value: '{{ kind }}'
      - name: ruleName
        value: '{{ ruleName }}'
      - name: description
        value: '{{ description }}'
      - name: priority
        value: '{{ priority }}'
      - name: match
        value: '{{ match }}'
      - name: action
        value: '{{ action }}'
      - name: securityProfileGroup
        value: '{{ securityProfileGroup }}'
      - name: tlsInspect
        value: '{{ tlsInspect }}'
      - name: direction
        value: '{{ direction }}'
      - name: targetResources
        value: '{{ targetResources }}'
      - name: enableLogging
        value: '{{ enableLogging }}'
      - name: ruleTupleCount
        value: '{{ ruleTupleCount }}'
      - name: targetServiceAccounts
        value: '{{ targetServiceAccounts }}'
      - name: targetSecureTags
        value: '{{ targetSecureTags }}'
      - name: disabled
        value: '{{ disabled }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>network_firewall_policies_rule</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.network_firewall_policies_rule
WHERE firewallPolicy = '{{ firewallPolicy }}'
AND project = '{{ project }}';
```

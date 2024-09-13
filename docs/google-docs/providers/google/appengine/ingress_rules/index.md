---
title: ingress_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - ingress_rules
  - appengine
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

Creates, updates, deletes or gets an <code>ingress_rule</code> resource or lists <code>ingress_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ingress_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.appengine.ingress_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | An optional string description of this rule. This field has a maximum length of 400 characters. |
| <CopyableCode code="action" /> | `string` | The action to take on matched requests. |
| <CopyableCode code="priority" /> | `integer` | A positive integer between 1, Int32.MaxValue-1 that defines the order of rule evaluation. Rules with the lowest priority are evaluated first.A default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when no previous rule matches. Only the action of this rule can be modified by the user. |
| <CopyableCode code="sourceRange" /> | `string` | IP address or range, defined using CIDR notation, of requests that this rule applies to. You can use the wildcard character "*" to match all IPs equivalent to "0/0" and "::/0" together. Examples: 192.168.1.1 or 192.168.0.0/16 or 2001:db8::/32 or 2001:0db8:0000:0042:0000:8a2e:0370:7334. Truncation will be silently performed on addresses which are not properly truncated. For example, 1.2.3.4/24 is accepted as the same address as 1.2.3.0/24. Similarly, for IPv6, 2001:db8::1/32 is accepted as the same address as 2001:db8::/32. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appsId, ingressRulesId" /> | Gets the specified firewall rule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appsId" /> | Lists the firewall rules of an application. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="appsId" /> | Creates a firewall rule for the application. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appsId, ingressRulesId" /> | Deletes the specified firewall rule. |
| <CopyableCode code="batch_update" /> | `UPDATE` | <CopyableCode code="appsId" /> | Replaces the entire firewall ruleset in one bulk operation. This overrides and replaces the rules of an existing firewall with the new rules.If the final rule does not match traffic with the '*' wildcard IP range, then an "allow all" rule is explicitly added to the end of the list. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="appsId, ingressRulesId" /> | Updates the specified firewall rule. |

## `SELECT` examples

Lists the firewall rules of an application.

```sql
SELECT
description,
action,
priority,
sourceRange
FROM google.appengine.ingress_rules
WHERE appsId = '{{ appsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ingress_rules</code> resource.

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
INSERT INTO google.appengine.ingress_rules (
appsId,
priority,
action,
sourceRange,
description
)
SELECT 
'{{ appsId }}',
'{{ priority }}',
'{{ action }}',
'{{ sourceRange }}',
'{{ description }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: priority
        value: '{{ priority }}'
      - name: action
        value: '{{ action }}'
      - name: sourceRange
        value: '{{ sourceRange }}'
      - name: description
        value: '{{ description }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a ingress_rule only if the necessary resources are available.

```sql
UPDATE google.appengine.ingress_rules
SET 
ingressRules = '{{ ingressRules }}'
WHERE 
appsId = '{{ appsId }}';
```

## `DELETE` example

Deletes the specified ingress_rule resource.

```sql
DELETE FROM google.appengine.ingress_rules
WHERE appsId = '{{ appsId }}'
AND ingressRulesId = '{{ ingressRulesId }}';
```

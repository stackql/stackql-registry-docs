
---
title: security_policies_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - security_policies_rule
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

Creates, updates, deletes or gets an <code>security_policies_rule</code> resource or lists <code>security_policies_rule</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_policies_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.security_policies_rule" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="action" /> | `string` | The Action to perform when the rule is matched. The following are the valid actions: - allow: allow access to target. - deny(STATUS): deny access to target, returns the HTTP response code specified. Valid values for `STATUS` are 403, 404, and 502. - rate_based_ban: limit client traffic to the configured threshold and ban the client if the traffic exceeds the threshold. Configure parameters for this action in RateLimitOptions. Requires rate_limit_options to be set. - redirect: redirect to a different target. This can either be an internal reCAPTCHA redirect, or an external URL-based redirect via a 302 response. Parameters for this action can be configured via redirectOptions. This action is only supported in Global Security Policies of type CLOUD_ARMOR. - throttle: limit client traffic to the configured threshold. Configure parameters for this action in rateLimitOptions. Requires rate_limit_options to be set for this.  |
| <CopyableCode code="headerAction" /> | `object` |  |
| <CopyableCode code="kind" /> | `string` | [Output only] Type of the resource. Always compute#securityPolicyRule for security policy rules |
| <CopyableCode code="match" /> | `object` | Represents a match condition that incoming traffic is evaluated against. Exactly one field must be specified. |
| <CopyableCode code="networkMatch" /> | `object` | Represents a match condition that incoming network traffic is evaluated against. |
| <CopyableCode code="preconfiguredWafConfig" /> | `object` |  |
| <CopyableCode code="preview" /> | `boolean` | If set to true, the specified action is not enforced. |
| <CopyableCode code="priority" /> | `integer` | An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest priority. |
| <CopyableCode code="rateLimitOptions" /> | `object` |  |
| <CopyableCode code="redirectOptions" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_rule" /> | `SELECT` | <CopyableCode code="project, securityPolicy" /> | Gets a rule at the specified priority. |
| <CopyableCode code="add_rule" /> | `INSERT` | <CopyableCode code="project, securityPolicy" /> | Inserts a rule into a security policy. |
| <CopyableCode code="remove_rule" /> | `DELETE` | <CopyableCode code="project, securityPolicy" /> | Deletes a rule at the specified priority. |

## `SELECT` examples

Gets a rule at the specified priority.

```sql
SELECT
description,
action,
headerAction,
kind,
match,
networkMatch,
preconfiguredWafConfig,
preview,
priority,
rateLimitOptions,
redirectOptions
FROM google.compute.security_policies_rule
WHERE project = '{{ project }}'
AND securityPolicy = '{{ securityPolicy }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_policies_rule</code> resource.

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
INSERT INTO google.compute.security_policies_rule (
project,
securityPolicy,
kind,
description,
priority,
match,
networkMatch,
action,
preview,
rateLimitOptions,
headerAction,
redirectOptions,
preconfiguredWafConfig
)
SELECT 
'{{ project }}',
'{{ securityPolicy }}',
'{{ kind }}',
'{{ description }}',
'{{ priority }}',
'{{ match }}',
'{{ networkMatch }}',
'{{ action }}',
true|false,
'{{ rateLimitOptions }}',
'{{ headerAction }}',
'{{ redirectOptions }}',
'{{ preconfiguredWafConfig }}'
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
      - name: description
        value: '{{ description }}'
      - name: priority
        value: '{{ priority }}'
      - name: match
        value: '{{ match }}'
      - name: networkMatch
        value: '{{ networkMatch }}'
      - name: action
        value: '{{ action }}'
      - name: preview
        value: '{{ preview }}'
      - name: rateLimitOptions
        value: '{{ rateLimitOptions }}'
      - name: headerAction
        value: '{{ headerAction }}'
      - name: redirectOptions
        value: '{{ redirectOptions }}'
      - name: preconfiguredWafConfig
        value: '{{ preconfiguredWafConfig }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified security_policies_rule resource.

```sql
DELETE FROM google.compute.security_policies_rule
WHERE project = '{{ project }}'
AND securityPolicy = '{{ securityPolicy }}';
```

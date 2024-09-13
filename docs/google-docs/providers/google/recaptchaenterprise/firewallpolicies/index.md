
---
title: firewallpolicies
hide_title: false
hide_table_of_contents: false
keywords:
  - firewallpolicies
  - recaptchaenterprise
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

Creates, updates, deletes or gets an <code>firewallpolicy</code> resource or lists <code>firewallpolicies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewallpolicies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recaptchaenterprise.firewallpolicies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name for the FirewallPolicy in the format `projects/{project}/firewallpolicies/{firewallpolicy}`. |
| <CopyableCode code="description" /> | `string` | Optional. A description of what this policy aims to achieve, for convenience purposes. The description can at most include 256 UTF-8 characters. |
| <CopyableCode code="actions" /> | `array` | Optional. The actions that the caller should take regarding user access. There should be at most one terminal action. A terminal action is any action that forces a response, such as `AllowAction`, `BlockAction` or `SubstituteAction`. Zero or more non-terminal actions such as `SetHeader` might be specified. A single policy can contain up to 16 actions. |
| <CopyableCode code="condition" /> | `string` | Optional. A CEL (Common Expression Language) conditional expression that specifies if this policy applies to an incoming user request. If this condition evaluates to true and the requested path matched the path pattern, the associated actions should be executed by the caller. The condition string is checked for CEL syntax correctness on creation. For more information, see the [CEL spec](https://github.com/google/cel-spec) and its [language definition](https://github.com/google/cel-spec/blob/master/doc/langdef.md). A condition has a max length of 500 characters. |
| <CopyableCode code="path" /> | `string` | Optional. The path for which this policy applies, specified as a glob pattern. For more information on glob, see the [manual page](https://man7.org/linux/man-pages/man7/glob.7.html). A path has a max length of 200 characters. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewallpoliciesId, projectsId" /> | Returns the specified firewall policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Returns the list of all firewall policies that belong to a project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new FirewallPolicy, specifying conditions at which reCAPTCHA Enterprise actions can be executed. A project may have a maximum of 1000 policies. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="firewallpoliciesId, projectsId" /> | Deletes the specified firewall policy. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="firewallpoliciesId, projectsId" /> | Updates the specified firewall policy. |
| <CopyableCode code="reorder" /> | `EXEC` | <CopyableCode code="projectsId" /> | Reorders all firewall policies. |

## `SELECT` examples

Returns the list of all firewall policies that belong to a project.

```sql
SELECT
name,
description,
actions,
condition,
path
FROM google.recaptchaenterprise.firewallpolicies
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>firewallpolicies</code> resource.

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
INSERT INTO google.recaptchaenterprise.firewallpolicies (
projectsId,
name,
condition,
description,
actions,
path
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ condition }}',
'{{ description }}',
'{{ actions }}',
'{{ path }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: condition
        value: '{{ condition }}'
      - name: description
        value: '{{ description }}'
      - name: actions
        value: '{{ actions }}'
      - name: path
        value: '{{ path }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a firewallpolicy only if the necessary resources are available.

```sql
UPDATE google.recaptchaenterprise.firewallpolicies
SET 
name = '{{ name }}',
condition = '{{ condition }}',
description = '{{ description }}',
actions = '{{ actions }}',
path = '{{ path }}'
WHERE 
firewallpoliciesId = '{{ firewallpoliciesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified firewallpolicy resource.

```sql
DELETE FROM google.recaptchaenterprise.firewallpolicies
WHERE firewallpoliciesId = '{{ firewallpoliciesId }}'
AND projectsId = '{{ projectsId }}';
```

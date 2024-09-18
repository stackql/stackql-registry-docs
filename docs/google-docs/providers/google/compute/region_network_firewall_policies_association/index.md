---
title: region_network_firewall_policies_association
hide_title: false
hide_table_of_contents: false
keywords:
  - region_network_firewall_policies_association
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

Creates, updates, deletes, gets or lists a <code>region_network_firewall_policies_association</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_network_firewall_policies_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_network_firewall_policies_association" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name for an association. |
| <CopyableCode code="attachmentTarget" /> | `string` | The target that the firewall policy is attached to. |
| <CopyableCode code="displayName" /> | `string` | [Output Only] Deprecated, please use short name instead. The display name of the firewall policy of the association. |
| <CopyableCode code="firewallPolicyId" /> | `string` | [Output Only] The firewall policy ID of the association. |
| <CopyableCode code="shortName" /> | `string` | [Output Only] The short name of the firewall policy of the association. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_association" /> | `SELECT` | <CopyableCode code="firewallPolicy, project, region" /> | Gets an association with the specified name. |
| <CopyableCode code="add_association" /> | `INSERT` | <CopyableCode code="firewallPolicy, project, region" /> | Inserts an association for the specified network firewall policy. |
| <CopyableCode code="remove_association" /> | `DELETE` | <CopyableCode code="firewallPolicy, project, region" /> | Removes an association for the specified network firewall policy. |

## `SELECT` examples

Gets an association with the specified name.

```sql
SELECT
name,
attachmentTarget,
displayName,
firewallPolicyId,
shortName
FROM google.compute.region_network_firewall_policies_association
WHERE firewallPolicy = '{{ firewallPolicy }}'
AND project = '{{ project }}'
AND region = '{{ region }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>region_network_firewall_policies_association</code> resource.

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
INSERT INTO google.compute.region_network_firewall_policies_association (
firewallPolicy,
project,
region,
name,
attachmentTarget,
firewallPolicyId,
shortName,
displayName
)
SELECT 
'{{ firewallPolicy }}',
'{{ project }}',
'{{ region }}',
'{{ name }}',
'{{ attachmentTarget }}',
'{{ firewallPolicyId }}',
'{{ shortName }}',
'{{ displayName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
attachmentTarget: string
firewallPolicyId: string
shortName: string
displayName: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>region_network_firewall_policies_association</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.region_network_firewall_policies_association
WHERE firewallPolicy = '{{ firewallPolicy }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```

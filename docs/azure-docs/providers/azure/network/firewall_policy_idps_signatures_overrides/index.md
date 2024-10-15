---
title: firewall_policy_idps_signatures_overrides
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policy_idps_signatures_overrides
  - network
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

Creates, updates, deletes, gets or lists a <code>firewall_policy_idps_signatures_overrides</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_policy_idps_signatures_overrides</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.firewall_policy_idps_signatures_overrides" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Will contain the resource id of the signature override resource |
| <CopyableCode code="name" /> | `string` | Contains the name of the resource (default) |
| <CopyableCode code="properties" /> | `object` | Will contain the properties of the resource (the actual signature overrides) |
| <CopyableCode code="type" /> | `string` | Will contain the type of the resource: Microsoft.Network/firewallPolicies/intrusionDetectionSignaturesOverrides |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Returns all signatures overrides for a specific policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Returns all signatures overrides objects for a specific policy as a list containing a single value. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Will update the status of policy's signature overrides for IDPS |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Will override/create a new signature overrides for the policy's IDPS |

## `SELECT` examples

Returns all signatures overrides for a specific policy.


```sql
SELECT
id,
name,
properties,
type
FROM azure.network.firewall_policy_idps_signatures_overrides
WHERE firewallPolicyName = '{{ firewallPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `UPDATE` example

Updates a <code>firewall_policy_idps_signatures_overrides</code> resource.

```sql
/*+ update */
UPDATE azure.network.firewall_policy_idps_signatures_overrides
SET 
name = '{{ name }}',
id = '{{ id }}',
type = '{{ type }}',
properties = '{{ properties }}'
WHERE 
firewallPolicyName = '{{ firewallPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>firewall_policy_idps_signatures_overrides</code> resource.

```sql
/*+ update */
REPLACE azure.network.firewall_policy_idps_signatures_overrides
SET 
name = '{{ name }}',
id = '{{ id }}',
type = '{{ type }}',
properties = '{{ properties }}'
WHERE 
firewallPolicyName = '{{ firewallPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

---
title: address_groups_references
hide_title: false
hide_table_of_contents: false
keywords:
  - address_groups_references
  - networksecurity
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

Creates, updates, deletes, gets or lists a <code>address_groups_references</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>address_groups_references</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.address_groups_references" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="firewallPolicy" /> | `string` | FirewallPolicy that is using the Address Group. |
| <CopyableCode code="rulePriority" /> | `integer` | Rule priority of the FirewallPolicy that is using the Address Group. |
| <CopyableCode code="securityPolicy" /> | `string` | Cloud Armor SecurityPolicy that is using the Address Group. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_address_groups_list_references" /> | `SELECT` | <CopyableCode code="addressGroupsId, locationsId, organizationsId" /> | Lists references of an address group. |
| <CopyableCode code="projects_locations_address_groups_list_references" /> | `SELECT` | <CopyableCode code="addressGroupsId, locationsId, projectsId" /> | Lists references of an address group. |

## `SELECT` examples

Lists references of an address group.

```sql
SELECT
firewallPolicy,
rulePriority,
securityPolicy
FROM google.networksecurity.address_groups_references
WHERE addressGroupsId = '{{ addressGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

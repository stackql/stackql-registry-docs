---
title: volumes_get_group_id_list_for_ldap_users
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes_get_group_id_list_for_ldap_users
  - netapp
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

Creates, updates, deletes, gets or lists a <code>volumes_get_group_id_list_for_ldap_users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes_get_group_id_list_for_ldap_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.volumes_get_group_id_list_for_ldap_users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="groupIdsForLdapUser" /> | `array` | Group Id list |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName, data__username" /> | Returns the list of group Ids for a specific LDAP User |

## `SELECT` examples

Returns the list of group Ids for a specific LDAP User


```sql
SELECT
groupIdsForLdapUser
FROM azure_isv.netapp.volumes_get_group_id_list_for_ldap_users
WHERE accountName = '{{ accountName }}'
AND poolName = '{{ poolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeName = '{{ volumeName }}'
AND data__username = '{{ data__username }}';
```